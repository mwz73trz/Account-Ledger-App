from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account_ledger_app.views import LedgerViewSet

router = DefaultRouter()
router.register("ledgers", LedgerViewSet, basename="ledger")

urlpatterns = [
    path("", include(router.urls)),
]