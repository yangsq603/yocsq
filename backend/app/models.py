from __future__ import annotations

from decimal import Decimal
from pydantic import BaseModel, Field, HttpUrl

class Product(BaseModel):
    product_id: str
    platform: str
    title: str
    brand: str | None = None
    model: str | None = None
    sku: str | None = None
    specs: dict[str, str] = Field(default_factory=dict)
    price: Decimal
    shipping: Decimal = Decimal("0")
    tax: Decimal = Decimal("0")
    coupon: Decimal = Decimal("0")
    platform_discount: Decimal = Decimal("0")
    subsidy: Decimal = Decimal("0")
    final_price: Decimal | None = None
    rating: float | None = None
    review_count: int | None = None
    seller: str | None = None
    condition: str = "new"
    image_url: HttpUrl | None = None
    product_url: HttpUrl

class SearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=300)
    platforms: list[str] = Field(default_factory=list)

class SearchResponse(BaseModel):
    query: str
    products: list[Product]
    grouped_products: list[list[str]] = Field(default_factory=list)
