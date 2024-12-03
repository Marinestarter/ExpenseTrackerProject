# Expense Tracker

An easy-to-use expense tracking application that allows users to log, manage, and categorize their financial transactions. The project features secure user authentication, expense categorization, and dynamic dashboards to provide insights into spending habits.

---

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)

---

## Features

### **User Authentication**
- **Login and Registration**:
  - Users can create an account with a unique username and email.
  - Passwords are hashed securely using `werkzeug.security`.
- **Session Management**:
  - Users remain logged in until they manually log out.
  - Unauthorized users are redirected to the login page.

### **Expense Management**
- **CRUD Functionality**:
  - Users can create, view, update, and delete expenses.
- **Expense Details**:
  - Each expense includes:
    - Name
    - Amount
    - Date of the transaction
    - Explanation
    - Optional category assignment
- **Recent Transactions**:
  - Displays the latest transactions in a user-friendly list.
- **Monthly Comparison**:
  - Compare expenses over the last six months with percentage changes.
- **Daily Average**:
  - Calculates the average daily spending over the past 30 days.

### **Category Management**
- **Add/Edit/Delete Categories**:
  - Users can manage categories to organize their expenses.
  - Categories include a name and an optional description.
- **Category Totals**:
  - Dynamically calculates total spending per category.

### **Dashboard Analytics**
- **Visual Summaries**:
  - Displays total expenses, current month's expenses, and category breakdowns.
- **Time-Based Insights**:
  - View spending trends for the last 6 months.

---

## Technologies Used

### Backend
- **Flask**: Manages server-side functionality and routing.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Lightweight and reliable database for storing user data.

### Frontend
- **Bootstrap 5.3**: Responsive and modern interface design.

---

## Installation

### Prerequisites
- Python 3.8+ installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Marinestarter/ExpenseTrackerProject.git
   ```
