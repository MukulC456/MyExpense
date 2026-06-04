# MyExpense- AI-Powered Expense Tracker

An intelligent full-stack expense tracking application built using Python, FastAPI, PostgreSQL, HTML, CSS, JavaScript, and Machine Learning.

The application helps users manage their personal finances, track spending habits, analyze expenses, and receive AI-powered financial insights.


##  Features

### Authentication

* User Registration
* User Login
* JWT Authentication
* Password Hashing with bcrypt

### Expense Management

* Add Expenses
* Edit Expenses
* Delete Expenses
* View Expense History
* Categorize Expenses

### Analytics Dashboard

* Monthly Spending Reports
* Category-wise Expense Breakdown
* Spending Trends
* Top Spending Categories

### Machine Learning Features

* Automatic Expense Category Prediction
* Monthly Expense Forecasting
* Overspending Detection
* Personalized Spending Insights


##  Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT Authentication

### Frontend

* HTML5
* CSS3
* JavaScript

### Machine Learning

* Pandas
* NumPy
* Scikit-learn
* Matplotlib

### Deployment

* Backend: Render/Railway
* Frontend: Vercel


##  Run Application

1. Run the command in backend file path:
uvicorn app.main:app --reload


2. API Documentation:
http://localhost:8000/docs


Swagger UI will be available automatically.


##  Machine Learning Modules

### Expense Categorization

Predicts expense category from transaction description.

Example:

Input:
Uber ride to airport

Output:
Travel

Algorithms:

* Logistic Regression
* Naive Bayes


### Expense Forecasting

Predicts future spending trends.

Algorithms:

* Linear Regression
* Random Forest Regressor


### Anomaly Detection

Detects unusual spending behavior.

Algorithms:

* Isolation Forest
* Z-Score Analysis


##  Security

* JWT Authentication
* Password Hashing
* Protected API Routes
* Environment Variable Configuration
* SQL Injection Protection through ORM


##  Future Improvements

* Receipt OCR
* Multi-Currency Support
* Budget Planning
* Email Reports
* Mobile App
* AI Financial Assistant
* Real-time Notifications
* Savings Recommendations


##  Learning Objectives

This project demonstrates:

* Backend Development with FastAPI
* Database Design with PostgreSQL
* REST API Development
* Authentication and Authorization
* CRUD Operations
* Machine Learning Integration
* Data Analysis and Visualization
* Full-Stack Application Development
* Deployment and DevOps Fundamentals