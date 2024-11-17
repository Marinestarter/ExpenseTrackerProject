from django.urls import path
from . import views

urlpatterns = [
    path('efv', views.ExpenseFormView, name='new_expense_url'),
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_id>', views.updateView, name= 'update_url'),
    path('del/<int:f_id>', views.deleteView, name= 'delete_url'),
]