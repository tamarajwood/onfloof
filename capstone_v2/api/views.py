from rest_framework import generics, viewsets, permissions
from django.contrib.auth import get_user_model

from posts.models import Post, Subject, Comment
from adoption.models import Breed, Activity
from .serializers import BreedSerializer, ActivitySerializer, PostSerializer, SubjectSerializer, UserSerializer, CommentSerializer
from .permissions import IsAdminUserOrReadOnly, AdminReadOnly, PostOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [PostOnly]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAdminUserOrReadOnly]

# ## User viewset not really needed
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer 
    permission_classes = [AdminReadOnly]

# this one is the view set for the current logged in user
# which will only be me/admin, I don't think I need this
# for anything but not sure
class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user


