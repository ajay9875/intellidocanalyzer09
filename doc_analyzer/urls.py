# doc_analyzer/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # Import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # Add this line to serve the main HTML file
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]