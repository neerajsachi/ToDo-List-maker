ToDo Application
Overview

This is a ToDo application built using Django and Django REST Framework. The application allows users to manage their daily tasks and goals by providing CRUD operations for todo items.
Features

    User Authentication: JSON Web Token (JWT) authentication for secure user login.
    CRUD Operations: Users can create, read, update, and delete todos
    API Endpoints: Provides a robust REST API for integration with frontend applications or external services.

Technologies Used

    Backend: Django, Django REST Framework
    Authentication: JWT (via djangorestframework-simplejwt)
    Database: MySQL
    Serialization: Django REST Framework's ModelSerializers

API Endpoints
Authentication

    /api/token/ (POST): Obtain JWT token by sending a username and password.
    /api/token/refresh/ (POST): Refresh an existing JWT token.

Todo API

    /api/todo/ (GET): List all todo items.
    /api/todo/<int:pk>/ (GET): Get a single todo item by its ID.
    /api/todo/enter/ (POST): Create a new todo item.
    /api/todo/update/<int:pk>/ (PUT): Update an existing todo item by its ID.
    /api/todo/delete/<int:pk>/ (DELETE): Delete a todo item by its ID.