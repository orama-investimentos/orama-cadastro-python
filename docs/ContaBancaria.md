# ContaBancaria

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banco** | **str** | Banco da conta, string com o numero do banco | 
**agencia** | **str** | Agencia bancaria da conta corrente | 
**conta** | **str** | Número da conta corrente sem o dígito verificador | 
**digito** | **str** | Digito verificador da conta corrente | 
**cotitular_conjuge** | **bool** | Informação se o conjuge é co-titular da conta corrente. Necessário caso seja especificado o cpfConjuge | [optional] 
**cpf_conjuge** | **str** | CPF do conjuge caso seja conta conjunta. CPF deve ser válido. O CPF tem que ter os 11 dígitos com a máscara incluindo os pontos e hífen. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


