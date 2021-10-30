from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from account_ledger_app.serializers import LedgerSerializer
from account_ledger_app.models import Ledger

class LedgerViewSet(ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer
