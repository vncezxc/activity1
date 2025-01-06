from django.urls import path
from .views import  HomePageView, UserListView, UserCreateView, UserUpdateView, UserDeleteView, UserDetailView
from .views import program_list, program_add, program_detail, ProgramUpdateView, ProgramDeleteView, ProgramDetailView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    # User URLs
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('program/', program_list , name='program_list'),
    path('program/add/', program_add , name='program_add'),
    path('program/<int:pk>', ProgramDetailView.as_view() , name='program_detail'),
    path('program/<int:pk>/edit/', ProgramUpdateView.as_view() , name='program_update'),
    path('program/<int:pk>/delete/', ProgramDeleteView.as_view() , name='program_delete'),
]

