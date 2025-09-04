# Intelli-Doc AI 📄🤖

Intelli-Doc AI is an intelligent document analysis tool built as a modern web application. It allows users to upload various documents and engage in a conversational Q&A to quickly extract and understand information, effectively turning any document into an interactive knowledge base.

## Key Features ✨

-   **Conversational Q&A:** Ask questions in natural language and receive AI-generated answers based on the document's content.
-   **Multi-Format Support:** Handles various file types, including PDF, Word, Excel, and PowerPoint.
-   **Personalized Workspaces:** Features secure, session-based support for multiple users, ensuring each person's documents and chats are kept private.
-   **Persistent Chat History:** Remembers your conversation for each document using browser `localStorage`, allowing you to continue your session even after a page refresh.
-   **Intelligent Document Management:** Automatically manages a queue of the 3 most recent documents for each user.

## Technology Stack 🛠️

-   **Backend:** Python, Django, Django REST Framework
-   **AI & NLP:** Google Gemini API, Sentence-Transformers (for embeddings), Faiss (for vector search)
-   **Frontend:** HTML, CSS, Vanilla JavaScript

## Setup and Installation 🚀

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

-   Python 3.8+
-   Git

### 2. Clone the Repository

```bash
git clone <your-repository-url>
cd intelli-doc
```

### 3. Set Up Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies

First, create a `requirements.txt` file from your current environment:
```bash
pip freeze > requirements.txt
```
Then, anyone setting up the project can install the dependencies:
```bash
pip install -r requirements.txt
```

### 5. Environment Variables

Create a `.env` file in the project root (where `manage.py` is located). This file will hold your API key.

```
# .env
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

### 6. Run Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

## How to Use 📖

1.  Open the web application in your browser.
2.  Click "Upload New PDF" to select a document from your computer. Supported formats are `.pdf`, `.docx`, `.xlsx`, and `.pptx`.
3.  The document will appear in the "Recent Documents" list. Click on it to start a chat session.
4.  Type your questions about the document in the input box and press Enter. The AI will provide answers based on the document's content.