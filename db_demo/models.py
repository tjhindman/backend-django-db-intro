from django.db import models

from django.contrib.auth.models import User


class Roles(models.Model):
    title=models.CharField(max_length=20)

class Permissions(models.Model):
    title=models.CharField(max_length=20)

class Categories(models.Model):
    parent=models.ForeignKey(Categories, on_delete=models.CASCADE)
    title=models.CharField(max_length=20)

# Unsure about contributors model.
class Contributors(models.Model):
    role=models.ForeignKey(Roles, on_delete=models.CASCADE)

class Pages(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    is_flagged=models.BooleanField(default=False)
    is_published=models.BooleanField(default=False)
    contributors=models.ForeignKey(Contributors, on_delete=models.CASCADE)
    tags=models.ForeignKey(Tags, on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    body=models.TextField()

class Profiles(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    # Not sure how to reference an image path.
    avatar=models.TextField()

class Tags(models.Model):
    body=models.TextField()

class UserRoles(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    role=models.ForeignKey(Roles, on_delete=models.CASCADE)

class RolePermissions(models.Model):
    role=models.ForeignKey(Roles, on_delete=models.CASCADE)
    permissions=models.ForeignKey(Permissions, on_delete=models.CASCADE)

class ContributorRoles(models.Model):
    contributor=models.ForeignKey(Contributors, on_delete=models.CASCADE)
    role=models.ForeignKey(Roles, on_delete=models.CASCADE)

class PageCategory(models.Model):
    page=models.ForeignKey(Pages, on_delete=models.CASCADE)
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
