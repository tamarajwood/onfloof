from rest_framework import serializers

from posts.models import Post, Subject
from users.models import CustomUser

class NestedSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject',)

class NestedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('title',)

class SubjectSerializer(serializers.ModelSerializer):
    post_detail = NestedPostSerializer(many=True, source="post", read_only=True)
    class Meta:
        model = Subject 
        fields = ('subject', 'post_detail')

class PostSerializer(serializers.ModelSerializer):
    subject_detail = NestedSubjectSerializer(many=True, source='subjects', read_only=True)
    class Meta:
        model = Post
        fields = ('title', 'subject_detail', 'created', 'previewImage', 'body')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username',)