from app import Expenses, app, db

with app.app_context():

    # Query all records from the model (table)
    records = Expenses.query.all()
    if not records:
        print("No records found")
        print(Expenses.query.count())