
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.models import Account
from accounts.serializers import AccountsSerializer


class AccountsViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def register(self, request):
        payload = request.data
        serializer = AccountsSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Success!"})

    @action(detail=False, methods=['put', 'patch'])
    def update_profile(self, request):
        try:
            payload = request.data
            email = payload.get('email')
            obj = Account.objects.get(email=email)
            serializer = AccountsSerializer(obj, data=payload, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({"detail": "Account with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False)
    def change_password(self, request):
        try:
            payload = request.data
            email = payload.get('email')
            obj = Account.objects.get(email=email)
            current_password = payload.get('current_password')
            new_password = payload.get('new_password')
            if not new_password:
                return Response({"detail": "Enter your new password"}, status=status.HTTP_400_BAD_REQUEST)
            if current_password == obj.password:
                obj.password = new_password
                obj.save()
            else:
                return Response({"detail": "Password does not match."}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"detail": "Password changed"})
        except Account.DoesNotExist:
            return Response({"detail": "Account with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False)
    def profile(self, request):
        try:
            email = request.query_params.get('email')
            obj = Account.objects.get(email=email)
            serializer = AccountsSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({"detail": "Account with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False)
    def profiles(self, request):
        objs = Account.objects.all()
        serializer = AccountsSerializer(objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
