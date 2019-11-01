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


class FrontEndStep(object):
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
        'step': 'float',
        'platform': 'str'
    }

    attribute_map = {
        'step': 'step',
        'platform': 'platform'
    }

    def __init__(self, step=None, platform=None, local_vars_configuration=None):  # noqa: E501
        """FrontEndStep - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._step = None
        self._platform = None
        self.discriminator = None

        if step is not None:
            self.step = step
        if platform is not None:
            self.platform = platform

    @property
    def step(self):
        """Gets the step of this FrontEndStep.  # noqa: E501

        Número positivo inteiro para registrar qual 'step' do ponto de vista de UI/front-end o Perfil se encontra.  # noqa: E501

        :return: The step of this FrontEndStep.  # noqa: E501
        :rtype: float
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this FrontEndStep.

        Número positivo inteiro para registrar qual 'step' do ponto de vista de UI/front-end o Perfil se encontra.  # noqa: E501

        :param step: The step of this FrontEndStep.  # noqa: E501
        :type: float
        """

        self._step = step

    @property
    def platform(self):
        """Gets the platform of this FrontEndStep.  # noqa: E501

        Representa o nome da plaforma do front-end.  # noqa: E501

        :return: The platform of this FrontEndStep.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this FrontEndStep.

        Representa o nome da plaforma do front-end.  # noqa: E501

        :param platform: The platform of this FrontEndStep.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                platform is not None and len(platform) > 200):
            raise ValueError("Invalid value for `platform`, length must be less than or equal to `200`")  # noqa: E501

        self._platform = platform

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
        if not isinstance(other, FrontEndStep):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FrontEndStep):
            return True

        return self.to_dict() != other.to_dict()