from django.test import TestCase
from .models import OrderForm

# Create your tests here.

def create_order(name, condo, amount):
    """
    Create order for agilize production
    """
    order = OrderForm(name=name, condo=condo, amount=amount)
    return order

class OrderModelTest(TestCase):

    def test_order_name_value(self):
        """
        Return false if order name isn't lowercase
        """
        order = create_order(name="PRESUPUESTO", condo="ccm", amount="1")
        self.assertIs(order.name_is_lower(), False)
