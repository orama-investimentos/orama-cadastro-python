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

from cadastro_orama.configuration import Configuration


class Aprovacao(object):
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
        'aprovado': 'str'
    }

    attribute_map = {
        'aprovado': 'aprovado'
    }

    def __init__(self, aprovado='INDEFINIDO', local_vars_configuration=None):  # noqa: E501
        """Aprovacao - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aprovado = None
        self.discriminator = None

        if aprovado is not None:
            self.aprovado = aprovado

    @property
    def aprovado(self):
        """Gets the aprovado of this Aprovacao.  # noqa: E501

        Estado de aprovação do perfil.  # noqa: E501

        :return: The aprovado of this Aprovacao.  # noqa: E501
        :rtype: str
        """
        return self._aprovado

    @aprovado.setter
    def aprovado(self, aprovado):
        """Sets the aprovado of this Aprovacao.

        Estado de aprovação do perfil.  # noqa: E501

        :param aprovado: The aprovado of this Aprovacao.  # noqa: E501
        :type: str
        """
        allowed_values = ["APROVADO", "PENDENTE", "EM ANÁLISE", "INDEFINIDO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and aprovado not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `aprovado` ({0}), must be one of {1}"  # noqa: E501
                .format(aprovado, allowed_values)
            )

        self._aprovado = aprovado

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
        if not isinstance(other, Aprovacao):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Aprovacao):
            return True

        return self.to_dict() != other.to_dict()
