from attr import fields
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from core.models import Contract, Router, Antenna, Package


class RouterSerializer(FlexFieldsModelSerializer):
    """Serializer for cutomer device objects"""

    class Meta:
        model = Router
        fields = ('id', 'name', 'price', 'available', 'updated', 'created')
        read_only_fields = ('id',)


class AntennaSerializer(FlexFieldsModelSerializer):
    """Serializer for cutomer device objects"""

    class Meta:
        model = Antenna
        fields = ('id', 'name', 'price', 'available', 'updated', 'created')
        read_only_fields = ('id',)


class PackageSerializer(serializers.ModelSerializer):
    """Serializer for package objects"""

    class Meta:
        model = Package
        fields = ('id', 'name', 'type', 'price','available','updated', 'created')
        read_only_fields = ('id',)
        


class ContractSerializerGET(FlexFieldsModelSerializer):
    """Serialize a contract"""
    # router = RouterSerializer(
    #     many=True,
    #     read_only=True
    # )

    # antenna = AntennaSerializer(
    #     many=True,
    #     read_only=True
    # )

    # packages = PackageSerializer(
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Contract
        fields = (
            'id', 'user', 'referral', 'contract_no', 'organization', 'contract_type',
            'router', 'antenna','poc_name', 'poc_number', 'poc_email', 'address',
            'packages', 'package_price', 'rou_cond',
            'rou_dec', 'rou_qty', 'rou_amnt', 'rou_lease_amnt', 'rou_amnt_totl', 'rou_collected',
            'ann_cond', 'ann_dec', 'ann_qty', 'ann_amnt', 'ann_lease_amnt', 'ann_amnt_totl', 'ann_collected',
            'cable', 'cable_cond', 'cable_collected', 'other_service', 'other_dec',
            'other_pay_method','other_qty', 'other_price', 'payment_total', 'service_charge',
            'other_charges', 'discount', 'note', 'grand_total', 'curren' ,'status', 'updated', 'created'
        )
        read_only_fields = ('id',)


class ContractSerializerPOST(FlexFieldsModelSerializer):
    """Serialize a contract"""
    # router = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Router.objects.all()
    # )

    # antenna = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Antenna.objects.all()
    # )

    # packages = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Package.objects.all()
    # )

    class Meta:
        model = Contract
        fields = (
            'id', 'user', 'referral', 'contract_no', 'organization', 'contract_type',
            'router', 'antenna','poc_name', 'poc_number', 'poc_email', 'address',
            'packages', 'package_price', 'rou_cond',
            'rou_dec', 'rou_qty', 'rou_amnt', 'rou_lease_amnt', 'rou_amnt_totl', 'rou_collected',
            'ann_cond', 'ann_dec', 'ann_qty', 'ann_amnt', 'ann_lease_amnt', 'ann_amnt_totl', 'ann_collected',
            'cable', 'cable_cond', 'cable_collected', 'other_service', 'other_dec',
            'other_pay_method','other_qty', 'other_price', 'payment_total', 'service_charge',
            'other_charges', 'discount', 'note', 'grand_total', 'curren' ,'status', 'updated', 'created'
        )
        read_only_fields = ('id',)
