# Django_Model_for_chatbot
## Overview
This project is an admin dashboard designed to manage prompt templates, agents, and model configurations for a medicine suggestion chatbot. The chatbot itself runs on **FastAPI** and uses **Gemini/OpenAI LLMs** to generate intelligent, safe responses based on curated medical references. This Django application helps structure and maintain the backend logic and knowledge used by the chatbot.

## Features
- Provides management of medicine-related prompts, models, and agent metadata.
- Uses structured datasets from medical references and pharmaceutical knowledge.
- Built with **Django** for a powerful admin interface and scalable backend.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher  
- pip (Python package installer)  
- A compatible operating system (Windows, macOS, or Linux)  
- MongoDB (for database)

## Installation
Follow these steps to set up the project:

### 1. Clone the repository:
Open your terminal and run the following command:

```bash
https://github.com/Harshitsoni30/Django_Model_for_chatbot.git
```

## 2. Navigate to the project directory:

```bash
cd Chatbot
```

### 3. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

Activate the virtual environment:

- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  venv\Scripts\activate
  ```

### 4. Install the required packages:
Use pip to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 5. Run the database migrations:
```bash
python manage,py makemigrations
python manage.py migrate
```

### 6. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```

### 7. Run the application:
Start the application using the following command:

```bash
python manage.py runserver

```

This will run the application in development mode, and you can access it at:

```
http://127.0.0.1:8001/admin/

```
