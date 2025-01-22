from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Expense, RecurringExpense

# Home Page View
def home(request):
    return render(request, 'users/home.html')

# Add a Single Expense
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

# List All Expenses
@login_required
def list_expenses(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'list_expenses.html', {'expenses': expenses})

# User Profile View
def profile(request):
    return render(request, 'users/profile.html')

# Expense Summary View
def expensesummary(request):
    return render(request, 'users/expensesummary.html')

# Spending Alert View
def spendingalert(request):
    return render(request, 'users/spendingalert.html')

# Add Recurring Expense
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import RecurringExpense

# Add Recurring Expense
@login_required
def add_recurring_expense(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        frequency = request.POST.get('frequency')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if not category or not amount or not frequency or not start_date:
            messages.error(request, "All fields except 'End Date' are required.")
            return redirect('add_recurring_expense')

        # Save recurring expense
        RecurringExpense.objects.create(
            user=request.user,
            category=category,
            amount=amount,
            frequency=frequency,
            start_date=start_date,
            end_date=end_date if end_date else None
        )

        messages.success(request, "Recurring expense added successfully!")
        return redirect('recurring_expenses_list')

    return render(request, 'users/add_recurring_expense.html')

# List Recurring Expenses
@login_required
def recurring_expenses_list(request):
    recurring_expenses = RecurringExpense.objects.filter(user=request.user)
    return render(request, 'users/recurring_expenses_list.html', {'recurring_expenses': recurring_expenses})
