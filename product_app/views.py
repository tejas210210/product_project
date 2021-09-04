import string
import random
from smartmin.views import *
from .models import Token,Product
from rest_framework.generics import CreateAPIView
from .serializers import *
from rest_framework import viewsets
from .authentication import MyOwnTokenAuthentication
from .custompermissions import *
from rest_framework import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class ProductCRUDL( SmartCRUDL ):
    model = Product

    class List( SmartListView ):
        fields = ('name', 'cost_per_item', 'stock_quantity', 'volume')

    class Create( SmartCreateView ):
        fields = ('name', 'description', 'cost_per_item', 'stock_quantity')

    class Update( SmartUpdateView ):
        fields = ('name', 'description', 'cost_per_item', 'stock_quantity')


class ProductModelViewSet( viewsets.ModelViewSet ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [MyOwnTokenAuthentication]
    permission_classes = [MyPermission]


class TokenModelViewSet( viewsets.ModelViewSet ):
    queryset = Token.objects.all()
    serializer_class = TokenModelSerializer
    permission_classes = [MyPermission]


def token_generate():
    return ''.join( random.choice( string.ascii_uppercase + string.digits ) for x in range( 32 ) )


class LogInModelViewSet( views.APIView ):
    # permission_classes = [MyPermission]
    def post(self, request, *args, **kwargs):
        user = request.data.get( 'username' )
        passwd = request.data.get( 'password' )
        # print( user, passwd )
        user = authenticate( request, username=user, password=passwd )
        # print( user )
        if user:
            token = Token.objects.filter( user_id=user ).first()
            if token:
                token = token.user_token
                token = {'token': token}
                json_token = json.dumps( token )
                return HttpResponse( json_token, content_type='application/json', status=200 )
            else:
                create_token = Token( user_id=user, user_token=token_generate() )
                create_token.save()
                token = create_token.user_token
                token = {'token': token}
                json_token = json.dumps( token )
                return HttpResponse( json_token, content_type='application/json', status=200 )
        else:
            return HttpResponse( json.dumps( {'msg': 'invalid user'} ), content_type='application/json', status=204 )


class UserCreateModelViewSet( CreateAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [MyPermission]
