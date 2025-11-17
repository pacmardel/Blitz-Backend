"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Blitz API",
      default_version='v1',
      description="""
      # Blitz API Documentation
      
      A comprehensive RESTful API for Blitz, a professional networking platform for developers.
      
      ## Features
      - **User Authentication:** JWT-based authentication for secure access
      - **Developer Profiles:** Manage developer profiles with personal and professional information
      - **Skills:** Add and manage skills with proficiency levels
      - **Projects:** Showcase developer projects and portfolios
      - **Connections:** Connect and network with other developers
      - **Messaging:** Send and receive private messages
      - **Endorsements:** Endorse developers for their skills
      
      ## Authentication
      To access protected endpoints, you need to obtain a JWT token:
      1. POST to `/api/token/` with your username and password
      2. Use the returned `access` token in the Authorization header: `Bearer <your-access-token>`
      3. When the access token expires, use the `refresh` token at `/api/token/refresh/` to get a new access token
      """,
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@blitz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   patterns=[
       path('api/', include('api.urls')),
   ],
)

from django.views.generic.base import RedirectView
from rest_framework.response import Response
from rest_framework import status

# Enhanced JWT token views with Swagger documentation
class TokenObtainPairViewWithDocs(TokenObtainPairView):
    @swagger_auto_schema(
        operation_summary="Obtain JWT Token",
        operation_description="""
        Authenticate and obtain JWT access and refresh tokens.
        
        Provide your username and password to receive:
        - `access`: Short-lived token for API requests (typically expires in 5 minutes)
        - `refresh`: Long-lived token to obtain new access tokens (typically expires in 24 hours)
        
        Use the access token in subsequent requests by including it in the Authorization header:
        ```
        Authorization: Bearer <your-access-token>
        ```
        """,
        tags=["Authentication"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["username", "password"],
            properties={
                "username": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Your username",
                    example="developer"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_PASSWORD,
                    description="Your password",
                    example="yourpassword123"
                ),
            }
        ),
        responses={
            200: openapi.Response(
                description="Token obtained successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "access": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="JWT access token",
                            example="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
                        ),
                        "refresh": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="JWT refresh token",
                            example="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
                        ),
                    }
                ),
                examples={
                    "application/json": {
                        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjM5MDIyfQ...",
                        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjMyNTQyMn0..."
                    }
                }
            ),
            401: openapi.Response(
                description="Invalid credentials",
                examples={
                    "application/json": {
                        "detail": "No active account found with the given credentials"
                    }
                }
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TokenRefreshViewWithDocs(TokenRefreshView):
    @swagger_auto_schema(
        operation_summary="Refresh JWT Token",
        operation_description="""
        Obtain a new access token using a refresh token.
        
        When your access token expires, use your refresh token to get a new access token
        without needing to re-authenticate with your username and password.
        """,
        tags=["Authentication"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["refresh"],
            properties={
                "refresh": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Your refresh token",
                    example="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
                ),
            }
        ),
        responses={
            200: openapi.Response(
                description="New access token obtained successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "access": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="New JWT access token",
                            example="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
                        ),
                    }
                ),
                examples={
                    "application/json": {
                        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjM5MDIyfQ..."
                    }
                }
            ),
            401: openapi.Response(
                description="Invalid or expired refresh token",
                examples={
                    "application/json": {
                        "detail": "Token is invalid or expired"
                    }
                }
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

urlpatterns = [
    path('', RedirectView.as_view(url='/swagger/', permanent=False)),
    path("admin/", admin.site.urls),
    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairViewWithDocs.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshViewWithDocs.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
