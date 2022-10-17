from http.client import ACCEPTED, HTTPException
from urllib import response
from fastapi import FastAPI, HTTPException, Request, Body, status, Header, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from schemas import schemas
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer
from app import model
import json

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



# https://stageapi.glovoapp.com/webhook/stores/{storeId}/orders/{orderId}/status
# @app.put("/webhook/stores/{storeId}/orders/{orderId}/status",status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(jwtBearer())], tags=["order"])
# async def update_order(storeId:str, orderId:str, status_order:schemas.Status_class, Content_type: str | None = Header(default="application/json")):
#     # return status_order
#     headers={"Content-type":"application/json"}
#     values = [x.value for x in schemas.Status]
#     print(status_order in values)
#     print(status_order)
#     if status_order.status not in values:
#         rm = schemas.Response_model()
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, headers=headers, detail= rm)
#     return    

@app.put("/webhook/stores/{storeId}/orders/{orderId}/status",status_code=status.HTTP_204_NO_CONTENT,dependencies=[Depends(jwtBearer())], tags=["order"],
responses={
        400: json.loads(schemas.Response_model().json())
    },
)
async def update_order(storeId:str, orderId:str, status_order:schemas.Status_class, Content_type: str | None = Header(default="application/json")):
    # return status_order
    headers={"Content-type":"application/json"}
    values = [x.value for x in schemas.Status]
    if status_order.status not in values:
        rm= schemas.Response_model()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, headers=headers, detail= rm)
    return  
    

# https://stageapi.glovoapp.com/webhook/stores/{storeId}/orders/{orderId}/replace_products
@app.post("/webhook/stores/{storeId}/orders/{orderId}/replace_products", dependencies=[Depends(jwtBearer())], response_model =schemas.Order,tags=["order"])
async def modify_order(storeId:str, orderId:str, request:schemas.Modify_request,  Content_type: str | None = Header(default="application/json")):
    headers={"Content-type":"application/json"}
    try:    
        res = schemas.Order()
        return res
    except:
        rm = schemas.Response_model()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, headers=headers, detail= rm)
    

    
    
