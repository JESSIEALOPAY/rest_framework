from django.urls import path
from . import views as api_views

urlpatterns = [
    path('news/',api_views.NewsListCreateAPIView.as_view(), name= "news"),
    path('reporter/',api_views.ReporterListCreateAPIView.as_view(), name="repoters"),
    path('news/<int:id>',api_views.NewsDetailAPIView.as_view(), name="detail"),
]




# urlpatterns = [
#     path('news/',api_views.news_list_create_api_view),
#     path('news/<int:id>',api_views.news_detail_api_view),
# ]