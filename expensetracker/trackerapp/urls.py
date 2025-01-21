from django.urls import path
from .views import home, add_expense, profile,recurringexpense,expensesummary,spendingalert


urlpatterns = [
    path('', home, name='home'),  # Home page
    path('add_expense', add_expense, name='add_expense'),  # Budget page
    path('profile/', profile, name='profile'),  # Profile page
    path('recurringexpense/', recurringexpense, name='recurringexpense'), #Recurring Expense page
    # path('transaction/', transaction, name='transaction'), #Transaction page
    path('expensesummary/', expensesummary, name='expensesummary'), #Expense Summary page
    path('spendingalert/', spendingalert, name='spendingalert'), #Spending Alert page
]
