# 👨‍👩‍👧 Parents Information API

A beginner-friendly RESTful API built with **FastAPI** and **Python** that demonstrates the four core HTTP methods — `GET`, `POST`, `PUT`, and `DELETE` — using a Parents Information management system as a practical use case.

---

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
  - [GET — Retrieve by ID](#1-get--retrieve-parent-by-id)
  - [GET — Search by Name](#2-get--search-parent-by-name)
  - [POST — Create a Parent](#3-post--create-a-parent)
  - [PUT — Update a Parent](#4-put--update-a-parent)
  - [DELETE — Delete a Parent](#5-delete--delete-a-parent)
- [Data Models](#data-models)
- [Sample Data](#sample-data)
- [HTTP Methods Explained](#http-methods-explained)
- [License](#license)

---

## Overview

This project is a learning-focused REST API that models a simple **Parents Information Management System**. It is designed to teach and demonstrate how each HTTP method works in a real-world API context using [FastAPI](https://fastapi.tiangolo.com/) — one of the fastest and most modern Python web frameworks available.

The API stores parent records in an in-memory Python dictionary (no database required), making it lightweight and easy to run locally without any setup complexity.

---

## Features

- Retrieve a parent's information using their unique numeric ID
- Search for a parent by name using a query parameter
- Create new parent records via HTTP POST
- Update existing parent records (partial updates supported)
- Delete parent records permanently
- Auto-generated interactive API documentation (Swagger UI & ReDoc)
- Input validation via Pydantic models
- Path parameter constraints (IDs must be between 100 and 200)

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| [Python 3.8+](https://www.python.org/) | Core programming language |
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework for building APIs |
| [Pydantic](https://docs.pydantic.dev/) | Data validation and schema definition |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server to run the FastAPI app |

---

## Project Structure

```
parents-api/
│
├── main.py           # Main application file containing all routes and logic
└── README.md         # Project documentation (this file)
```

---

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/parents-api.git
cd parents-api
```

2. **Create and activate a virtual environment (recommended):**

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install the required dependencies:**

```bash
pip install fastapi uvicorn
```

### Running the Server

Start the development server with:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables hot-reloading so the server automatically restarts when you make code changes.

Once running, open your browser and visit:

| Interface | URL |
|-----------|-----|
| Swagger UI (Interactive Docs) | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) |
| ReDoc (Alternative Docs) | [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) |
| Base API URL | [http://127.0.0.1:8000](http://127.0.0.1:8000) |

---

## API Endpoints

### 1. `GET` — Retrieve Parent by ID

**Endpoint:** `GET /get-parents/{parents_id}`

Fetches the full information of a parent using their unique numeric ID.

**Path Parameter:**

| Parameter | Type | Required | Constraint | Description |
|-----------|------|----------|------------|-------------|
| `parents_id` | `int` | Yes | `100 < id < 200` | The unique ID of the parent |

**Example Request:**

```http
GET /get-parents/101
```

**Success Response (`200 OK`):**

```json
{
  "name": "Garuba Abdulhammed Olohuntoyin",
  "gender": "male",
  "age": 50,
  "Relationship": "Father"
}
```

**Error Response (ID not found):**

```json
{
  "Error": "Parent does not Exists"
}
```

---

### 2. `GET` — Search Parent by Name

**Endpoint:** `GET /get-by-name`

Searches for a parent record using a name query parameter. The search is **case-insensitive** and supports partial name matching.

**Query Parameter:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | `str` | No | Full or partial name to search for |

**Example Request:**

```http
GET /get-by-name?name=omowunmi
```

**Success Response (`200 OK`):**

```json
{
  "name": "Abdulhammed Omowunmi Lateefat",
  "gender": "female",
  "age": 45,
  "relationship": "Mother"
}
```

**Not Found Response:**

```json
{
  "Data": "Not found"
}
```

---

### 3. `POST` — Create a Parent

**Endpoint:** `POST /create-parents/{parent_id}`

Creates a new parent record with the given ID. If a parent with that ID already exists, an error is returned.

**Path Parameter:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `parent_id` | `int` | Yes | The unique ID to assign to the new parent |

**Request Body:**

```json
{
  "name": "John Doe",
  "gender": "male",
  "age": 55,
  "relationship": "Father"
}
```

**Success Response (`200 OK`):**

```json
{
  "name": "John Doe",
  "gender": "male",
  "age": 55,
  "relationship": "Father"
}
```

**Error Response (ID already exists):**

```json
{
  "Error": "Parent exists"
}
```

---

### 4. `PUT` — Update a Parent

**Endpoint:** `PUT /update-parent/{parent_id}`

Updates one or more fields of an existing parent record. Only the fields included in the request body will be updated — all other fields remain unchanged (partial update).

**Path Parameter:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `parent_id` | `int` | Yes | The unique ID of the parent to update |

**Request Body (all fields optional):**

```json
{
  "age": 52
}
```

**Success Response (`200 OK`):**

```json
{
  "name": "Garuba Abdulhammed Olohuntoyin",
  "gender": "male",
  "age": 52,
  "Relationship": "Father"
}
```

**Error Response (ID not found):**

```json
{
  "Error": "Parent does not Exists"
}
```

---

### 5. `DELETE` — Delete a Parent

**Endpoint:** `DELETE /delete-parent/{parent_id}`

Permanently removes a parent record from the in-memory store by their ID.

**Path Parameter:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `parent_id` | `int` | Yes | The unique ID of the parent to delete |

**Example Request:**

```http
DELETE /delete-parent/103
```

**Success Response (`200 OK`):**

```json
{
  "Message": "Deleted Successfully"
}
```

**Error Response (ID not found):**

```json
{
  "Error": "Parent does not Exits"
}
```

---

## Data Models

### `Parents` — Used for Creating Records

Defines the required fields when creating a new parent entry.

```python
class Parents(BaseModel):
    name: str
    gender: str
    age: int
    relationship: str
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `str` | Yes | Full name of the parent |
| `gender` | `str` | Yes | Gender of the parent (e.g., `"male"`, `"female"`) |
| `age` | `int` | Yes | Age of the parent |
| `relationship` | `str` | Yes | Relationship type (e.g., `"Father"`, `"Mother"`) |

---

### `UpdateParent` — Used for Partial Updates

All fields are optional, allowing partial record updates without affecting unchanged fields.

```python
class UpdateParent(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    relationship: Optional[str] = None
```

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `name` | `str` | No | `None` | Updated name |
| `gender` | `str` | No | `None` | Updated gender |
| `age` | `int` | No | `None` | Updated age |
| `relationship` | `str` | No | `None` | Updated relationship type |

---

## Sample Data

The application is pre-loaded with three parent records for testing:

| ID | Name | Gender | Age | Relationship |
|----|------|--------|-----|--------------|
| 101 | Garuba Abdulhammed Olohuntoyin | Male | 50 | Father |
| 102 | Abdulhammed Omowunmi Lateefat | Female | 45 | Mother |
| 103 | Yusuf Ganiyat Romoke | Female | 40 | Mother |

> **Note:** This data is stored in-memory and resets every time the server restarts. No data is persisted to a file or database.

---

## HTTP Methods Explained

This project is built to demonstrate the four fundamental HTTP methods used in REST APIs:

| Method | Endpoint Pattern | Real-World Analogy |
|--------|------------------|--------------------|
| `GET` | `/get-parents/{id}`, `/get-by-name` | A user logging into a website — their data is fetched and verified |
| `POST` | `/create-parents/{id}` | A user signing up and creating a new account |
| `PUT` | `/update-parent/{id}` | A user changing their username or profile details |
| `DELETE` | `/delete-parent/{id}` | A user permanently deleting their account |

---


## License

This project is open-source and available under the [MIT License](LICENSE).

---

> Built with ❤️ using [FastAPI](https://fastapi.tiangolo.com/) — a modern, fast, and production-ready Python web framework.
