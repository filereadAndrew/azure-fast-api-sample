from typing import Union, Annotated
import os
from fastapi import FastAPI, Form, Request
from dotenv import load_dotenv

from fastapi_microsoft_identity import initialize, requires_auth, validate_scope, AuthError

load_dotenv()
azure_client_id = os.getenv("AZURE_CLIENT_ID")
azure_tenant_id = os.getenv("AZURE_TENANT_ID")

app = FastAPI()

def configure_auth(tenant_id, client_id):
    initialize(tenant_id, client_id)
    
configure_auth(azure_tenant_id, azure_client_id)


@app.get("/")
def read_root():
    print(azure_client_id, azure_tenant_id)
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/login")
def login( username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {'password': password}


# Secured endpoint
@app.get('/api/test')
@requires_auth
async def test_endpoint(request:Request):
    # try:
    #     validate_scope(required_scope='client.write', request=request)
    # except AuthError:
    #     return{'try': 'again'}
    return {'hello': 'world'}