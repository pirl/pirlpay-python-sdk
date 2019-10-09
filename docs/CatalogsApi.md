# pirlpay.CatalogsApi

All URIs are relative to *https://api.pirlpay.com/api/v1/merchant*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogs_products_create**](CatalogsApi.md#catalogs_products_create) | **POST** /catalogs/products/ | 
[**catalogs_products_list**](CatalogsApi.md#catalogs_products_list) | **GET** /catalogs/products/ | 

# **catalogs_products_create**
> Product catalogs_products_create(body)



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
api_instance = pirlpay.CatalogsApi(pirlpay.ApiClient(configuration))
body = pirlpay.Product() # Product | 

try:
    api_response = api_instance.catalogs_products_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->catalogs_products_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Product**](Product.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_products_list**
> list[Product] catalogs_products_list()



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
api_instance = pirlpay.CatalogsApi(pirlpay.ApiClient(configuration))

try:
    api_response = api_instance.catalogs_products_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->catalogs_products_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Product]**](Product.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

