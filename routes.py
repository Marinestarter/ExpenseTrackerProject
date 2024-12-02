from datetime import datetime
import flask
from models import Expenses, Category
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
    categories = Category.query.all()  # Get all categories
    return flask.render_template('transaction_list.html', expenses=expenses, categories=categories)


@main.route('/transaction_form')
def new_transaction():
    categories = Category.query.all()
    return flask.render_template('transaction_form.html', categories=categories)


@main.route('/add_transaction', methods=['POST'])
def add_expense():
    try:
        name = request.form['title']
        amount = float(request.form['amount'])  # Convert amount to float
        date_str = request.form['date']
        explanation = request.form.get('explanation', '')
        category_id = request.form.get('category_id')  # Get category_id from form

        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        # Create new expense with proper category relationship
        new_expense = Expenses(
            name=name,
            amount=amount,
            date=date,
            explanation=explanation,
            category_id=category_id if category_id else None  # Only set category_id if it exists
        )

        db.session.add(new_expense)
        db.session.commit()
        flash('Transaction added successfully!', 'success')
    except ValueError as e:
        flash('Invalid input: Please check the amount and date format', 'danger')
        return redirect(url_for('main.new_transaction'))
    except Exception as e:
        flash('Error adding transaction', 'danger')
        return redirect(url_for('main.new_transaction'))

    return redirect('/transaction_record')

@main.route('/update', methods=['POST'])
def update():
    expense = Expenses.query.get_or_404(request.form.get('id'))
    expense.name = request.form['title']
    expense.amount = float(request.form['amount'])
    expense.category = request.form['category.id']
    expense.date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
    expense.explanation = request.form['explanation']

    db.session.commit()
    flash("Transaction updated successfully!", "success")

    return redirect(url_for('main.transaction_record'))


@main.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    expense = Expenses.query.get_or_404(id)
    try:
        db.session.delete(expense)
        db.session.commit()
        flash("Transaction deleted successfully!", "success")
    except Exception as e:
        flash("Error deleting transaction!", "danger")

    return redirect(url_for('main.transaction_record'))


@main.route('/categories')
def categories():
    categories = Category.query.all()
    return flask.render_template('categories.html', categories=categories)


@main.route('/add_category', methods=['POST'])
def add_category():
    name = request.form['name']
    description = request.form.get('description', '')

    try:
        category = Category(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        flash('Category added successfully!', 'success')
    except Exception as e:
        flash('Error adding category!', 'danger')

    return redirect(url_for('main.categories'))


@main.route('/delete_category/<int:id>', methods=['POST'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    try:
        db.session.delete(category)
        db.session.commit()
        flash('Category deleted successfully!', 'success')
    except Exception as e:
        flash('Error deleting category!', 'danger')

    return redirect(url_for('main.categories'))