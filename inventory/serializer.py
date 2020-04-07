from rest_framework import serializers
from .models import Family, Location, Product, Transaction


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['reference', 'title', 'description']


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['reference', 'title', 'description', 'unit']


class ProductSerializer(serializers.ModelSerializer):
    # location = LocationSerializer()
    # family = FamilySerializer()
    class Meta:
        model = Product
        fields = ['sku', 'barcode', 'title', 'description', 'location', 'family']


class TransactionSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    class Meta:
        model = Transaction
        fields = ['sku', 'barcode', 'product']
