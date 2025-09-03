# core/urls.py
from django.urls import path
from .views import DocumentUploadView, QueryView, RecentDocumentsView

urlpatterns = [
    path('api/documents/', RecentDocumentsView.as_view(), name='recent-documents'),
    path('api/upload/', DocumentUploadView.as_view(), name='document-upload'),
    path('api/query/', QueryView.as_view(), name='query'),
]