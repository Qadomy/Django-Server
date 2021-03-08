from django.urls import path

from boards import views

urlpatterns = [
    path('', views.BoarListView.as_view(), name='home'),
    path('boards/<int:board_id>/', views.board_topics, name='board_topics'),
    path('boards/<int:board_id>/new', views.new_topic, name='new_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>', views.topic_posts, name='topic_posts'),
    path('boards/<int:board_id>/topics/<int:topic_id>/replay/', views.replay_topic, name='replay_topic'),

    path('boards/<int:board_id>/topics/<int:topic_id>/posts/<int:post_id>/edit/',
         views.PostUpdateView.as_view(), name='edit_posts'),
]
