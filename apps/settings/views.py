from rest_framework import generics
from apps.settings.models import Pricing, History, Jobs, Procurement, Banner,BankDetails
from apps.settings.serializers import ProcurementSerializer, PricingSerializer, JobsSerializer, HistorySerializer, BannerSerializer,BankDetailsSerializer

class PricingAPIView(generics.ListAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
    
class HistoryAPIView(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    
class JobsAPIView(generics.ListAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    
class ProcurementAPIView(generics.ListAPIView):
    queryset = Procurement.objects.all()
    serializer_class = ProcurementSerializer

class BannerAPIView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BankDetailsAPIView(generics.ListAPIView):
    queryset = BankDetails.objects.all()
    serializer_class = BankDetailsSerializer