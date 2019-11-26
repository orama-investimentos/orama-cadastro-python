# cadastro_orama.DevelopersApi

All URIs are relative to *https://cadastro.orama.com.br/api/contas/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_identificacao_parceiro_post**](DevelopersApi.md#account_identificacao_parceiro_post) | **POST** /identificacao-parceiro/ | Cria um login para usuário.


# **account_identificacao_parceiro_post**
> LoginCriado account_identificacao_parceiro_post(login_senha_objeto)

Cria um login para usuário.

Cria um novo login que será usado para acesso ao sistema.

### Example

* Api Key Authentication (Api-Key):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure API key authorization: Api-Key
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v1.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v1.0"
# Create an instance of the API class
api_instance = cadastro_orama.DevelopersApi(cadastro_orama.ApiClient(configuration))
login_senha_objeto = cadastro_orama.LoginSenhaObjeto() # LoginSenhaObjeto | Dados para criação do login

try:
    # Cria um login para usuário.
    api_response = api_instance.account_identificacao_parceiro_post(login_senha_objeto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->account_identificacao_parceiro_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_senha_objeto** | [**LoginSenhaObjeto**](LoginSenhaObjeto.md)| Dados para criação do login | 

### Return type

[**LoginCriado**](LoginCriado.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Login criado |  -  |
**400** | Dados inválidos ou incompletos |  -  |
**405** | Metodo não permitido |  -  |
**409** | CPF, celular ou e-mail duplicados |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

