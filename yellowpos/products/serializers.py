from rest_framework import serializers

from products.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'tax', 'tax_included')
