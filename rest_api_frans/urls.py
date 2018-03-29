from django.urls import path
from . import views


urlpatterns = [
    path('news/create', views.CreateNews.as_view()),
    path('news/list', views.ListNews.as_view()),
    path('news/detail/<int:pk>', views.ViewDetailNews.as_view()),
    path('news/update/<int:pk>', views.UpdateNews.as_view()),
    path('news/delete/<int:pk>', views.DeleteNews.as_view()),
    path('news/filter/status/<str:status>', views.FilterNewsByStatus.as_view()),
    path('news/filter/topic/<int:pk>', views.FilterNewsByTopic.as_view()),

    path('topic/create', views.CreateTopic.as_view()),
    path('topic/list', views.ListTopic.as_view()),
    path('topic/detail/<int:pk>', views.ViewDetailTopic.as_view()),
    path('topic/update/<int:pk>', views.UpdateTopic.as_view()),
    path('topic/delete/<int:pk>', views.DeleteTopic.as_view()),
]