from django.db import models
import uuid


class BaseModelUnowned(models.Model):
    class Meta:
        abstract = True
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BaseModel(BaseModelUnowned):
    class Meta:
        abstract = True
    created_by = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True, related_name="%(class)s_created_by")
    updated_by = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True, related_name="%(class)s_updated_by")
