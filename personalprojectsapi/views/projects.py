"""View module for handling requests about park areas"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from personalprojectsapi.models import Project

class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for projects

    Arguments:
        serializers.HyperlinkedModelSerializer
    """

    class Meta:
        model = Project
        url = serializers.HyperlinkedIdentityField(
            view_name="projects",
            lookup_field="id"
        )
        fields = (
            "id",
            "url",
            "available",
            "description",
            "github_url",
            "screenshot",
            "technologies_used",
            "title",
            "project_url"
            )

class Projects(ViewSet):
    """Projects view for personal projects api"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single project
        Returns:
            Response -- JSON serialized project instance
        """
        try:
            area = Project.objects.get(pk=pk)
            serializer = ProjectsSerializer(area, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests for personal projects api

        Returns:
            Response -- JSON serialized list of projects
        """
        projects = Project.objects.all()
        serializer = ProjectsSerializer(
            projects,
            many=True,
            context={"request": request}
        )
        return Response(serializer.data)
