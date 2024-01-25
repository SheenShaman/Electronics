from rest_framework import serializers

from main.models import Link, Contacts, Product
from main.validators import prohibition_change_debt


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer()
    products = ProductSerializer(many=True, read_only=True)
    hierarchy_level = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Link
        fields = '__all__'

    @staticmethod
    def get_hierarchy_level(obj):
        provider = obj.provider
        if provider:
            if provider.network_object == '0':
                return 1
            return int(provider.network_object) + 1
        else:
            return 0

    def validate(self, attrs):
        instance = self.instance

        old_debt = instance.debt if instance else None
        new_debt = attrs.get('debt', old_debt)

        prohibition_change_debt(new_debt, old_debt)
        return attrs
