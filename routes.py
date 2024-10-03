from datetime import datetime
import flask
from models import Expenses
from flask import Flask, request, redirect, url_for, flash, Blueprint
from app import db

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def dashboard():
    return flask.render_template('dashboard.html')

@main.route('/transaction_record')
def transaction_record():
    page = request.args.get('page', 1, type=int)
    expenses = Expenses.query.order_by(Expenses.date.desc()).paginate(page=page, per_page=10)
    return flask.render_template('transaction_list.html', expenses=expenses)


@main.route('/transaction_form')
def new_transaction():
    return flask.render_template('transaction_form.html')


@main.route('/add_transaction', methods=['POST'])
def add_expense():
    name = request.form['title']
    amount = request.form['amount']
    date_str = request.form['date']
    explanation = request.form.get('explanation', '')
    date = datetime.strptime(date_str, '%Y-%m-%d').date()

    new_expense = Expenses(name=name, amount=amount, date=date, explanation=explanation)
    db.session.add(new_expense)
    db.session.commit()

    return redirect(url_for('main.transaction_record'))

@main.route('/update', methods=['POST'])
def update():
    temp_data = Expenses.query.get(request.form.get('id'))
    temp_data.name = request.form['title']
    temp_data.amount = float(request.form['amount'])
    datestr = request.form['date']
    temp_data.date = datetime.strptime(datestr, '%Y-%m-%d').date()

    temp_data.explanation = request.form['explanation']

    db.session.commit()
    flash("Transaction successfully updated!")
    return redirect(url_for('main.transaction_record'))