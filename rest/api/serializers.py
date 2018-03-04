from rest_framework import serializers
from .models import Employee, Project, Client


class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer to map the Employee instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Employee
        fields = ('id', 'name','email', 'designation', 'project')
        read_only_fields = ('date_created', 'date_modified')


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer to map the Project instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Project
        fields = ('id', 'name','client', 'status')
        read_only_fields = ('date_created',)


class ClientSerializer(serializers.ModelSerializer):
    """Serializer to map the Client instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Client
        fields = ('id', 'name')
        read_only_fields = ('date_created','date_modified')


class ClientViewSerializer(serializers.Serializer):
    client = serializers.CharField()
    projects = serializers.CharField()
    employees = serializers.CharField()


class EmpS(serializers.ModelSerializer):
    pass
