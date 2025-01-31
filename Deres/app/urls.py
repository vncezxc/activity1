from django.urls import path
from .views import  HomePageView, UserListView, UserCreateView, UserUpdateView, UserDeleteView, UserDetailView
from .views import program_list, program_add, program_detail, ProgramUpdateView, ProgramDeleteView, ProgramDetailView, exercise_list, exercise_create, exercise_update, exercise_delete
from .views import exercise_detail, split_exercise_list, split_exercise_detail, split_exercise_create, split_exercise_update, split_exercise_delete, split_list, split_detail, split_create, split_update, split_delete

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
    path('program/<int:pk>', program_detail , name='program_detail'),
    path('program/<int:pk>/edit/', ProgramUpdateView.as_view() , name='program_update'),
    path('program/<int:pk>/delete/', ProgramDeleteView.as_view() , name='program_delete'),
    path('exercises/', exercise_list, name='exercise_list'),
    path('exercises/<int:pk>/', exercise_detail, name='exercise_detail'),
    path('exercises/new/', exercise_create, name='exercise_create'),
    path('exercises/<int:pk>/edit/', exercise_update, name='exercise_update'),
    path('exercises/<int:pk>/delete/', exercise_delete, name='exercise_delete'),
    path('split-exercises/', split_exercise_list, name='split_exercise_list'),
    path('split-exercises/<int:pk>/', split_exercise_detail, name='split_exercise_detail'),
    path('split-exercises/new/', split_exercise_create, name='split_exercise_create'),
    path('split-exercises/<int:pk>/edit/', split_exercise_update, name='split_exercise_update'),
    path('split-exercises/<int:pk>/delete/', split_exercise_delete, name='split_exercise_delete'),
    path('splits/', split_list, name='split_list'),
    path('split/<int:pk>/', split_detail, name='split_detail'),
    path('split/new/', split_create, name='split_create'),
    path('split/<int:pk>/edit/', split_update, name='split_update'),
    path('split/<int:pk>/delete/', split_delete, name='split_delete'),
]

