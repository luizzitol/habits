from django.shortcuts import render
from .models import Project, ProjectUser, Invitation
from ninja import Router, Schema
from typing import List
import uuid


project_router = Router(tags=["Projects"])

class ProjectIn(Schema):
    name: str

class ProjectOut(Schema):
    id: uuid.UUID
    name: str

class ProjectListOut(Schema):
    projects: List[ProjectOut]


@project_router.get("/", response=ProjectListOut)
def get(request):
    user = request.user
    # get the projects that the user is a part of
    # users is a many to many field on the project model
    projects = Project.objects.filter(users=user)
    
    # serialize the projects    
    return {"projects": projects}

@project_router.post("/", response=ProjectOut)
def create(request, project: ProjectIn):
    user = request.user
    project = Project.objects.create(**project.dict())
    ProjectUser.objects.create(user=user, project=project, is_admin=True)
    return project
    


