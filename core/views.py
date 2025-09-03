# core/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import services

class RecentDocumentsView(APIView):
    """View to get the list of recently uploaded documents for the current user."""
    def get(self, request, *args, **kwargs):
        if not request.session.session_key:
            request.session.create()
        session_id = request.session.session_key
        
        documents = services.get_recent_documents(session_id)
        return Response(documents)

class DocumentUploadView(APIView):
    """View to upload a document for the current user."""
    def post(self, request, *args, **kwargs):
        if not request.session.session_key:
            request.session.create()
        session_id = request.session.session_key
        
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        doc_id, file_name = services.process_document(file, session_id)
        
        if doc_id:
            return Response({'document_id': doc_id, 'file_name': file_name}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Failed to process document. The file might be empty or in an unsupported format.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class QueryView(APIView):
    """View to ask a question about a document for the current user."""
    def post(self, request, *args, **kwargs):
        if not request.session.session_key:
            return Response({'error': 'Session not found. Please refresh the page.'}, status=status.HTTP_400_BAD_REQUEST)
        session_id = request.session.session_key
        
        document_id = request.data.get('document_id')
        question = request.data.get('question')

        if not document_id or not question:
            return Response({'error': 'Document ID and question are required.'}, status=status.HTTP_400_BAD_REQUEST)

        answer = services.query_document(document_id, question, session_id)
        
        return Response({'answer': answer})