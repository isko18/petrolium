from django.urls import path
from apps.settings.views import PricingAPIView, ProcurementAPIView, JobsAPIView, HistoryAPIView,BannerAPIView,BankDetailsAPIView

urlpatterns = [
    path('pricing/', PricingAPIView.as_view()),
    path('procumerent/', ProcurementAPIView.as_view()),
    path('jobs/', JobsAPIView.as_view()),
    path('history/', HistoryAPIView.as_view()),
    path('banner/', BannerAPIView.as_view()),
    path('bank_details/', BankDetailsAPIView.as_view()),
]
