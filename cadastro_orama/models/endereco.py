# coding: utf-8

"""
    Criação de Contas

    API de Criação de Contas.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: cadastro_api@orama.com.br
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Endereco(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'cep': 'str',
        'logradouro': 'str',
        'bairro': 'str',
        'uf': 'str',
        'cidade': 'str',
        'numero': 'str',
        'complemento': 'str'
    }

    attribute_map = {
        'cep': 'cep',
        'logradouro': 'logradouro',
        'bairro': 'bairro',
        'uf': 'uf',
        'cidade': 'cidade',
        'numero': 'numero',
        'complemento': 'complemento'
    }

    def __init__(self, cep=None, logradouro=None, bairro=None, uf=None, cidade=None, numero=None, complemento=None):  # noqa: E501
        """Endereco - a model defined in OpenAPI"""  # noqa: E501

        self._cep = None
        self._logradouro = None
        self._bairro = None
        self._uf = None
        self._cidade = None
        self._numero = None
        self._complemento = None
        self.discriminator = None

        if cep is not None:
            self.cep = cep
        if logradouro is not None:
            self.logradouro = logradouro
        if bairro is not None:
            self.bairro = bairro
        if uf is not None:
            self.uf = uf
        if cidade is not None:
            self.cidade = cidade
        if numero is not None:
            self.numero = numero
        if complemento is not None:
            self.complemento = complemento

    @property
    def cep(self):
        """Gets the cep of this Endereco.  # noqa: E501

        Código Postal Brasileiro  # noqa: E501

        :return: The cep of this Endereco.  # noqa: E501
        :rtype: str
        """
        return self._cep

    @cep.setter
    def cep(self, cep):
        """Sets the cep of this Endereco.

        Código Postal Brasileiro  # noqa: E501

        :param cep: The cep of this Endereco.  # noqa: E501
        :type: str
        """

        self._cep = cep

    @property
    def logradouro(self):
        """Gets the logradouro of this Endereco.  # noqa: E501

        logradouro do endereço  # noqa: E501

        :return: The logradouro of this Endereco.  # noqa: E501
        :rtype: str
        """
        return self._logradouro

    @logradouro.setter
    def logradouro(self, logradouro):
        """Sets the logradouro of this Endereco.

        logradouro do endereço  # noqa: E501

        :param logradouro: The logradouro of this Endereco.  # noqa: E501
        :type: str
        """
        if logradouro is not None and len(logradouro) > 200:
            raise ValueError("Invalid value for `logradouro`, length must be less than or equal to `200`")  # noqa: E501

        self._logradouro = logradouro

    @property
    def bairro(self):
        """Gets the bairro of this Endereco.  # noqa: E501

        bairro do endereço, preferencialmente lexicográficamente igual a descrição obtida pelo uso do CEP  # noqa: E501

        :return: The bairro of this Endereco.  # noqa: E501
        :rtype: str
        """
        return self._bairro

    @bairro.setter
    def bairro(self, bairro):
        """Sets the bairro of this Endereco.

        bairro do endereço, preferencialmente lexicográficamente igual a descrição obtida pelo uso do CEP  # noqa: E501

        :param bairro: The bairro of this Endereco.  # noqa: E501
        :type: str
        """
        if bairro is not None and len(bairro) > 30:
            raise ValueError("Invalid value for `bairro`, length must be less than or equal to `30`")  # noqa: E501

        self._bairro = bairro

    @property
    def uf(self):
        """Gets the uf of this Endereco.  # noqa: E501

        Unidade da Federação do endereço  # noqa: E501

        :return: The uf of this Endereco.  # noqa: E501
        :rtype: str
        """
        return self._uf

    @uf.setter
    def uf(self, uf):
        """Sets the uf of this Endereco.

        Unidade da Federação do endereço  # noqa: E501

        :param uf: The uf of this Endereco.  # noqa: E501
        :type: str
        """

        self._uf = uf

    @property
    def cidade(self):
        """Gets the cidade of this Endereco.  # noqa: E501

        Município do endereço. Formato é o nome lexicograficamente igual a descrição do IBGE ou o código de cidade completo do IBGE  # noqa: E501

        :return: The cidade of this Endereco.  # noqa: E501
        :rtype: str
        """
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        """Sets the cidade of this Endereco.

        Município do endereço. Formato é o nome lexicograficamente igual a descrição do IBGE ou o código de cidade completo do IBGE  # noqa: E501

        :param cidade: The cidade of this Endereco.  # noqa: E501
        :type: str
        """
        if cidade is not None and len(cidade) > 200:
            raise ValueError("Invalid value for `cidade`, length must be less than or equal to `200`")  # noqa: E501

        self._cidade = cidade

    @property
    def numero(self):
        """Gets the numero of this Endereco.  # noqa: E501

        Número do logradouro no endereço  # noqa: E501

        :return: The numero of this Endereco.  # noqa: E501
        :rtype: str
        """
        return self._numero

    @numero.setter
    def numero(self, numero):
        """Sets the numero of this Endereco.

        Número do logradouro no endereço  # noqa: E501

        :param numero: The numero of this Endereco.  # noqa: E501
        :type: str
        """
        if numero is not None and len(numero) > 10:
            raise ValueError("Invalid value for `numero`, length must be less than or equal to `10`")  # noqa: E501

        self._numero = numero

    @property
    def complemento(self):
        """Gets the complemento of this Endereco.  # noqa: E501

        Complemento do Endereço  # noqa: E501

        :return: The complemento of this Endereco.  # noqa: E501
        :rtype: str
        """
        return self._complemento

    @complemento.setter
    def complemento(self, complemento):
        """Sets the complemento of this Endereco.

        Complemento do Endereço  # noqa: E501

        :param complemento: The complemento of this Endereco.  # noqa: E501
        :type: str
        """
        if complemento is not None and len(complemento) > 50:
            raise ValueError("Invalid value for `complemento`, length must be less than or equal to `50`")  # noqa: E501

        self._complemento = complemento

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Endereco):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
