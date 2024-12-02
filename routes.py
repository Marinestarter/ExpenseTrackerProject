from datetime import datetime
import flask
from models import Expenses, Category
from flask import Flask, request, redirect, url_for, flash, Blueprint, render_template
from app import db


main = Blueprint('main', __name__)

from datetime import datetime, timedelta
from sqlalchemy import func


@main.route('/')
def dashboard():
    # Calculate total expenses
    total_expenses = db.session.query(func.sum(Expenses.amount)).scalar() or 0

    # Calculate current month expenses
    current_month = datetime.utcnow().replace(day=1)
    current_month_expenses = db.session.query(func.sum(Expenses.amount)) \
                                 .filter(Expenses.date >= current_month).scalar() or 0

    # Calculate daily average (last 30 days)
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    recent_total = db.session.query(func.sum(Expenses.amount)) \
                       .filter(Expenses.date >= thirty_days_ago).scalar() or 0
    daily_average = recent_total / 30

    # Get recent transactions
    recent_expenses = Expenses.query \
        .order_by(Expenses.date.desc()) \
        .limit(5) \
        .all()

    # Get total expenses by category
    category_totals = db.session.query(
        Category.name,
        func.sum(Expenses.amount).label('total')
    ).join(Expenses) \
        .group_by(Category.name) \
        .all()

    # Get monthly comparison (last 6 months)
    monthly_comparison = []
    for i in range(5    , -1, -1):
        month_start = datetime.utcnow().replace(day=1) - timedelta(days=i * 30)
        month_end = (month_start + timedelta(days=32)).replace(day=1)

        month_total = db.session.query(func.sum(Expenses.amount)) \
                          .filter(Expenses.date >= month_start) \
                          .filter(Expenses.date < month_end) \
                          .scalar() or 0

        # Calculate change percentage
        if i < 5:  # Skip first month as we can't calculate change
            prev_month = monthly_comparison[-1]['total']
            if prev_month > 0:
                change = ((month_total - prev_month) / prev_month) * 100
            else:
                change = 0
        else:
            change = 0

        monthly_comparison.append({
            'month': month_start.strftime('%b'),
            'total': month_total,
            'change': change
        })

    return render_template('dashboard.html',
                           total_expenses=total_expenses,
                           current_month_expenses=current_month_expenses,
                           daily_average=daily_average,
                           recent_expenses=recent_expenses,
                           category_totals=category_totals,
                           monthly_comparison=monthly_comparison)


@main.route('/transaction_record')
def transaction_record():
    page = request.args.get('page', 1, type=int)
    expenses = Expenses.query.order_by(Expenses.date.desc()).paginate(page=page, per_page=10)
    categories = Category.query.all()  # Get all categories
    return flask.render_template('transaction_list.html', expenses=expenses, categories=categories)


@main.route('/transaction_form')
def new_transaction():
    categories = Category.query.all()
    date= datetime.date
    return flask.render_template('transaction_form.html', categories=categories)


@main.route('/add_transaction', methods=['POST'])
def add_expense():
    try:
        name = request.form['title']
        amount = float(request.form['amount'])
        date_str = request.form['date']
        explanation = request.form.get('explanation', '')
        category_id = request.form.get('category_id')

        date = datetime.strptime(date_str, '%Y-%m-%d').date()


        new_expense = Expenses(
            name=name,
            amount=amount,
            date=date,
            explanation=explanation,
            category_id=category_id if category_id else None
        )

        db.session.add(new_expense)
        db.session.commit()
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
    return redirect(url_for('main.transaction_record'))


@main.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    expense = Expenses.query.get_or_404(id)
    try:
        db.session.delete(expense)
        db.session.commit()
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
    except Exception as e:
        flash('Error adding category!', 'danger')

    return redirect(url_for('main.categories'))


@main.route('/delete_category/<int:id>', methods=['POST'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    try:
        db.session.delete(category)
        db.session.commit()
    except Exception as e:
        flash('Error deleting category!', 'danger')

    return redirect(url_for('main.categories'))