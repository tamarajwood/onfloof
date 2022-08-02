from django.urls import path 
from rest_framework.routers import DefaultRouter 

from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('subjects', views.SubjectViewSet, basename='subjects')
router.register('comments', views.CommentViewSet, basename='comments')
router.register('breeds', views.BreedViewSet, basename='breeds')
router.register('activities', views.ActivityViewSet, basename='activities')

urlpatterns = router.urls + [ 
    path('currentuser/', views.CurrentUserView.as_view())
]
