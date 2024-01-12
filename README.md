# azure-fast-api-sample
sample api

this is sample api code to test out azure ad

Here is the base tutorial I followed for setting up azure with postman https://dev.to/425show/calling-an-azure-ad-secured-api-with-postman-22co

To install the setup.py run ```pip install -e .```

Fill in the .env file with the correct values from microsoft AD

To run the fastapi server ```uvicorn sample_api.main:app --reload ```

To test follow the steps in the blog post above, and generate an auth token following the steps on postman. Then try to access the endpoint on localhost:8000/api/test which is protected via the auth

