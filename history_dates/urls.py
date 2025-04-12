from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('list', views.event_list, name='event_list'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<int:pk>/', views.edit_event, name='edit_event'),
    path('delete/<int:pk>/', views.delete_event, name='delete_event'),
    path('quiz/', views.quiz, name='quiz'),
    path('timeline_quiz/', views.timeline_quiz, name='timeline_quiz'),
    path('timeline/check/', views.check_timeline_order, name='check_timeline_order'),
]
