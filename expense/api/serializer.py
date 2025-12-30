from rest_framework import serializers
from .models import Expense,Category

class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Expense
        fields = '__all__'