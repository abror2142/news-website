from django.urls import path

from .views import create_post, writer_posts, writer_waiting_list


urlpatterns = [
    path('writer-create-post/', create_post, name='writer_create_post'),
    path('writer-posts/', writer_posts, name='writer_posts'),
    path('writer-waiting-list/', writer_waiting_list, name='writer_waiting_list'),
]
