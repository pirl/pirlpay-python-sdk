# pirlpay
The PirlPay API for automated payment processing
pip install twine
- API version: v1
- Package version: 0.0.1

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import pirlpay 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pirlpay
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import pirlpay
from pirlpay.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = pirlpay.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pirlpay.BillingApi(pirlpay.ApiClient(configuration))
body = pirlpay.ProductTransaction() # ProductTransaction | 

try:
    api_response = api_instance.billing_products_transactions_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_products_transactions_create: %s\n" % e)
# Configure HTTP basic authorization: Basic
configuration = pirlpay.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pirlpay.BillingApi(pirlpay.ApiClient(configuration))

try:
    api_response = api_instance.billing_products_transactions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_products_transactions_list: %s\n" % e)
# Configure HTTP basic authorization: Basic
configuration = pirlpay.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pirlpay.BillingApi(pirlpay.ApiClient(configuration))
body = pirlpay.SimplePayment() # SimplePayment | 

try:
    api_response = api_instance.billing_simple_payment_transactions_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_simple_payment_transactions_create: %s\n" % e)
# Configure HTTP basic authorization: Basic
configuration = pirlpay.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pirlpay.BillingApi(pirlpay.ApiClient(configuration))

try:
    api_response = api_instance.billing_simple_payment_transactions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_simple_payment_transactions_list: %s\n" % e)
# Configure HTTP basic authorization: Basic
configuration = pirlpay.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pirlpay.BillingApi(pirlpay.ApiClient(configuration))
body = pirlpay.Subscription() # Subscription | 

try:
    api_response = api_instance.billing_subscriptions_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_subscriptions_create: %s\n" % e)
# Configure HTTP basic authorization: Basic
configuration = pirlpay.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pirlpay.BillingApi(pirlpay.ApiClient(configuration))

try:
    api_response = api_instance.billing_subscriptions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_subscriptions_list: %s\n" % e)
# Configure HTTP basic authorization: Basic
configuration = pirlpay.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pirlpay.BillingApi(pirlpay.ApiClient(configuration))

try:
    api_response = api_instance.billing_subscriptions_transactions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_subscriptions_transactions_list: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.pirlpay.com/api/v1/merchant*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BillingApi* | [**billing_products_transactions_create**](docs/BillingApi.md#billing_products_transactions_create) | **POST** /billing/products-transactions/ | 
*BillingApi* | [**billing_products_transactions_list**](docs/BillingApi.md#billing_products_transactions_list) | **GET** /billing/products-transactions/ | 
*BillingApi* | [**billing_simple_payment_transactions_create**](docs/BillingApi.md#billing_simple_payment_transactions_create) | **POST** /billing/simple-payment-transactions/ | 
*BillingApi* | [**billing_simple_payment_transactions_list**](docs/BillingApi.md#billing_simple_payment_transactions_list) | **GET** /billing/simple-payment-transactions/ | 
*BillingApi* | [**billing_subscriptions_create**](docs/BillingApi.md#billing_subscriptions_create) | **POST** /billing/subscriptions/ | 
*BillingApi* | [**billing_subscriptions_list**](docs/BillingApi.md#billing_subscriptions_list) | **GET** /billing/subscriptions/ | 
*BillingApi* | [**billing_subscriptions_transactions_list**](docs/BillingApi.md#billing_subscriptions_transactions_list) | **GET** /billing/subscriptions-transactions/ | 
*CatalogsApi* | [**catalogs_products_create**](docs/CatalogsApi.md#catalogs_products_create) | **POST** /catalogs/products/ | 
*CatalogsApi* | [**catalogs_products_list**](docs/CatalogsApi.md#catalogs_products_list) | **GET** /catalogs/products/ | 
*PaymentsApi* | [**payments_billing_plans_create**](docs/PaymentsApi.md#payments_billing_plans_create) | **POST** /payments/billing-plans/ | 
*PaymentsApi* | [**payments_billing_plans_list**](docs/PaymentsApi.md#payments_billing_plans_list) | **GET** /payments/billing-plans/ | 

## Documentation For Models

 - [BillingPlan](docs/BillingPlan.md)
 - [Product](docs/Product.md)
 - [ProductTransaction](docs/ProductTransaction.md)
 - [SimplePayment](docs/SimplePayment.md)
 - [SimplePaymentGet](docs/SimplePaymentGet.md)
 - [Subscription](docs/Subscription.md)
 - [SubscriptionTransaction](docs/SubscriptionTransaction.md)

## Documentation For Authorization


## Basic

- **Type**: HTTP basic authentication


## Author

support@pirl.io
