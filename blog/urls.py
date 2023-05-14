from django.urls import path
from .views import bloglistviews, blogdeatilview, blog_detail_view, BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list_view'),
    path('<int:pk>/', blog_detail_view, name='blog_detail_view')
]
