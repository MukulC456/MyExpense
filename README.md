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

---

## 🛠 Tech Stack

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

---

## 📂 Project Structure

expense-tracker/

├── backend/

│   ├── app/

│   │   ├── auth/

│   │   ├── database/

│   │   ├── routes/

│   │   ├── schemas/

│   │   ├── services/

│   │   ├── ml/

│   │   └── main.py

│   │

│   ├── requirements.txt

│   └── .env

│

├── frontend/

│   ├── index.html

│   ├── dashboard.html

│   ├── css/

│   └── js/

│

├── dataset/

│

├── docs/

│

└── README.md

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/expense-tracker.git

cd expense-tracker
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🐘 PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE expense_tracker;
```

Configure environment variables:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/expense_tracker

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## ▶️ Run Application

```bash
uvicorn app.main:app --reload
```

API Documentation:

```text
http://localhost:8000/docs
```

Swagger UI will be available automatically.

---

## 📊 Machine Learning Modules

### Expense Categorization

Predicts expense category from transaction description.

Example:

Input:

```text
Uber ride to airport
```

Output:

```text
Travel
```

Algorithms:

* Logistic Regression
* Naive Bayes

---

### Expense Forecasting

Predicts future spending trends.

Algorithms:

* Linear Regression
* Random Forest Regressor

---

### Anomaly Detection

Detects unusual spending behavior.

Algorithms:

* Isolation Forest
* Z-Score Analysis

---

## 🔐 Security

* JWT Authentication
* Password Hashing
* Protected API Routes
* Environment Variable Configuration
* SQL Injection Protection through ORM

---

## 📈 Future Improvements

* Receipt OCR
* Multi-Currency Support
* Budget Planning
* Email Reports
* Mobile App
* AI Financial Assistant
* Real-time Notifications
* Savings Recommendations

---

## 🎯 Learning Objectives

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

---

## 👨‍💻 Author

Built by [Your Name]

Computer Science Graduate | Python Developer | Machine Learning Enthusiast

---

## 📄 License

This project is licensed under the MIT License.
