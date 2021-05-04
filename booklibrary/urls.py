from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('list/', views.BookListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.BookDetailView.as_view(), name='detail'),
]