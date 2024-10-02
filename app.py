import flask
import models
from flask import Flask, request, redirect, url_for
from datetime import datetime, timezone
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    explanation = db.Column(db.Text, nullable=True)

    def __init__(self, name, amount, date=None, explanation=None):
        self.name = name
        self.amount = amount
        if date is not None:
            self.date = date
        else:
            self.date = datetime.utcnow()  # Default to current time
        self.explanation = explanation


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    return flask.render_template('dashboard.html')

@app.route('/transaction_form')
def new_transaction():
    expenses = Expenses.query.all()
    total_expense = sum(expense.amount for expense in expenses)
    return flask.render_template('transaction_form.html', expenses=expenses, total_expense=total_expense)


@app.route('/add_transaction', methods=['POST'])
def add_transaction_handler():
    name = request.form['title']
    amount = request.form['amount']
    date_str = request.form['date']
    explanation = request.form.get('explanation', '')

    date = datetime.strptime(date_str, '%Y-%m-%d').date()

    new_expense = Expenses(name=name, amount=amount, date=date, explanation=explanation)
    db.session.add(new_expense)
    db.session.commit()

@app.route('/transaction_record')
def transaction_record():
    page = request.args.get('page', 1, type=int)
    expenses = Expenses.query.order_by(Expenses.date.desc()).paginate(page=page, per_page=10)
    return flask.render_template('transaction_list.html', expenses=expenses)

    
if __name__ == '__main__':
    app.run(debug=True)
