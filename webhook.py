import requests
import json
from fastapi.responses import JSONResponse
from fastapi import Depends
from schemas import schemas
# from fastapi.security import 

# oauth2_scheme=O

auth_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VkSUQiOiJubkBleGFtcGxlLmNvbSIsImV4cGlyeSI6MTY2NTk2MDMwMi4yNjE5NjkzfQ.jyX5N9_vLrJEA4sXr5m-96nBOhWrcCE4Ut-Pw7MvqIw'
hed = {'Content-type': 'application/json','Authorization': 'Bearer ' + auth_token}

def order_dispatched(url:str):
  data= schemas.Order()
  r = requests.post(url, json=json.loads(data.json()), headers=hed)
  return JSONResponse(content=None, status_code=200) if r.status_code==200 else None


def order_cancelled(url:str):
  data=schemas.Order_canceller()
  r = requests.post(url, json=json.loads(data.json()), headers=hed)
  return JSONResponse(content=None, status_code=200) if r.status_code==200 else None

url = "https://webhook.site/88d825cd-ee99-4806-b67e-6a14a4021018"
print(order_dispatched(url))
print(order_cancelled(url))
# https://webhook.site/88d825cd-ee99-4806-b67e-6a14a4021018