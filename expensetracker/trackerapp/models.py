from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to User model
    date = models.DateField()
    label = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.label} - ₹{self.amount} on {self.date}"
    
from django.db import models
from django.contrib.auth.models import User

class RecurringExpense(models.Model):  # Renamed to PascalCase
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recurring_expenses')
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(
        max_length=50,
        choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Annually', 'Annually')]
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.category} - {self.amount} - {self.frequency}'

