# core/urls.py
from django.urls import path
from .views import DocumentUploadView, QueryView, RecentDocumentsView
from . import views
urlpatterns = [
    path('api/documents/', RecentDocumentsView.as_view(), name='recent-documents'),
    path('api/upload/', DocumentUploadView.as_view(), name='document-upload'),
    path('api/query/', QueryView.as_view(), name='query'),
    path('clear-session/', views.clear_all_session_data, name='clear_session'),
    path('api/delete-all-documents/', views.delete_all_documents, name='delete_all_documents'),
]
