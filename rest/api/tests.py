# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Employee, Project, Client

# Create your tests here.


class ClientModelTestCase(TestCase):
    """This class defines the test suite for the Client model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client_name = 'Pepsi'
        self.client = Client(name=self.client_name)

    def create_client(self):
        """Test the employee model can create a client."""
        old_count = Client.objects.count()
        self.client.save()
        new_count = Client.objects.count()
        self.assertNotEqual(old_count, new_count)


class ProjectModelTestCase(TestCase):
    """This class defines the test suite for the project model."""
    def setUp(self):
        """Define the test client and other test variables."""
        self.project_name = 'John'
        self.client = Client.objects.get()
        self.project_status = 'in_progress'
        self.project = Project(name=self.project_name, status=self.project_status,
                               client=self.client)

    def create_project(self):
        """Test the employee model can create a project."""
        old_count = Project.objects.count()
        self.project.save()
        new_count = Project.objects.count()
        self.assertNotEqual(old_count, new_count)


class EmployeeModelTestCase(TestCase):
    """This class defines the test suite for the employee model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.employee_name = 'John'
        self.project = Project.objects.get()
        self.employee_email = 'john@test.com'
        self.employee_designation = 'Software Engineer'
        self.employee = Employee(name=self.employee_name, email=self.employee_email,
                                 project=self.project, designation=self.employee_designation)

    def create_employee(self):
        """Test the employee model can create a employee."""
        old_count = Employee.objects.count()
        self.employee.save()
        new_count = Employee.objects.count()
        self.assertNotEqual(old_count, new_count)




class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.project = Project.objects.get()
        self.employee_data = {'name': 'John', 'email': 'john@test.com', 'designation': 'Software Engineer', 'project': self.project}
        self.response = self.client.post(
            reverse('add'),
            self.employee_data,
            format="json")

    def test_api_can_create_an_emplyee(self):
        """Test the api has employee creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_an_emplyee(self):
        """Test the api can get a given employee."""
        employee = Employee.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': employee.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, employee)
