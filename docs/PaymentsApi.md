# pirlpay.PaymentsApi

All URIs are relative to *https://api.pirlpay.com/api/v1/merchant*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_billing_plans_create**](PaymentsApi.md#payments_billing_plans_create) | **POST** /payments/billing-plans/ | 
[**payments_billing_plans_list**](PaymentsApi.md#payments_billing_plans_list) | **GET** /payments/billing-plans/ | 

# **payments_billing_plans_create**
> BillingPlan payments_billing_plans_create(body)



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
api_instance = pirlpay.PaymentsApi(pirlpay.ApiClient(configuration))
body = pirlpay.BillingPlan() # BillingPlan | 

try:
    api_response = api_instance.payments_billing_plans_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->payments_billing_plans_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingPlan**](BillingPlan.md)|  | 

### Return type

[**BillingPlan**](BillingPlan.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_billing_plans_list**
> list[BillingPlan] payments_billing_plans_list()



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
api_instance = pirlpay.PaymentsApi(pirlpay.ApiClient(configuration))

try:
    api_response = api_instance.payments_billing_plans_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->payments_billing_plans_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BillingPlan]**](BillingPlan.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

