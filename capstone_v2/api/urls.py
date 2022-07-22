from django.urls import path 
from rest_framework.routers import DefaultRouter 

from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('subjects', views.SubjectViewSet, basename='subjects')

urlpatterns = router.urls + [ 
    path('currentuser/', views.CurrentUserView.as_view())
]
