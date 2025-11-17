from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Profile, Skill, Project, Connection, Message, Endorsement
from .serializers import (
    ProfileSerializer,
    SkillSerializer,
    ProjectSerializer,
    ConnectionSerializer,
    MessageSerializer,
    EndorsementSerializer,
)

class ProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing developer profiles.
    
    Provides CRUD operations for developer profiles including personal information,
    social links, and professional details.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    @swagger_auto_schema(
        operation_summary="List all developer profiles",
        operation_description="Retrieve a list of all developer profiles with their information.",
        tags=["Profiles"],
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=ProfileSerializer(many=True),
                examples={
                    "application/json": {
                        "count": 2,
                        "results": [
                            {
                                "id": 1,
                                "email": "developer@example.com",
                                "full_name": "John Doe",
                                "bio": "Full-stack developer with 5 years of experience",
                                "avatar_url": "https://example.com/avatar.jpg",
                                "location": "San Francisco, CA",
                                "website": "https://johndoe.dev",
                                "github_url": "https://github.com/johndoe",
                                "linkedin_url": "https://linkedin.com/in/johndoe",
                                "twitter_url": "https://twitter.com/johndoe",
                                "years_experience": 5,
                                "open_to_work": True,
                                "created_at": "2024-01-01T00:00:00Z",
                                "updated_at": "2024-01-01T00:00:00Z"
                            }
                        ]
                    }
                }
            ),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Retrieve a developer profile",
        operation_description="Get detailed information about a specific developer profile by ID.",
        tags=["Profiles"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID of the profile to retrieve",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=ProfileSerializer,
                examples={
                    "application/json": {
                        "id": 1,
                        "email": "developer@example.com",
                        "full_name": "John Doe",
                        "bio": "Full-stack developer with 5 years of experience",
                        "avatar_url": "https://example.com/avatar.jpg",
                        "location": "San Francisco, CA",
                        "website": "https://johndoe.dev",
                        "github_url": "https://github.com/johndoe",
                        "linkedin_url": "https://linkedin.com/in/johndoe",
                        "twitter_url": "https://twitter.com/johndoe",
                        "years_experience": 5,
                        "open_to_work": True,
                        "created_at": "2024-01-01T00:00:00Z",
                        "updated_at": "2024-01-01T00:00:00Z"
                    }
                }
            ),
            404: openapi.Response(description="Profile not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Create a new developer profile",
        operation_description="Create a new developer profile with the provided information.",
        tags=["Profiles"],
        request_body=ProfileSerializer,
        responses={
            201: openapi.Response(description="Profile created successfully", schema=ProfileSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update a developer profile",
        operation_description="Update an existing developer profile. Use PATCH for partial updates.",
        tags=["Profiles"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID of the profile to update",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        request_body=ProfileSerializer,
        responses={
            200: openapi.Response(description="Profile updated successfully", schema=ProfileSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            404: openapi.Response(description="Profile not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Partially update a developer profile",
        operation_description="Partially update an existing developer profile (PATCH method).",
        tags=["Profiles"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID of the profile to update",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        request_body=ProfileSerializer,
        responses={
            200: openapi.Response(description="Profile updated successfully", schema=ProfileSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            404: openapi.Response(description="Profile not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Delete a developer profile",
        operation_description="Delete a developer profile by ID.",
        tags=["Profiles"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID of the profile to delete",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        responses={
            204: openapi.Response(description="Profile deleted successfully"),
            404: openapi.Response(description="Profile not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class SkillViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing developer skills.
    
    Provides CRUD operations for skills associated with developer profiles.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
    @swagger_auto_schema(
        operation_summary="List all skills",
        operation_description="Retrieve a list of all skills across all developer profiles.",
        tags=["Skills"],
        responses={
            200: openapi.Response(description="Successful response", schema=SkillSerializer(many=True)),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Create a new skill",
        operation_description="Add a new skill to a developer profile.",
        tags=["Skills"],
        request_body=SkillSerializer,
        responses={
            201: openapi.Response(description="Skill created successfully", schema=SkillSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Retrieve a skill",
        operation_description="Get detailed information about a specific skill by ID.",
        tags=["Skills"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the skill to retrieve",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        responses={
            200: openapi.Response(description="Successful response", schema=SkillSerializer),
            404: openapi.Response(description="Skill not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update a skill",
        operation_description="Update an existing skill.",
        tags=["Skills"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the skill to update",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        request_body=SkillSerializer,
        responses={
            200: openapi.Response(description="Skill updated successfully", schema=SkillSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            404: openapi.Response(description="Skill not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Delete a skill",
        operation_description="Delete a skill by ID.",
        tags=["Skills"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the skill to delete",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        responses={
            204: openapi.Response(description="Skill deleted successfully"),
            404: openapi.Response(description="Skill not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing developer projects.
    
    Provides CRUD operations for projects that showcase developer work.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    @swagger_auto_schema(
        operation_summary="List all projects",
        operation_description="Retrieve a list of all projects across all developer profiles.",
        tags=["Projects"],
        responses={
            200: openapi.Response(description="Successful response", schema=ProjectSerializer(many=True)),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Create a new project",
        operation_description="Add a new project to showcase developer work.",
        tags=["Projects"],
        request_body=ProjectSerializer,
        responses={
            201: openapi.Response(description="Project created successfully", schema=ProjectSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Retrieve a project",
        operation_description="Get detailed information about a specific project by ID.",
        tags=["Projects"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the project to retrieve",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        responses={
            200: openapi.Response(description="Successful response", schema=ProjectSerializer),
            404: openapi.Response(description="Project not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update a project",
        operation_description="Update an existing project.",
        tags=["Projects"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the project to update",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        request_body=ProjectSerializer,
        responses={
            200: openapi.Response(description="Project updated successfully", schema=ProjectSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            404: openapi.Response(description="Project not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Delete a project",
        operation_description="Delete a project by ID.",
        tags=["Projects"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the project to delete",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        responses={
            204: openapi.Response(description="Project deleted successfully"),
            404: openapi.Response(description="Project not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ConnectionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing developer connections.
    
    Provides CRUD operations for connections/follow relationships between developers.
    """
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    
    @swagger_auto_schema(
        operation_summary="List all connections",
        operation_description="Retrieve a list of all connections between developers.",
        tags=["Connections"],
        responses={
            200: openapi.Response(description="Successful response", schema=ConnectionSerializer(many=True)),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Create a new connection",
        operation_description="Create a connection between two developers.",
        tags=["Connections"],
        request_body=ConnectionSerializer,
        responses={
            201: openapi.Response(description="Connection created successfully", schema=ConnectionSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Retrieve a connection",
        operation_description="Get detailed information about a specific connection by ID.",
        tags=["Connections"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the connection to retrieve",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        responses={
            200: openapi.Response(description="Successful response", schema=ConnectionSerializer),
            404: openapi.Response(description="Connection not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update a connection",
        operation_description="Update an existing connection.",
        tags=["Connections"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the connection to update",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        request_body=ConnectionSerializer,
        responses={
            200: openapi.Response(description="Connection updated successfully", schema=ConnectionSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            404: openapi.Response(description="Connection not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Delete a connection",
        operation_description="Delete a connection by ID.",
        tags=["Connections"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the connection to delete",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        responses={
            204: openapi.Response(description="Connection deleted successfully"),
            404: openapi.Response(description="Connection not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing private messages.
    
    Provides CRUD operations for private messages between developers.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    @swagger_auto_schema(
        operation_summary="List all messages",
        operation_description="Retrieve a list of all messages between developers.",
        tags=["Messages"],
        responses={
            200: openapi.Response(description="Successful response", schema=MessageSerializer(many=True)),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Send a new message",
        operation_description="Send a private message from one developer to another.",
        tags=["Messages"],
        request_body=MessageSerializer,
        responses={
            201: openapi.Response(description="Message sent successfully", schema=MessageSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Retrieve a message",
        operation_description="Get detailed information about a specific message by ID.",
        tags=["Messages"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the message to retrieve",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        responses={
            200: openapi.Response(description="Successful response", schema=MessageSerializer),
            404: openapi.Response(description="Message not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update a message",
        operation_description="Update an existing message.",
        tags=["Messages"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the message to update",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        request_body=MessageSerializer,
        responses={
            200: openapi.Response(description="Message updated successfully", schema=MessageSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            404: openapi.Response(description="Message not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Delete a message",
        operation_description="Delete a message by ID.",
        tags=["Messages"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the message to delete",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        responses={
            204: openapi.Response(description="Message deleted successfully"),
            404: openapi.Response(description="Message not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class EndorsementViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing skill endorsements.
    
    Provides CRUD operations for endorsements given by developers to other developers for specific skills.
    """
    queryset = Endorsement.objects.all()
    serializer_class = EndorsementSerializer
    
    @swagger_auto_schema(
        operation_summary="List all endorsements",
        operation_description="Retrieve a list of all skill endorsements.",
        tags=["Endorsements"],
        responses={
            200: openapi.Response(description="Successful response", schema=EndorsementSerializer(many=True)),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Create a new endorsement",
        operation_description="Endorse another developer for a specific skill.",
        tags=["Endorsements"],
        request_body=EndorsementSerializer,
        responses={
            201: openapi.Response(description="Endorsement created successfully", schema=EndorsementSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Retrieve an endorsement",
        operation_description="Get detailed information about a specific endorsement by ID.",
        tags=["Endorsements"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the endorsement to retrieve",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        responses={
            200: openapi.Response(description="Successful response", schema=EndorsementSerializer),
            404: openapi.Response(description="Endorsement not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update an endorsement",
        operation_description="Update an existing endorsement.",
        tags=["Endorsements"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the endorsement to update",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        request_body=EndorsementSerializer,
        responses={
            200: openapi.Response(description="Endorsement updated successfully", schema=EndorsementSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            404: openapi.Response(description="Endorsement not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Delete an endorsement",
        operation_description="Delete an endorsement by ID.",
        tags=["Endorsements"],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="UUID of the endorsement to delete",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True
            ),
        ],
        responses={
            204: openapi.Response(description="Endorsement deleted successfully"),
            404: openapi.Response(description="Endorsement not found"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
