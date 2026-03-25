from rest_framework import serializers
from .models import User, globalmail, MailReply, podcast, uploadedpodcast


class UserSerializer(serializers.ModelSerializer):
    membership_type_display = serializers.CharField(source='get_membership_type_display', read_only=True)
    court_type_display = serializers.CharField(source='get_court_type_display', read_only=True)
    user_type_display = serializers.CharField(source='get_user_type_display', read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username',
            'user_type', 'user_type_display',
            'membership_type', 'membership_type_display',
            'court_type', 'court_type_display',
            'child_name', 'child_age',
            'profile_picture', 'is_verified',
        ]
        read_only_fields = ['id', 'is_verified']


class MailReplySerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = MailReply
        fields = ['id', 'mail', 'user', 'user_email', 'reply_content', 'created_at']
        read_only_fields = ['id', 'created_at']


class GlobalMailSerializer(serializers.ModelSerializer):
    replies = MailReplySerializer(many=True, read_only=True)

    class Meta:
        model = globalmail
        fields = ['id', 'mailtitel', 'mailbody', 'reply_mail', 'created_at', 'replies']
        read_only_fields = ['id', 'created_at']


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = podcast
        fields = ['id', 'podcasttitel', 'video', 'thumbnail', 'created_at']
        read_only_fields = ['id', 'created_at']


class UploadedPodcastSerializer(serializers.ModelSerializer):
    podcast_detail = PodcastSerializer(source='podcast', read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = uploadedpodcast
        fields = ['id', 'podcast', 'podcast_detail', 'user', 'user_email', 'created_at']
        read_only_fields = ['id', 'created_at']
