from http.client import ACCEPTED, HTTPException
from fastapi import FastAPI, HTTPException, Request, Body, status, Header, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from schemas import schemas
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer
from app import model

app = FastAPI()

@app.get("/")
async def root():
    return {}

users=[
]

@app.post("/user/signup", tags=["user"])
def user_signup(user: model.UserSchema=Body(default=None)):
    users.append(user)
    print(users)
    return signJWT(user.email)

def check_user(data: model.UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

@app.post("/user/login", tags=["user"])
def user_login(user:model.UserLoginSchema=Body(Default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error":"Invalid",
            "users": users
        }

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({{
                                "userInfo": {},
                                "code": "189654",
                                "requestId": "4568100530282487425",
                                "domain": "com.glovoapp.core-services",
                                "message": "There was a problem with your request.",
                                "staticCode": 0
                                }}),
                                    )


# https://stageapi.glovoapp.com/webhook/stores/{storeId}/orders/{orderId}/status
@app.put("/webhook/stores/{storeId}/orders/{orderId}/status",status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(jwtBearer())], tags=["order"])
async def update_order(storeId:str, orderId:str, status_order:schemas.Status_class, Content_type: str | None = Header(default="application/json")):
    # return status_order
    headers={"Content-type":"application/json"}
    values = [x.value for x in schemas.Status]
    print(status_order in values)
    print(status_order)
    if status_order.status not in values:
        rm: schemas.Response_model
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, headers=headers, detail= rm)
    return    

    

# https://stageapi.glovoapp.com/webhook/stores/{storeId}/orders/{orderId}/replace_products
@app.post("/webhook/stores/{storeId}/orders/{orderId}/replace_products", dependencies=[Depends(jwtBearer())], tags=["order"])
async def modify_order(storeId:str, orderId:str, request:schemas.Modify_request,  Content_type: str | None = Header(default="application/json")):
    res=schemas.Response_model
    return res
    
    
    
    
    
    # order = await request.json()
    # try:
    #     check_list = lambda some_list: isinstance(some_list, list)
    #     if "replacements" in order and "removed_purchases" in order and "added_products" in order and check_list(order["replacements"]) and check_list(order["removed_purchases"])and check_list(order["added_products"]):
    #         return JSONResponse(status_code=200, content={
    #             "order_id": "12345",
    #             "store_id": "your-store-id",
    #             "order_time": "2018-06-08 14:24:53",
    #             "estimated_pickup_time": "2018-06-08 14:45:44",
    #             "utc_offset_minutes": "60",
    #             "payment_method": "CASH",
    #             "currency": "EUR",
    #             "order_code": "BA7DWBUL",
    #             "allergy_info": "I am allergic to tomato",
    #             "special_requirements": "Make sure there is no meat",
    #             "estimated_total_price": 3080,
    #             "delivery_fee": None,
    #             "minimum_basket_surcharge": None,
    #             "customer_cash_payment_amount": 5000,
    #             "courier": {
    #                 "name": "Flash",
    #                 "phone_number": "+34666666666"
    #             },
    #             "customer": {
    #                 "name": "Waldo",
    #                 "phone_number": "N/A",
    #                 "hash": "11111111-2222-3333-4444-555555555555",
    #                 "invoicing_details": {
    #                 "company_name": "Acme Inc.",
    #                 "company_address": "42 Wallaby Way, Sydney",
    #                 "tax_id": "B12341234"
    #                 }
    #             },
    #             "products": [
    #                 {
    #                 "id": "pd1",
    #                 "purchased_product_id": "A1",
    #                 "name": "Burger",
    #                 "price": 1000,
    #                 "quantity": 2,
    #                 "attributes": [
    #                     {
    #                     "id": "at1",
    #                     "name": "Extra meat",
    #                     "price": 300,
    #                     "quantity": 1
    #                     },
    #                     {
    #                     "id": "at2",
    #                     "name": "Water (33 cl)",
    #                     "price": 0,
    #                     "quantity": 1
    #                     },
    #                     {
    #                     "id": "at3",
    #                     "name": "Tomato sauce",
    #                     "price": 0,
    #                     "quantity": 1
    #                     },
    #                     {
    #                     "id": "at4",
    #                     "name": "Lettuce",
    #                     "price": 0,
    #                     "quantity": 1
    #                     }
    #                 ]
    #                 },
    #                 {
    #                 "id": "pd2",
    #                 "purchased_product_id": "A2",
    #                 "name": "Ice cream",
    #                 "price": 480,
    #                 "quantity": 1,
    #                 "attributes": [
    #                     {
    #                     "id": "at5",
    #                     "name": "Vanilla",
    #                     "price": 0,
    #                     "quantity": 1
    #                     },
    #                     {
    #                     "id": "at6",
    #                     "name": "Small size",
    #                     "price": 0,
    #                     "quantity": 1
    #                     }
    #                 ]
    #                 }
    #             ],
    #             "delivery_address": {
    #                 "label": "123 Fake Street, Gotham",
    #                 "latitude": 41.3971955,
    #                 "longitude": 2.2001737
    #             },
    #             "bundled_orders": [
    #                 "order-id-1",
    #                 "order-id-2"
    #             ],
    #             "pick_up_code": "433",
    #             "is_picked_up_by_customer": False,
    #             "cutlery_requested": True,
    #             "partner_discounts_products": 1550,
    #             "partner_discounted_products_total": 1530,
    #             "total_customer_to_pay": None,
    #             "loyalty_card": "CUSTOMER123"
    #             })
    #     else:
    #         raise 
    # except:
    #     raise HTTPException(status_code=400, detail={
    #             "userInfo": { },
    #             "code": "189654",
    #             "requestId": "4568100530282487425",
    #             "domain": "com.glovoapp.core-services",
    #             "message": "There was a problem with your request.",
    #             "staticCode": 0
    #             })

