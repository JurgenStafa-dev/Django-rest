from django.urls import path

from .views import BusinessConditionView, BusinessBasicView, CashflowView, BalanceSheetView
app_name = "business"

urlpatterns = [
    path('business_basic/', BusinessBasicView.as_view(),
         name="business_basic"),
    path('business_condition/', BusinessConditionView.as_view(),
         name="business_condition"),
    path('business_cashflow/', CashflowView.as_view(),
         name="business_cashflow"),
    path('business_sheet/', BalanceSheetView.as_view(),
         name="business_sheet"),
]
