# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Client(models.Model):
    """This class represents the client model."""

    name = models.CharField('Client name', max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # proj

    def __str__(self):
        return self.name


class Project(models.Model):
    """This class represents the project model."""

    status = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress')
    )
    name = models.CharField('Project name', max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=status)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """This class represents the employee model."""

    name = models.CharField(max_length=255)
    email = models.CharField('Employee email', max_length=255)
    designation = models.CharField('Employee designation', max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProjectEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
