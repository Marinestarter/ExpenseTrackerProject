import uuid
from django.db import models
from django.utils import timezone

class Expense(models.Model):
    """
    Expense model for tracking financial transactions
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    explanation = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date']
        db_table = 'expense_app_expense'

    def __str__(self):
        return f"{self.name} - ${self.amount}"