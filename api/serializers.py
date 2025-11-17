from rest_framework import serializers
from .models import Profile, Skill, Project, Connection, Message, Endorsement

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Developer Profiles.
    
    Represents a developer's profile with personal information, social links, and professional details.
    """
    id = serializers.IntegerField(read_only=True, help_text="User ID (primary key)")
    email = serializers.EmailField(help_text="Email address of the developer")
    full_name = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True, help_text="Full name of the developer")
    bio = serializers.CharField(required=False, allow_blank=True, allow_null=True, help_text="Biography or description about the developer")
    avatar_url = serializers.URLField(required=False, allow_blank=True, allow_null=True, help_text="URL to the developer's avatar image")
    location = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True, help_text="Location of the developer")
    website = serializers.URLField(required=False, allow_blank=True, allow_null=True, help_text="Personal website URL")
    github_url = serializers.URLField(required=False, allow_blank=True, allow_null=True, help_text="GitHub profile URL")
    linkedin_url = serializers.URLField(required=False, allow_blank=True, allow_null=True, help_text="LinkedIn profile URL")
    twitter_url = serializers.URLField(required=False, allow_blank=True, allow_null=True, help_text="Twitter/X profile URL")
    years_experience = serializers.IntegerField(required=False, allow_null=True, help_text="Years of professional experience")
    open_to_work = serializers.BooleanField(default=False, help_text="Whether the developer is open to work opportunities")
    created_at = serializers.DateTimeField(read_only=True, help_text="Timestamp when the profile was created")
    updated_at = serializers.DateTimeField(read_only=True, help_text="Timestamp when the profile was last updated")
    
    class Meta:
        model = Profile
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    """
    Serializer for Developer Skills.
    
    Represents a skill with proficiency level that belongs to a developer profile.
    """
    id = serializers.UUIDField(read_only=True, help_text="Unique identifier for the skill")
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), help_text="ID of the profile this skill belongs to")
    skill_name = serializers.CharField(max_length=255, help_text="Name of the skill (e.g., 'Python', 'JavaScript', 'React')")
    proficiency = serializers.ChoiceField(
        choices=Skill.PROFICIENCY_CHOICES,
        help_text="Proficiency level: 'beginner', 'intermediate', 'advanced', or 'expert'"
    )
    created_at = serializers.DateTimeField(read_only=True, help_text="Timestamp when the skill was added")
    
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Developer Projects.
    
    Represents a project that showcases a developer's work.
    """
    id = serializers.UUIDField(read_only=True, help_text="Unique identifier for the project")
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), help_text="ID of the profile this project belongs to")
    title = serializers.CharField(max_length=255, help_text="Title of the project")
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True, help_text="Detailed description of the project")
    image_url = serializers.URLField(required=False, allow_blank=True, allow_null=True, help_text="URL to the project's image/thumbnail")
    project_url = serializers.URLField(required=False, allow_blank=True, allow_null=True, help_text="URL to the live project")
    github_url = serializers.URLField(required=False, allow_blank=True, allow_null=True, help_text="URL to the project's GitHub repository")
    technologies = serializers.CharField(required=False, allow_blank=True, allow_null=True, help_text="Comma-separated list of technologies used (e.g., 'React, Node.js, PostgreSQL')")
    created_at = serializers.DateTimeField(read_only=True, help_text="Timestamp when the project was created")
    updated_at = serializers.DateTimeField(read_only=True, help_text="Timestamp when the project was last updated")
    
    class Meta:
        model = Project
        fields = '__all__'

class ConnectionSerializer(serializers.ModelSerializer):
    """
    Serializer for Developer Connections.
    
    Represents a connection/follow relationship between two developers.
    """
    id = serializers.UUIDField(read_only=True, help_text="Unique identifier for the connection")
    follower = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), help_text="ID of the profile that is following")
    following = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), help_text="ID of the profile being followed")
    status = serializers.ChoiceField(
        choices=Connection.STATUS_CHOICES,
        default='connected',
        help_text="Connection status: 'pending' or 'connected'"
    )
    created_at = serializers.DateTimeField(read_only=True, help_text="Timestamp when the connection was created")
    
    class Meta:
        model = Connection
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Private Messages.
    
    Represents a private message sent between two developers.
    """
    id = serializers.UUIDField(read_only=True, help_text="Unique identifier for the message")
    sender = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), help_text="ID of the profile sending the message")
    receiver = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), help_text="ID of the profile receiving the message")
    content = serializers.CharField(help_text="Content/body of the message")
    read = serializers.BooleanField(default=False, read_only=True, help_text="Whether the message has been read")
    created_at = serializers.DateTimeField(read_only=True, help_text="Timestamp when the message was sent")
    
    class Meta:
        model = Message
        fields = '__all__'

class EndorsementSerializer(serializers.ModelSerializer):
    """
    Serializer for Skill Endorsements.
    
    Represents an endorsement given by one developer to another for a specific skill.
    """
    id = serializers.UUIDField(read_only=True, help_text="Unique identifier for the endorsement")
    endorser = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), help_text="ID of the profile giving the endorsement")
    endorsee = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), help_text="ID of the profile receiving the endorsement")
    skill = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), help_text="ID of the skill being endorsed")
    created_at = serializers.DateTimeField(read_only=True, help_text="Timestamp when the endorsement was given")
    
    class Meta:
        model = Endorsement
        fields = '__all__'
