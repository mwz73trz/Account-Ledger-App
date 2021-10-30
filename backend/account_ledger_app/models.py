from django.db import models
from django.db.models import Sum, F

class Account(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Ledger(models.Model):
    TYPE_TRANSACTION = [
    ('Deposit', 'Deposit'),
    ('Withdrawal', 'Withdrawal')
]
    type = models.CharField(max_length=10, choices=TYPE_TRANSACTION)
    check_number = models.IntegerField(default=0000, null=True, blank=True)
    description = models.CharField(max_length=254)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    withdrawal_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    date = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="ledgers")

    @property
    def total_deposit(self):
        return Ledger.objects.all().aggregate(total_deposit=Sum('deposit_amount'))

    @property
    def total_withdrawal(self):
        return Ledger.objects.all().aggregate(total_withdrawal=Sum('withdrawal_amount'))

    @property
    def balance(self):
        return Ledger.objects.all().aggregate(balance=Sum(F('deposit_amount') - F('withdrawal_amount')))
    
    def __str__(self):
        return f"{self.type}"


