from django.db import models
from core.models import BaseModel, BaseModelUnowned

class Project(BaseModel):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField("accounts.User", related_name="project_users", through="projects.ProjectUser")


class ProjectUser(BaseModelUnowned):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "project")


class Invitation(BaseModel):
    email = models.EmailField()
    message = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="invitations")

    class Meta:
        unique_together = ("email", "project")

