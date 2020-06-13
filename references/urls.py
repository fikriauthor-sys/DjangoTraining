from django.urls import path
from .import views

app_name = 'references'
urlpatterns = [
    path('', views.ReferencesListView.as_view(), name='references_list'),
    path('postref/add/', views.ReferencesCreateView.as_view(), name='references_create'),
    path('postref/<int:pk>-<slug:slug>/update/', views.ReferencesUpdateView.as_view(), name='references_update'),
    path('postref/<int:pk>-<slug:slug>/delete/', views.ReferencesDeleteView.as_view(), name='references_delete')
]