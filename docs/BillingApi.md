# pirlpay.BillingApi

All URIs are relative to *https://api.pirlpay.com/api/v1/merchant*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_products_transactions_create**](BillingApi.md#billing_products_transactions_create) | **POST** /billing/products-transactions/ | 
[**billing_products_transactions_list**](BillingApi.md#billing_products_transactions_list) | **GET** /billing/products-transactions/ | 
[**billing_simple_payment_transactions_create**](BillingApi.md#billing_simple_payment_transactions_create) | **POST** /billing/simple-payment-transactions/ | 
[**billing_simple_payment_transactions_list**](BillingApi.md#billing_simple_payment_transactions_list) | **GET** /billing/simple-payment-transactions/ | 
[**billing_subscriptions_create**](BillingApi.md#billing_subscriptions_create) | **POST** /billing/subscriptions/ | 
[**billing_subscriptions_list**](BillingApi.md#billing_subscriptions_list) | **GET** /billing/subscriptions/ | 
[**billing_subscriptions_transactions_list**](BillingApi.md#billing_subscriptions_transactions_list) | **GET** /billing/subscriptions-transactions/ | 

# **billing_products_transactions_create**
> ProductTransaction billing_products_transactions_create(body)



### Example
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductTransaction**](ProductTransaction.md)|  | 

### Return type

[**ProductTransaction**](ProductTransaction.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_products_transactions_list**
> list[ProductTransaction] billing_products_transactions_list()



### Example
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

try:
    api_response = api_instance.billing_products_transactions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_products_transactions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProductTransaction]**](ProductTransaction.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_simple_payment_transactions_create**
> SimplePayment billing_simple_payment_transactions_create(body)



### Example
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
body = pirlpay.SimplePayment() # SimplePayment | 

try:
    api_response = api_instance.billing_simple_payment_transactions_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_simple_payment_transactions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SimplePayment**](SimplePayment.md)|  | 

### Return type

[**SimplePayment**](SimplePayment.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_simple_payment_transactions_list**
> list[SimplePaymentGet] billing_simple_payment_transactions_list()



### Example
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

try:
    api_response = api_instance.billing_simple_payment_transactions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_simple_payment_transactions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SimplePaymentGet]**](SimplePaymentGet.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_subscriptions_create**
> Subscription billing_subscriptions_create(body)



### Example
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
body = pirlpay.Subscription() # Subscription | 

try:
    api_response = api_instance.billing_subscriptions_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_subscriptions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Subscription**](Subscription.md)|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_subscriptions_list**
> list[Subscription] billing_subscriptions_list()



### Example
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

try:
    api_response = api_instance.billing_subscriptions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_subscriptions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_subscriptions_transactions_list**
> list[SubscriptionTransaction] billing_subscriptions_transactions_list()



### Example
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

try:
    api_response = api_instance.billing_subscriptions_transactions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_subscriptions_transactions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SubscriptionTransaction]**](SubscriptionTransaction.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

