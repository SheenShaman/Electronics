from rest_framework import serializers

from main.models import Link, Contacts, Product
from main.validators import prohibition_change_debt


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

    def validate(self, attrs):
        instance = self.instance

        old_debt = instance.debt if instance else None
        new_debt = attrs.get('debt', old_debt)

        prohibition_change_debt(new_debt, old_debt)
        return attrs


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
