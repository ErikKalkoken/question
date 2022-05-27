from tkinter.messagebox import QUESTION
from unicodedata import name
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('view/<int:pk>/', views.viewQuestion, name='view-Question'),
    path('question/<int:pk>/answer/', views.My_Answer.as_view(), name='answer'),
    path('question/', views.My_Question.as_view(), name='question'),
    path('register/', views.register, name='register'),
    path('feedback/', views.PostFeedBack.as_view(), name='FeedBack'),
    path('login/', views.login, name='login'),
    path('notification/', views.NotificationListView.as_view(), name='notification'),
    path('rules/', views.rules, name='Rules'),
    path('viewAnonymous/<int:pk>/', views.viewAnonymous, name='viewAnonymous'),
]