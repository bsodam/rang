from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('list/all/', views.ListView.as_view(), name='list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('search_results/', views.SearchResultListView.as_view(), name='search_results'),
    path('create/', views.CreateView.as_view(), name='create'),

]