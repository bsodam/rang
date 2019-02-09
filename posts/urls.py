from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('list/all/', views.ListView.as_view(), name='list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('search_results/', views.SearchResultListView.as_view(), name='search_results'),
    path('create/', views.post_new, name='create'),
    path('<int:pk>/edit/', views.post_edit, name='edit'),
    path('<int:pk>/remove/', views.post_remove, name='remove'),
    path('<int:pk>/comment/', views.comment_add, name='comment'),
    path('<int:pk>/comment/<int:pk_comment>', views.comment_remove, name='comment_remove'),
]