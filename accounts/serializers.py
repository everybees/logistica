from rest_framework import serializers

from accounts.models import Account


class AccountsSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Account
        # fields = "__all__"  # this returns all serialized fields
        exclude = ("password", )    # this excludes password from being returned in serialized data

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
