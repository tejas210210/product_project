from smartmin.views import *
from .models import *


class ProductCRUDL(SmartCRUDL):
    model = Product

    class List(SmartListView):
        fields = ('name', 'cost_per_item', 'stock_quantity', 'volume')

    class Create(SmartCreateView):
        fields = ('name', 'description', 'cost_per_item', 'stock_quantity')

    class Update(SmartUpdateView):
        fields = ('name', 'description', 'cost_per_item', 'stock_quantity')
