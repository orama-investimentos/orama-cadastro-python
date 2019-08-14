# PerfilUsuario

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**us_person** | **bool** | define se o usuário pode ou não ser enquadrado como US person de acordo com a definição da CVM | [optional] [default to False]
**politicamente_exposto** | **bool** | define se o usuário pode ou não ser enquadrado como pessoa politicamente exposta de acordo com a definição da Deliberação Coremec nº 2, de 1º de dezembro de 2006 | [optional] [default to False]
**nacionalidade** | **str** | Definição de Nacionalidade de acordo com o Art. 12 da CF | [optional] 
**uf_nascimento** | **str** | Unidade da Federação em que a pessoa nasceu | [optional] 
**cidade_nascimento** | **str** | Município em que a pessoa nascida no Brasil nasceu. Formato é o nome lexicograficamente igual a descrição do IBGE ou o código de cidade completo do IBGE | [optional] 
**pais_nascimento** | **str** | País em que a pessoa nasceu. Código ISO 3166-1 alpha-2 | [optional] 
**sexo** | **str** | Sexo do indivíduo | [optional] 
**estado_civil** | **str** | Estado civil do usuário | [optional] 
**nome_conjuge** | **str** | Nome do conjuge ou companheiro, necessário em casos que o estado civil seja &#39;Casado(a)&#39; ou &#39;União estável&#39; | [optional] 
**nome_mae** | **str** | Nome da mãe do usuário | [optional] 
**nome_pai** | **str** | Nome do pai do usuário | [optional] 
**login** | [**LoginObjeto**](LoginObjeto.md) |  | [optional] 
**documento** | [**list[Documento]**](Documento.md) |  | [optional] 
**profissao** | [**DadosProfissionais**](DadosProfissionais.md) |  | [optional] 
**endereco** | [**Endereco**](Endereco.md) |  | [optional] 
**patrimonio** | [**DadosPatrimonial**](DadosPatrimonial.md) |  | [optional] 
**conta_bancaria** | [**list[ContaBancaria]**](ContaBancaria.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


