from rest_framework.serializers import ModelSerializer
from account_ledger_app.models import Ledger

class LedgerSerializer(ModelSerializer):
    class Meta:
        model = Ledger
        fields = ['id', 'account', 'type', 'check_number', 'description', 'deposit_amount', 'withdrawal_amount', 'date', 'total_deposit', 'total_withdrawal', 'balance']
