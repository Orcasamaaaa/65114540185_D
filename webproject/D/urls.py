from django.urls import path,include
from D.views import *
urlpatterns = [
    path('coures',CourseListView.as_view(),name='coureslist'),
    path('edit<str:pk>',CourseEditView.as_view(),name='edit')
]