import string
import random
from smartmin.views import *
from .models import *
from rest_framework.generics import CreateAPIView
from .serializers import *
from rest_framework import viewsets
from .authentication import MyOwnTokenAuthentication
from .custompermissions import *
from rest_framework import views
from django.contrib.auth.models import User
from .models import Token


class ProductCRUDL(SmartCRUDL):
    model = Product

    class List(SmartListView):
        fields = ('name', 'cost_per_item', 'stock_quantity', 'volume')

    class Create(SmartCreateView):
        fields = ('name', 'description', 'cost_per_item', 'stock_quantity')

    class Update(SmartUpdateView):
        fields = ('name', 'description', 'cost_per_item', 'stock_quantity')


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [MyOwnTokenAuthentication]
    permission_classes = [MyPermission]


class TokenModelViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenModelSerializer
    # permission_classes = [MyPermission]


class LogInModelViewSet(views.APIView):
    def post(self, request, *args, **kwargs):
        usr = request.data.get('username')
        passwd = request.data.get('password')
        user = User.objects.filter(username = usr, password = passwd)
        if user:
            token = Token.objects.filter(user_id = user)
            if token:
                return Token.objects.get(user_token=user)
            else:
                tk = ''.join( random.choice( string.ascii_uppercase + string.digits ) for x in range( 32 ) )
                t = Token(user_id = user, user_token = tk)
                t.save()
        else:
            return "user not authenticated...!!"


class UserCreateModelViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer