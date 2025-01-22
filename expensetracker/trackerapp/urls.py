from django.urls import path
from .views import home, add_expense, profile,add_recurring_expense,expensesummary,spendingalert, recurring_expenses_list


urlpatterns = [
    path('', home, name='home'),  # Home page
    path('add_expense', add_expense, name='add_expense'),  # Budget page
    path('profile/', profile, name='profile'),  # Profile page
    path('add_recurring_expense/', add_recurring_expense, name='add_recurring_expense'), #Recurring Expense page
    path('recurring_expenses_list/', recurring_expenses_list, name='recurring_expenses_list'), #Recurring Expense page
    # path('transaction/', transaction, name='transaction'), #Transaction page
    path('expensesummary/', expensesummary, name='expensesummary'), #Expense Summary page
    path('spendingalert/', spendingalert, name='spendingalert'), #Spending Alert page
]
