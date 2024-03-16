from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'category', 'price', 'quantity', 'barcode']
        # extra_kwargs = {
        #         'barcode': {'validators': []}  # Disable unique validator to allow updating
        #     }