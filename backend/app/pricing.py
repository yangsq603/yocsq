from decimal import Decimal
from .models import Product

def calculate_final_price(product: Product) -> Decimal:
    value = product.price + product.shipping + product.tax - product.coupon - product.platform_discount - product.subsidy
    return max(Decimal('0'), value).quantize(Decimal('0.01'))

def with_final_price(product: Product) -> Product:
    return product.model_copy(update={'final_price': calculate_final_price(product)})
