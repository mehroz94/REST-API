# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from rest_framework import generics
from .serializers import EmployeeSerializer, ProjectSerializer, ClientSerializer, ClientViewSerializer, EmpS
from .models import Employee, Project, Client, ProjectEmployee, ProjectClient
from rest_framework import permissions, authentication
from rest_framework.response import Response


class EmployeeView(generics.ListAPIView):
    """ To List all Employees """
    authentication_classes = ()
    permission_classes = ()
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreate(generics.CreateAPIView):
    """To create Employee """
    serializer_class = EmployeeSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new employee."""
        serializer.save()


class EmployeeDetailsView(generics.UpdateAPIView):
    """To Update Employee."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class ProjectView(generics.ListAPIView):
    """List all Projects."""
    authentication_classes = ()
    permission_classes = ()
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreate(generics.CreateAPIView):
    """Create new Project."""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new project."""
        serializer.save()


class ProjectDetailsView(generics.RetrieveUpdateAPIView):
    """This class handles the http GET and PUT requests on Project."""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ClientView(generics.ListAPIView):
    """List al Clients."""
    authentication_classes = ()
    permission_classes = ()
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientCreate(generics.CreateAPIView):
    """Create new client."""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new client."""
        serializer.save()


class ClientDetailsView(generics.ListAPIView):
    """View single client."""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ClientViewSerializer

    def get_queryset(self):
        _list = []
        client = Client.objects.filter(id=int(self.kwargs['pk']))
        obj = {}
        projects = Project.objects.filter(client=client).all()
        empl = Employee.objects.filter(project__in=projects).all()
        obj['client'] = client
        obj['projects'] = projects
        obj['employees'] = empl
        _list.append(obj)
        return _list


class ClientUpdateView(generics.RetrieveUpdateAPIView):
    """ Update a client."""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class AddEmployeeToProject(generics.CreateAPIView):
    """ Add Employee to Project"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EmpS

    def post(self, request, *args, **kwargs):
        project = self.kwargs['pk']
        emp = Employee.objects.get(pk=int(self.request.POST.get('employee', None)))
        proj = Project.objects.get(pk=int(project))
        ProjectEmployee.objects.create(project=proj, employee=emp)
        return Response(status=200)

    def get_queryset(self):
        ProjectEmployee.objects.all()


class AddProjectToClient(generics.CreateAPIView):
    """Add Project to Client"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EmpS

    def post(self, request, *args, **kwargs):
        client = self.kwargs['pk']
        project = Project.objects.get(pk=int(self.request.POST.get('project', None)))
        client = Client.objects.get(pk=int(client))
        ProjectClient.objects.create(client=client, project=project)
        return Response(status=200)

    def get_queryset(self):
        ProjectClient.objects.all()




