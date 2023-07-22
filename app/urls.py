from django.urls import path ,include
from .views import *

urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('about/',about,name='about'),
    path('dashboard/',dashboard,name='dashboard'),
    path('signup/',user_signup,name='signup'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('add-post/',add_post,name='add-post'),
    path('update-post/<int:id>/',update_post,name='update-post'),
    path('delete-post/<int:id>/',delete_post,name='delete-post'),
]