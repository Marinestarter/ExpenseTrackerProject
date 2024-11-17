from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .forms import ExpenseForm
from .models import Expense

# Create your views here.
def ExpenseFormView(request):
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            expenses = Expense.objects.all()
            # Render the updated list
            expense_list_html = render_to_string(
                'expense_app/partials/expense_list.html',
                {'obj': expenses},
                request=request
            )
            # Add a div that will clear the form area using hx-swap-oob
            response_html = f"""
                {expense_list_html}
                <div id="expense-form"></div>
            """
            return HttpResponse(response_html)
        else:
            # If form is invalid, return the form with errors
            return render(request, 'expense_app/expense.html', {'form': form})

    template_name = 'expense_app/expense.html'
    context = {'form': form}
    return render(request, template_name, context)
def showView(request):
    obj = Expense.objects.all()
    template_name = 'expense_app/show.html'
    context = {'obj': obj}
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
    print(f"Delete view called with id: {f_id}")
    print(f"Request method: {request.method}")
    print(f"Request headers: {request.headers}")
    if request.method == 'DELETE':  # HTMX sends DELETE request

        obj = Expense.objects.get(id=f_id)
        obj.delete()
        return HttpResponse('')  # Empty response as element will be removed