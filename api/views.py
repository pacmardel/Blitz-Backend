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
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["email"],
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description="Email address"),
                "full_name": openapi.Schema(type=openapi.TYPE_STRING, description="Full name"),
                "bio": openapi.Schema(type=openapi.TYPE_STRING, description="Biography"),
                "avatar_url": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description="Avatar URL"),
                "location": openapi.Schema(type=openapi.TYPE_STRING, description="Location"),
                "website": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description="Website URL"),
                "github_url": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description="GitHub URL"),
                "linkedin_url": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description="LinkedIn URL"),
                "twitter_url": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description="Twitter URL"),
                "years_experience": openapi.Schema(type=openapi.TYPE_INTEGER, description="Years of experience"),
                "open_to_work": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Open to work"),
            },
            example={
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
                "open_to_work": True
            }
        ),
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
        operation_summary="Delete a developer profile",
        operation_description="Delete a developer profile by ID.",
        tags=["Profiles"],
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
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["profile", "skill_name", "proficiency"],
            properties={
                "profile": openapi.Schema(type=openapi.TYPE_INTEGER, description="Profile ID"),
                "skill_name": openapi.Schema(type=openapi.TYPE_STRING, description="Name of the skill"),
                "proficiency": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    enum=["beginner", "intermediate", "advanced", "expert"],
                    description="Proficiency level"
                ),
            },
            example={
                "profile": 1,
                "skill_name": "Python",
                "proficiency": "advanced"
            }
        ),
        responses={
            201: openapi.Response(description="Skill created successfully", schema=SkillSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

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
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["profile", "title"],
            properties={
                "profile": openapi.Schema(type=openapi.TYPE_INTEGER, description="Profile ID"),
                "title": openapi.Schema(type=openapi.TYPE_STRING, description="Project title"),
                "description": openapi.Schema(type=openapi.TYPE_STRING, description="Project description"),
                "image_url": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description="Project image URL"),
                "project_url": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description="Live project URL"),
                "github_url": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description="GitHub repository URL"),
                "technologies": openapi.Schema(type=openapi.TYPE_STRING, description="Comma-separated technologies"),
            },
            example={
                "profile": 1,
                "title": "E-Commerce Platform",
                "description": "A full-stack e-commerce platform built with React and Node.js",
                "image_url": "https://example.com/project.jpg",
                "project_url": "https://example.com/project",
                "github_url": "https://github.com/user/project",
                "technologies": "React, Node.js, PostgreSQL, Redis"
            }
        ),
        responses={
            201: openapi.Response(description="Project created successfully", schema=ProjectSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

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
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["follower", "following"],
            properties={
                "follower": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the profile that is following"),
                "following": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the profile being followed"),
                "status": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    enum=["pending", "connected"],
                    description="Connection status"
                ),
            },
            example={
                "follower": 1,
                "following": 2,
                "status": "connected"
            }
        ),
        responses={
            201: openapi.Response(description="Connection created successfully", schema=ConnectionSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

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
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["sender", "receiver", "content"],
            properties={
                "sender": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the profile sending the message"),
                "receiver": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the profile receiving the message"),
                "content": openapi.Schema(type=openapi.TYPE_STRING, description="Message content"),
            },
            example={
                "sender": 1,
                "receiver": 2,
                "content": "Hi! I'd like to connect and discuss potential collaboration opportunities."
            }
        ),
        responses={
            201: openapi.Response(description="Message sent successfully", schema=MessageSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

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
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["endorser", "endorsee", "skill"],
            properties={
                "endorser": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the profile giving the endorsement"),
                "endorsee": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the profile receiving the endorsement"),
                "skill": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="ID of the skill being endorsed"),
            },
            example={
                "endorser": 1,
                "endorsee": 2,
                "skill": "550e8400-e29b-41d4-a716-446655440000"
            }
        ),
        responses={
            201: openapi.Response(description="Endorsement created successfully", schema=EndorsementSerializer),
            400: openapi.Response(description="Bad request - Invalid data"),
            401: openapi.Response(description="Unauthorized - Authentication required"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
