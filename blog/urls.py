from django.urls import path
from blog import views
from blog.views import post_list

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]
