import requests
import json
from fastapi.responses import JSONResponse
from fastapi import Depends
# from fastapi.security import 

# oauth2_scheme=O

def order_dispatched(url:str):
  data={
  "order_id": "12345",
  "store_id": "your-store-id",
  "order_time": "2018-06-08 14:24:53",
  "estimated_pickup_time": "2018-06-08 14:45:44",
  "utc_offset_minutes": "60",
  "payment_method": "CASH",
  "currency": "EUR",
  "order_code": "BA7DWBUL",
  "allergy_info": "I am allergic to tomato",
  "special_requirements": "Make sure there is no meat",
  "estimated_total_price": 3080,
  "delivery_fee": None,
  "minimum_basket_surcharge": None,
  "customer_cash_payment_amount": 5000,
  "courier": {
    "name": "Flash",
    "phone_number": "+34666666666"
  },
  "customer": {
    "name": "Waldo",
    "phone_number": "N/A",
    "hash": "11111111-2222-3333-4444-555555555555",
    "invoicing_details": {
      "company_name": "Acme Inc.",
      "company_address": "42 Wallaby Way, Sydney",
      "tax_id": "B12341234"
    }
  },
  "products": [
    {
      "id": "pd1",
      "purchased_product_id": "A1",
      "name": "Burger",
      "price": 1000,
      "quantity": 2,
      "attributes": [
        {
          "id": "at1",
          "name": "Extra meat",
          "price": 300,
          "quantity": 1
        },
        {
          "id": "at2",
          "name": "Water (33 cl)",
          "price": 0,
          "quantity": 1
        },
        {
          "id": "at3",
          "name": "Tomato sauce",
          "price": 0,
          "quantity": 1
        },
        {
          "id": "at4",
          "name": "Lettuce",
          "price": 0,
          "quantity": 1
        }
      ]
    },
    {
      "id": "pd2",
      "purchased_product_id": "A2",
      "name": "Ice cream",
      "price": 480,
      "quantity": 1,
      "attributes": [
        {
          "id": "at5",
          "name": "Vanilla",
          "price": 0,
          "quantity": 1
        },
        {
          "id": "at6",
          "name": "Small size",
          "price": 0,
          "quantity": 1
        }
      ]
    }
  ],
  "delivery_address": {
    "label": "123 Fake Street, Gotham",
    "latitude": 41.3971955,
    "longitude": 2.2001737
  },
  "bundled_orders": [
    "order-id-1",
    "order-id-2"
  ],
  "pick_up_code": "433",
  "is_picked_up_by_customer": False,
  "cutlery_requested": True,
  "partner_discounts_products": 1550,
  "partner_discounted_products_total": 1530,
  "total_customer_to_pay": None,
  "loyalty_card": "CUSTOMER123"
  }
  r = requests.post(url, data=data, headers={'Content-type': 'application/json'})
  print(r.status_code)
  return JSONResponse(content=None, status_code=200) if r.status_code==200 else None


def order_cancelled(url:str):
  data={
    "order_id": "12345",
    "store_id": "your-store-id",
    "cancel_reason": "STORE_ERROR",
    "payment_strategy": "PAY_PRODUCTS"
  }
  r = requests.post(url, data=data, headers={'Content-type': 'application/json'})
  return JSONResponse(content=None, status_code=200) if r.status_code==200 else None

url = "https://webhook.site/88d825cd-ee99-4806-b67e-6a14a4021018"
print(order_dispatched(url))
print(order_cancelled(url))
# https://webhook.site/88d825cd-ee99-4806-b67e-6a14a4021018