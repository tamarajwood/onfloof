from rest_framework import generics, viewsets, permissions
from django.contrib.auth import get_user_model

from posts.models import Post, Subject
from .serializers import PostSerializer, SubjectSerializer, UserSerializer 
from .permissions import IsAdminUserOrReadOnly, AdminReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
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


