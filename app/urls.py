from django.urls import path
from .views import  HomePageView, UserListView, UserCreateView, UserUpdateView, UserDeleteView, UserDetailView
from .views import program_list, program_add, program_detail, ProgramUpdateView, ProgramDeleteView, ProgramDetailView
from app import views


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
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('profile',views.profile,name="profile"),
    path('gallery',views.gallery,name="gallery"),
    path('attendance',views.attendance,name="attendance"),

]

