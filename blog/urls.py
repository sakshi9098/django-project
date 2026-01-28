from django.urls import path
from .views import PostListView, qa_view

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('qa/', qa_view, name='qa'),
]
