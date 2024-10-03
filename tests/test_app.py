import pytest
from datetime import datetime
from app import create_app, db
from models import Expenses


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


@pytest.fixture
def sample_expense(client):
    expense = Expenses(name="Test Expense", amount=100.0, date=datetime.utcnow(), explanation="Test explanation")
    db.session.add(expense)
    db.session.commit()
    return expense


def test_dashboard(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Dashboard" in response.data


def test_new_transaction(client):
    response = client.get('/transaction_form')
    assert response.status_code == 200
    assert b"New Expense" in response.data


def test_add_transaction(client):
    data = {
        'title': 'New Expense',
        'amount': '50.0',
        'date': '2023-01-01',
        'explanation': 'Test explanation'
    }
    response = client.post('/add_transaction', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"New Expense" in response.data


def test_transaction_record(client, sample_expense):
    response = client.get('/transaction_record')
    assert response.status_code == 200
    assert sample_expense.name.encode() in response.data


def test_update_transaction(client, sample_expense):
    data = {
        'id': sample_expense.id,
        'title': 'Updated Expense',
        'amount': '150.0',
        'date': '2023-02-01',
        'explanation': 'Updated explanation'
    }
    response = client.post('/update', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Updated Expense" in response.data


def test_expense_model():
    expense = Expenses(name="Test", amount=100.0, date=datetime.utcnow(), explanation="Test")
    assert expense.name == "Test"
    assert expense.amount == 100.0
    assert isinstance(expense.date, datetime)
    assert expense.explanation == "Test"