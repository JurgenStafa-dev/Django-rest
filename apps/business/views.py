from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BusinessConditionSerializer, BusinessBasicSerializer, CashflowSerializer, BalanceSheetSerializer
from .models import Business_Condition, Business_Basic_Info, Cashflow, Balance_sheet
# Create your views here.


class BusinessBasicView(GenericAPIView):
    serializer_class = BusinessBasicSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res_data = {
            "success": True,
            "data": serializer.data
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        data = Business_Basic_Info.objects.all()
        print(data)
        res_data = {
            "success": True,
            "data": BusinessBasicSerializer(data, many=True).data
        }
        return Response(data=res_data, status=status.HTTP_200_OK)


class BusinessConditionView(GenericAPIView):
    serializer_class = BusinessConditionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res_data = {
            "success": True,
            "data": serializer.data
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        data = Business_Condition.objects.all()
        print(data)
        res_data = {
            "success": True,
            "data": BusinessConditionSerializer(data, many=True).data
        }
        return Response(data=res_data, status=status.HTTP_200_OK)


class CashflowView(GenericAPIView):
    serializer_class = CashflowSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res_data = {
            "success": True,
            "data": serializer.data
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        data = Cashflow.objects.all()
        print(data)
        res_data = {
            "success": True,
            "data": CashflowSerializer(data, many=True).data
        }
        return Response(data=res_data, status=status.HTTP_200_OK)


class BalanceSheetView(GenericAPIView):
    serializer_class = BalanceSheetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res_data = {
            "success": True,
            "data": serializer.data
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        data = Balance_sheet.objects.all()
        print(data)
        res_data = {
            "success": True,
            "data": BalanceSheetSerializer(data, many=True).data
        }
        return Response(data=res_data, status=status.HTTP_200_OK)
