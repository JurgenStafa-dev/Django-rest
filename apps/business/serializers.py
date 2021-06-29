from rest_framework import serializers
from .models import Business_Condition, Business_Basic_Info, Cashflow, Balance_sheet


class BusinessBasicSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(required=False)
    address_1 = serializers.CharField(required=False)
    address_2 = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    zipcode = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    sector = serializers.JSONField(required=False)
    industry = serializers.CharField(required=False)
    website = serializers.CharField(required=False)
    number_of_employees = serializers.IntegerField(required=False)
    description_of_business = serializers.CharField(required=False)

    class Meta:
        model = Business_Basic_Info
        fields = '__all__'


class BusinessConditionSerializer(serializers.ModelSerializer):
    company_formation = serializers.CharField(required=False)
    business_model = serializers.CharField(required=False)
    leverage_on_tech = serializers.CharField(required=False)
    competitiveness_1 = serializers.CharField(required=False)
    competitiveness_2 = serializers.CharField(required=False)
    competitiveness_3 = serializers.CharField(required=False)
    growth_1 = serializers.CharField(required=False)
    growth_2 = serializers.CharField(required=False)
    growth_3 = serializers.CharField(required=False)
    top_risk_1 = serializers.CharField(required=False)
    top_risk_2 = serializers.CharField(required=False)
    top_risk_3 = serializers.CharField(required=False)
    rival_sector = serializers.CharField(required=False)
    competitor_1 = serializers.CharField(required=False)
    competitor_2 = serializers.CharField(required=False)
    competitor_3 = serializers.CharField(required=False)
    supplychain_risk = serializers.CharField(required=False)
    business_basic_info_id = serializers.IntegerField(required=True)

    class Meta:
        model = Business_Condition
        fields = "__all__"
        # exclude = ["business_basic_info_id"]

class CashflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashflow
        fields = '__all__'

class BalanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance_sheet
        fields = '__all__'
