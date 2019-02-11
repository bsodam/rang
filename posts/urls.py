from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    # Post List
    path('list/all/', views.ListView.as_view(), name='list_all'),
    path('list/', views.list_local, name='list_local'),
    path('search_results/', views.SearchResultListView.as_view(), name='search_results'),

    # Post Detail
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/add_heart/', views.add_heart, name='add_heart'),
    path('<int:pk>/add_poop/', views.add_poop, name='add_poop'),
    path('create/', views.post_new, name='create'),
    path('<int:pk>/edit/', views.post_edit, name='edit'),
    path('<int:pk>/remove/', views.post_remove, name='remove'),

    # Comment
    path('<int:pk>/comment/', views.comment_add, name='comment'),
    path('<int:pk>/comment_remove/<int:pk_comment>', views.comment_remove, name='comment_remove'),

    # Comment On Comment
    path('<int:pk>/comment_on_comment/<int:pk_comment>', views.comment_on_comment, name='comment_on_comment'),
    path('<int:pk>/comment_on_comment_remove/<int:pk_comment_on_comment>', views.comment_on_comment_remove, name='comment_on_comment_remove'),
]
