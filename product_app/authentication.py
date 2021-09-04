from rest_framework.authentication import BaseAuthentication
from .models import Token
from rest_framework import exceptions


class MyOwnTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):

        token = request.META.get('HTTP_AUTHORIZATION',None)
        if not token:
            return None
        try:
            token = Token.objects.get(user_token=token)

        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such token.....!!")

        return token.user_id, None