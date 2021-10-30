from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account_ledger_app.views import AccountViewSet, LedgerViewSet

router = DefaultRouter()
router.register("accounts", AccountViewSet, basename="account")
router.register("ledgers", LedgerViewSet, basename="ledger")

urlpatterns = [
    path("", include(router.urls)),
]