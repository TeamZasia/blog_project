from django.urls import path

from . import views

urlpatterns = [
    path('', views.Bloglistview.as_view(), name='home'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', views.BlogcreateView.as_view(), name='post_new'),
    path('post/edit/<int:pk>/', views.BlogUpdate.as_view(), name='post_edit'),
    path('post/delete/<int:pk>/', views.bloddelte.as_view(), name='post_delete'),
]