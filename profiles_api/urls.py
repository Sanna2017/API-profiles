from django.urls import path, include
from . import views

#########################   VIEW SETS   ###############################
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet) 
#do not need basename as you have queryset; queryset  (see VIEWS.PY) will find it out 
#you could have basename only if you want to overwrite queryset
router.register('feed', views.UserProfileFeedViewSet)

#########################   API VIEWS   ###############################
urlpatterns = [
    path('', include(router.urls)),
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
]