from django.urls import path
from . import views

urlpatterns = [
    path('sv/', views.showView, name='show_url'),
    path('expense/', views.ExpenseFormView, name='new_expense_url'),
    path('expense/<int:f_id>/', views.updateView, name='update_url'),
    path('del/<int:f_id>', views.deleteView, name='delete_url'),
]
