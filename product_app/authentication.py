from rest_framework.authentication import BaseAuthentication
from .models import Token
from rest_framework import exceptions


class MyOwnTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_X_user_token')
        if not token:
            return None
        try:
            token = Token.objects.get(user_token=token)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed("no such token")

        return Token, None


