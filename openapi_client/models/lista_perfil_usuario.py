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


class ListaPerfilUsuario(object):
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
        'quantidade': 'float',
        'proximo': 'str',
        'anterior': 'str',
        'resultados': 'list[PerfilUsuario]'
    }

    attribute_map = {
        'quantidade': 'quantidade',
        'proximo': 'proximo',
        'anterior': 'anterior',
        'resultados': 'resultados'
    }

    def __init__(self, quantidade=None, proximo=None, anterior=None, resultados=None):  # noqa: E501
        """ListaPerfilUsuario - a model defined in OpenAPI"""  # noqa: E501

        self._quantidade = None
        self._proximo = None
        self._anterior = None
        self._resultados = None
        self.discriminator = None

        if quantidade is not None:
            self.quantidade = quantidade
        if proximo is not None:
            self.proximo = proximo
        if anterior is not None:
            self.anterior = anterior
        if resultados is not None:
            self.resultados = resultados

    @property
    def quantidade(self):
        """Gets the quantidade of this ListaPerfilUsuario.  # noqa: E501

        quantidade de elementos que foram retornados  # noqa: E501

        :return: The quantidade of this ListaPerfilUsuario.  # noqa: E501
        :rtype: float
        """
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        """Sets the quantidade of this ListaPerfilUsuario.

        quantidade de elementos que foram retornados  # noqa: E501

        :param quantidade: The quantidade of this ListaPerfilUsuario.  # noqa: E501
        :type: float
        """

        self._quantidade = quantidade

    @property
    def proximo(self):
        """Gets the proximo of this ListaPerfilUsuario.  # noqa: E501

        URL da próxima página de resultados  # noqa: E501

        :return: The proximo of this ListaPerfilUsuario.  # noqa: E501
        :rtype: str
        """
        return self._proximo

    @proximo.setter
    def proximo(self, proximo):
        """Sets the proximo of this ListaPerfilUsuario.

        URL da próxima página de resultados  # noqa: E501

        :param proximo: The proximo of this ListaPerfilUsuario.  # noqa: E501
        :type: str
        """

        self._proximo = proximo

    @property
    def anterior(self):
        """Gets the anterior of this ListaPerfilUsuario.  # noqa: E501

        URL da próxima anterior de resultados  # noqa: E501

        :return: The anterior of this ListaPerfilUsuario.  # noqa: E501
        :rtype: str
        """
        return self._anterior

    @anterior.setter
    def anterior(self, anterior):
        """Sets the anterior of this ListaPerfilUsuario.

        URL da próxima anterior de resultados  # noqa: E501

        :param anterior: The anterior of this ListaPerfilUsuario.  # noqa: E501
        :type: str
        """

        self._anterior = anterior

    @property
    def resultados(self):
        """Gets the resultados of this ListaPerfilUsuario.  # noqa: E501

        Lista composta por objetos do tipo Perfil  # noqa: E501

        :return: The resultados of this ListaPerfilUsuario.  # noqa: E501
        :rtype: list[PerfilUsuario]
        """
        return self._resultados

    @resultados.setter
    def resultados(self, resultados):
        """Sets the resultados of this ListaPerfilUsuario.

        Lista composta por objetos do tipo Perfil  # noqa: E501

        :param resultados: The resultados of this ListaPerfilUsuario.  # noqa: E501
        :type: list[PerfilUsuario]
        """

        self._resultados = resultados

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
        if not isinstance(other, ListaPerfilUsuario):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other