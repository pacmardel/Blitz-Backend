# Blitz-Backend

This is the backend for Blitz, a professional networking platform for developers. It is built with Django and Django REST Framework, and it provides a RESTful API for managing developer profiles, skills, projects, connections, messages, and endorsements.

## Features

*   **User Authentication:** JWT-based authentication for secure access to the API.
*   **Developer Profiles:** Create and manage developer profiles with information such as bio, experience, and social links.
*   **Skills:** Add and manage skills with different proficiency levels.
*   **Projects:** Showcase projects with descriptions, URLs, and technologies.
*   **Connections:** Connect with other developers and manage your network.
*   **Messaging:** Send and receive private messages with other users.
*   **Endorsements:** Endorse other developers for their skills.
*   **API Documentation:** Interactive API documentation with Swagger UI and ReDoc.
*   **Deployment Ready:** Includes a `render.yaml` file for easy deployment on Render.

## Technologies Used

*   **Python:** The primary programming language for the backend.
*   **Django:** A high-level Python web framework for rapid development.
*   **Django REST Framework:** A powerful and flexible toolkit for building Web APIs.
*   **djangorestframework-simplejwt:** A JSON Web Token authentication plugin for Django REST Framework.
*   **drf-yasg:** A Swagger generation tool for Django REST Framework.
*   **PostgreSQL:** The database used for production (via Render).
*   **Gunicorn:** A Python WSGI HTTP server for UNIX.
*   **Render:** A unified cloud to build and run all your apps and websites.

## Installation and Setup

To get the project running locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Blitz-Backend.git
    cd Blitz-Backend
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

4.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints and Authentication

The API is documented using Swagger UI and ReDoc. You can access the documentation at the following endpoints:

*   **Swagger UI:** `/swagger/`
*   **ReDoc:** `/redoc/`

### Authentication

To access the protected endpoints, you need to obtain a JWT token by sending a POST request to the `/api/token/` endpoint with your username and password. You will receive an access token and a refresh token.

Include the access token in the `Authorization` header of your requests as a bearer token:

```
Authorization: Bearer <your-access-token>
```

When the access token expires, you can obtain a new one by sending a POST request to the `/api/token/refresh/` endpoint with your refresh token.

### Endpoints

The following API endpoints are available:

*   `/api/profiles/`
*   `/api/skills/`
*   `/api/projects/`
*   `/api/connections/`
*   `/api/messages/`
*   `/api/endorsements/`

## Deployment

This project is configured for deployment on Render. You can deploy it by creating a new web service on Render and connecting it to your GitHub repository. Render will automatically detect the `render.yaml` file and configure the services.

The `render.yaml` file defines a web service and a PostgreSQL database. The `build.sh` script installs the dependencies and runs the database migrations. The start command `gunicorn backend.wsgi:application` starts the application.
