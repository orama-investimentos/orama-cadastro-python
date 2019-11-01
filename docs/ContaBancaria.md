# ContaBancaria

Modelo de Conta bancária no sistema bancário brasileiro. Deve ser enviado somente uma conta bancária na lista de 'contaBancaria'.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banco** | **str** | Banco da conta, string com o número do banco | 
**tipo** | **str** | Tipo da conta bancária. O tipo deve ser conta corrente (CC) ou conta poupança (CP). | [default to 'CC']
**agencia** | **str** | Agência da conta bancária | 
**conta** | **str** | Número da conta bancária sem o dígito verificador | 
**digito** | **str** | Digito verificador da conta bancária | 
**conta_conjunta** | **bool** | Informação que define se é uma conta conjunta. Caso seja, deve ser definido como true. | [optional] [default to False]
**segundo_participante_titular** | **bool** | Informação se o segundo participante (co-titular) é o titular da conta, caso não seja, o primeiro participante quem esta preenchendo a conta é o titular. | [optional] [default to False]
**cpf_cotitular** | **str** | CPF do co-titular caso seja conta conjunta. CPF deve ser válido. O CPF tem que ter os 11 dígitos com a máscara incluindo os pontos e hífen. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


