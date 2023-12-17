from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.custom_login, name='login'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/add_comment/', views.add_comment_to_post, name='add_comment_to_post'),
]
