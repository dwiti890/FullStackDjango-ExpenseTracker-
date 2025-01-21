from django.shortcuts import render

# # Create your views here.
def home(request):
    return render(request, 'users/home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense,RecurringExpense
from django.contrib import messages
from django.http import HttpResponse
from .models import recurringexpense

@login_required
def add_expense(request):
    if request.method == 'POST':
        date = request.POST['date']
        label = request.POST['label']
        amount = request.POST['amount']

        # Save expense for the logged-in user
        expense = Expense(user=request.user, date=date, label=label, amount=amount)
        expense.save()

        messages.success(request, 'Expense added successfully!')
        return redirect('add_expense')

    return render(request, 'users/add_expense.html')

@login_required
def list_expenses(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'list_expenses.html', {'expenses': expenses})

def profile(request):

    return render(request, 'users/profile.html')



# def transaction(request):
#     return render(request, 'users/transaction.html')

def expensesummary(request):
    return render(request, 'users/expensesummary.html')

def spendingalert(request):
    return render(request, 'users/spendingalert.html')





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import RecurringExpense  # Ensure the updated model name is used

@login_required
def add_recurring_expense(request):  # Updated function name
    if request.method == 'POST':
        # Get data from the POST request
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        frequency = request.POST.get('frequency')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Validate the data (basic validation)
        if not category or not amount or not frequency or not start_date:
            return HttpResponse("All fields except 'End Date' are required.", status=400)

        try:
            # Save the new recurring expense with the logged-in user
            RecurringExpense = RecurringExpense.objects.create(  # Use the correct model name
                user=request.user,
                category=category,
                amount=amount,
                frequency=frequency,
                start_date=start_date,
                end_date=end_date if end_date else None
            )
            return redirect('recurring_expenses_list')  # Redirect to the list of recurring expenses
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}", status=500)

    return render(request, 'users/add_recurring_expense.html')  # Make sure this template exists


@login_required
def recurring_expenses_list(request):
    # Fetch all recurring expenses for the logged-in user
    recurring_expenses = RecurringExpense.objects.filter(user=request.user)
    return render(request, 'users/recurring_expenses_list.html', {'recurring_expenses': recurring_expenses})
