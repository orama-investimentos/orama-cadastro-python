# openapi_client.DevelopersApi

All URIs are relative to *https://cadastro.orama.com.br/api/contas/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perfil_get**](DevelopersApi.md#perfil_get) | **GET** /perfil/ | Retorna uma lista composta por objetos do tipo perfil


# **perfil_get**
> ListaPerfilUsuario perfil_get(limite=limite, deslocamento=deslocamento, campos=campos)

Retorna uma lista composta por objetos do tipo perfil

Returna uma lista composta por objetos do tipo perfil

### Example

* Api Key Authentication (Api-Key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: Api-Key
configuration.api_key['Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Api-Key'] = 'Bearer'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v1.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v1.0"
# Create an instance of the API class
api_instance = openapi_client.DevelopersApi(openapi_client.ApiClient(configuration))
limite = 1000 # float | Número máximo de elementos (optional)
deslocamento = 10 # float | Número de deslocamento (offset) dos elementos (optional)
campos = 'login,profissao,usPerson' # str | Lista de campos para ser inclusivamente filtrados (optional)

try:
    # Retorna uma lista composta por objetos do tipo perfil
    api_response = api_instance.perfil_get(limite=limite, deslocamento=deslocamento, campos=campos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->perfil_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limite** | **float**| Número máximo de elementos | [optional] 
 **deslocamento** | **float**| Número de deslocamento (offset) dos elementos | [optional] 
 **campos** | **str**| Lista de campos para ser inclusivamente filtrados | [optional] 

### Return type

[**ListaPerfilUsuario**](ListaPerfilUsuario.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

