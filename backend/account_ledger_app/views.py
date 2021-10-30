from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from account_ledger_app.serializers import AccountSerializer, LedgerSerializer
from account_ledger_app.models import Account, Ledger

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class LedgerViewSet(ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer
