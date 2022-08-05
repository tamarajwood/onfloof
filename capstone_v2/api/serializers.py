from xml.etree.ElementTree import Comment
from rest_framework import serializers

from posts.models import Post, Subject, Comment
from users.models import CustomUser
from adoption.models import Breed, Activity

class NestedSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject',)

class NestedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('title', 'id')

class NestedCommentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', 'created')

class NestedBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('breed', 'endurance', 'id')

class NestedActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('activity',)

class SubjectSerializer(serializers.ModelSerializer):
    post_detail = NestedPostSerializer(many=True, source="post", read_only=True)
    class Meta:
        model = Subject 
        fields = ('subject', 'post_detail')

class PostSerializer(serializers.ModelSerializer):
    comment_detail = NestedCommentSerialzer(many=True, source='comments', read_only=True)
    subject_detail = NestedSubjectSerializer(many=True, source='subjects', read_only=True)
    class Meta:
        model = Post
        fields = ('title', 'id', 'subject_detail', 'created', 'previewImage', 'body', 'comment_detail', 'previewText')

class CommentSerializer(serializers.ModelSerializer):
    post_detail = NestedPostSerializer(many=True, source="post", read_only=True)
    class Meta:
        model = Comment
        fields = ('comment', 'created', 'post_detail', 'post')
    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['post_detail'] = PostSerializer(
    #         Post.objects.get(pk=data['post_detail'])).data
    #     return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username',)

class BreedSerializer(serializers.ModelSerializer):
    activity_detail = NestedActivitySerializer(many=True, source='activity', read_only=True)
    # ^ this is NOT WORKING I am not sure why but I don't actually need it so I will mess around with it when I have time
    class Meta:
        model = Breed
        fields = ('breed', 'endurance', 'id', 'activity_detail')

class ActivitySerializer(serializers.ModelSerializer):
    breed_detail = NestedBreedSerializer(many=True, source='breed', read_only=True)
    class Meta:
        model = Activity
        fields = ('activity', 'breed_detail')