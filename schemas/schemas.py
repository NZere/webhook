from email import header
from enum import Enum
from http.client import ACCEPTED, HTTPException
from inspect import stack
import re
from threading import stack_size
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