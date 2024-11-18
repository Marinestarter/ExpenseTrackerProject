from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ExpenseForm
from .models import Expense


def ExpenseFormView(request):
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'expense_app/expense.html'
    context = {'form': form}
    return render(request, template_name, context)


def showView(request):
    expenses = Expense.objects.all()
    template_name = 'expense_app/show.html'
    context = {'obj': expenses}
    return render(request, template_name, context)


def updateView(request, f_id):
    obj = Expense.objects.get(id=f_id)
    form = ExpenseForm(instance=obj)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'expense_app/expense.html'
    context = {'form': form}
    return render(request, template_name, context)


def deleteView(request, f_id):
    obj = Expense.objects.get(id=f_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'expense_app/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)
