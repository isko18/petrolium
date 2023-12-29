from rest_framework import serializers
from apps.settings.models import Pricing, History, Jobs, Procurement, Banner,BankDetails
from parler_rest.fields import TranslatedFieldsField
class PricingSerializer(serializers.ModelSerializer):
    translations = TranslatedFieldsField(shared_model=Pricing)
    class Meta:
        model = Pricing
        fields = "__all__"
        
class HistorySerializer(serializers.ModelSerializer):
    translations = TranslatedFieldsField(shared_model=History)
    class Meta:
        model = History
        fields = "__all__"
        
class JobsSerializer(serializers.ModelSerializer):
    translations = TranslatedFieldsField(shared_model=Jobs)
    class Meta:
        model = Jobs
        fields = "__all__"
        
class ProcurementSerializer(serializers.ModelSerializer):
    translations = TranslatedFieldsField(shared_model=Procurement)
    class Meta:
        model = Procurement
        fields = "__all__"

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        fields = "__all__"