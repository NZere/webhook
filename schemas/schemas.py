from email import header
from enum import Enum
from http.client import ACCEPTED, HTTPException
from inspect import stack
import re
from threading import stack_size
from typing import Any, Optional
from urllib import response
from fastapi import FastAPI, HTTPException, Request, Response, status, Header
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder


class Status(str, Enum):
    accepted:str="ACCEPTED"
    ready_for_pickup:str="READY_FOR_PICKUP"
    out_for_delivary:str="OUT_FOR_DELIVERY"
    picked_up_by_customer:str="PICKED_UP_BY_CUSTOMER"

class Status_class(BaseModel):
    status:Status

class Response_model(BaseModel):
    userInfo={}
    code:str = "189654"
    requestId:str = "4568100530282487425",
    domain:str= "com.glovoapp.core-services",
    message:str= "There was a problem with your request.",
    staticCode: int = 0

class Modify_request(BaseModel):
    replacements:list
    removed_purchases:list
    added_products:list

class Payment(str, Enum):
    cash="CASH"
    delayed="DELAYED"

class Courier(BaseModel):
    name:str ="Flash"
    phone_number:str = "+34666666666"

class Invoicing_details(BaseModel):
    company_name:str ="Acme Inc."
    company_address:str ="42 Wallaby Way, Sydney"
    tax_id:str ="B12341234"

class Customer(BaseModel):
    name: str ="Waldo"
    phone_number:str ="N/A"
    hash:str ="11111111-2222-3333-4444-555555555555"
    invoicing_details: Invoicing_details = Invoicing_details()


class Order(BaseModel):
    order_id:str="12345"
    store_id:str="your-store-id"
    order_time: Optional[str] = None
    estimated_pickup_time: Optional[str] = None
    utc_offset_minutes:Optional[str] = None
    payment_method : Payment = Payment.cash
    currency :str = "EUR"
    order_code: str ="BA7DWBUL"
    allergy_info: Optional[str] = None
    special_requirements: Optional[str] = None
    estimated_total_price:int =3080
    delivery_fee: Optional[int] = None
    minimum_basket_surcharge: Optional[int] = None
    customer_cash_payment_amount:  Optional[int] = None
    courier: Courier = Courier()
    customer: Customer=Customer()

class Cansel_reason(str, Enum):
    PRODUCTS_NOT_AVAILABLE="PRODUCTS_NOT_AVAILABLE" 
    STORE_CAN_NOT_DELIVER="STORE_CAN_NOT_DELIVER" 
    PARTNER_PRINTER_ISSUE="PARTNER_PRINTER_ISSUE" 
    USER_ERROR="USER_ERROR" 
    STORE_ERROR="STORE_ERROR" 
    ORDER_NOT_FEASIBLE="ORDER_NOT_FEASIBLE" 
    OTHER="OTHER"

class Payment_strategy(str, Enum):
    PAY_NOTHING="PAY_NOTHING" 
    PAY_PRODUCTS="PAY_PRODUCTS"

class Order_canceller(BaseModel):
    order_id:str ="12345"
    store_id:str= "your-store-id"
    cancel_reason: Cansel_reason =Cansel_reason.STORE_ERROR
    payment_strategy: Payment_strategy= Payment_strategy.PAY_PRODUCTS



