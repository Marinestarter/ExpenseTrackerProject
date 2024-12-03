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
2. Create a virtual environment:
   ```bash
   # Windows
    python -m venv venv
    venv\Scripts\activate
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
 4. Initialize the database:
   ```bash
   flask db upgrade
   ```
   5.Start the development server:
   ```bash
   flask run
   ```
   6. The application will be available at http://localhost:5000
  
   ## Usage

  1.   **Register or Login**:
     - Visit the application URL at `http://127.0.0.1:5000/`.
     - If you're a new user, click on the "Register" link to create an account by providing your username, email, and password.
     - If you already have an account, log in using your credentials.

  2. **Access the Dashboard**:
     - After logging in, you'll be directed to the dashboard.
     - The dashboard displays key financial summaries, including:
       - Total expenses
       - Current month’s expenses
       - Spending trends and category breakdowns
       - Recent transactions

  3. **Add a New Expense**:
     - Navigate to the "New Transaction" page.
     - Fill in the form with:
       - **Title**: A brief name for the transaction.
       - **Amount**: The transaction amount.
       - **Date**: The date of the transaction.
       - **Category**: (Optional) Assign the expense to a category.
       - **Explanation**: (Optional) Add additional notes about the transaction.
     - Click "Save" to add the transaction to your record.

  4. **View and Manage Transactions**:
     - Go to the "Transaction Record" page to view all your expenses.
     - Use the pagination controls to navigate through your records.
     - Edit or delete transactions using the corresponding options next to each record.

  5. **Manage Categories**:
     - Navigate to the "Categories" page.
     - Add new categories to organize your expenses.
     - Edit or delete categories as needed.
  
  6. **Analyze Spending**:
     - View category totals and monthly comparisons in the dashboard to analyze your spending habits.
     - Use these insights to plan budgets or track financial goals.
  
  7. **Logout**:
     - Click the "Logout" button to securely end your session.
     - You can log back in anytime to resume tracking your expenses.
