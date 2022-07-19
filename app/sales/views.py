from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from rest_flex_fields import FlexFieldsModelViewSet

from core.models import Router, Antenna, Package, Contract, Log

from sales import serializers

import pytz

from datetime import datetime


class BaseSaleAttrViewSet(viewsets.ModelViewSet):
    """Base viewset for user owned sales attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for current authenticated user only"""
        return self.queryset.all().order_by('-name')

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class RouterViewSet(BaseSaleAttrViewSet):
    """Manage devices in the database"""
    queryset = Router.objects.all()
    serializer_class = serializers.RouterSerializer


class AntennaViewSet(BaseSaleAttrViewSet):
    """Manage devices in the database"""
    queryset = Antenna.objects.all()
    serializer_class = serializers.AntennaSerializer


class PackageViewSet(BaseSaleAttrViewSet):
    """Manage packages in the database"""
    queryset = Package.objects.all()
    serializer_class = serializers.PackageSerializer


class LogViewSet(viewsets.ModelViewSet):
    """Manage logs in the database"""
    queryset = Log.objects.all()
    serializer_class = serializers.LogSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for current authenticated user only"""

        contract_no = self.request.query_params.get('contract-no')


        queryset = self.queryset

        if contract_no:
            return queryset.filter(contract__icontains=contract_no).order_by('-updated')
        else:
            return queryset.all().order_by('-updated')

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class ContractViewSet(FlexFieldsModelViewSet):
    """Manage contracts in the database"""
    # @action(methods='POST', detail=True, url_path='contracts')
    # serializer_class = serializers.ContractSerializer

    def get_serializer_class(self):
        """Return apropriate serializer class"""
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.ContractSerializerGET
        else:
            return serializers.ContractSerializerPOST
    queryset = Contract.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
            """Convert a list of string IDs to list of integers"""
            return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve contracts for the authenticated user"""
        contract_no = self.request.query_params.get('contract-no')
        poc_number = self.request.query_params.get('poc_number')
        router = self.request.query_params.get('has-router')
        antenna = self.request.query_params.get('has-antenna')
        package = self.request.query_params.get('has-package')
        device_type = self.request.query_params.get('device-type')
        package_type = self.request.query_params.get('package-type')
        device_condition = self.request.query_params.get('device-condition')
        status = self.request.query_params.get('contract-status')

        start_date = self.request.query_params.get('start_date')
        # start_date = "2022-06-06"
        end_date = self.request.query_params.get('end_date')
        # end_date = "2022-06-21"

        # date_as_string = request.POST['date-search']
        

        # print(date_search)

        queryset = self.queryset

        if status:
            return queryset.filter(status__icontains=status)

        if start_date:
            parsed_date1 = datetime.strptime(start_date, '%Y-%m-%d')
            kabul_timezone = pytz.timezone('Asia/Kabul')
            date_search1 = kabul_timezone.localize(parsed_date1)
            parsed_date2 = datetime.strptime(end_date, '%Y-%m-%d')
            date_search2 = kabul_timezone.localize(parsed_date2)
            print(date_search1)
            print(date_search2)
            return queryset.filter(created__gte=date_search1, created__lte=date_search2)

        if device_condition:
            return queryset.filter(
                Q(ann_cond__icontains=device_condition) |
                Q(rou_cond__icontains=device_condition)
            )
            
        if device_type:
            device_id = self._params_to_ints(device_type)
            return queryset.filter(customerDevices__id__in=device_id)

        if package_type:
            packaage_id = self._params_to_ints(package_type)
            return queryset.filter(packages__id__in=packaage_id)

        if poc_number:
            return queryset.filter(poc_number__icontains=poc_number)

        if contract_no:
            return queryset.filter(contract_no__icontains=contract_no)

        if router == "1":
            return queryset.filter(router__isnull=False)
        
        if router == "0":
            return queryset.filter(router=True)

        if antenna == "1":
            return queryset.filter(antenna__isnull=False)
        
        if antenna == "0":
            return queryset.filter(antenna=True)

        if package == "1":
            return queryset.filter(packages__isnull=False)
        
        if package == "0":
            return queryset.filter(packages__isnull=True)

        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new contract"""
        return serializer.save(user=self.request.user)
