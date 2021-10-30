from rest_framework.serializers import ModelSerializer
from account_ledger_app.models import Account, Ledger

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'ledgers']
        depth = 1

class LedgerSerializer(ModelSerializer):
    class Meta:
        model = Ledger
        fields = ['id', 'type', 'check_number', 'description', 'deposit_amount', 'withdrawal_amount', 'date', 'total_deposit', 'total_withdrawal', 'balance']
