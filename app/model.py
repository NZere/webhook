from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    fullname: str =Field(default=None)
    email : EmailStr = Field(default=None)
    password : str =Field(default=None)
    class Config:
        the_schema = {
            "user_demo":{
                "fullname":"aa",
                "email": "aa@aa.com",
                "password":"aa"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str =Field(default=None)
    class Config:
        the_schema = {
            "user_demo":{
                "email": "aa@aa.com",
                "password":"aa"
            }
        }

