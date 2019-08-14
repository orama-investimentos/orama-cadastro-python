# coding: utf-8

"""
    Criação de Contas

    API de Criação de Contas.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: cadastro_api@orama.com.br
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cadastro_orama.api_client import ApiClient
from cadastro_orama.exceptions import (
    ApiTypeError,
    ApiValueError
)


class DevelopersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def perfil_get(self, **kwargs):  # noqa: E501
        """Retorna uma lista composta por objetos do tipo perfil  # noqa: E501

        Returna uma lista composta por objetos do tipo perfil  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perfil_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param float limite: Número máximo de elementos
        :param float deslocamento: Número de deslocamento (offset) dos elementos
        :param str campos: Lista de campos para ser inclusivamente filtrados
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ListaPerfilUsuario
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.perfil_get_with_http_info(**kwargs)  # noqa: E501

    def perfil_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retorna uma lista composta por objetos do tipo perfil  # noqa: E501

        Returna uma lista composta por objetos do tipo perfil  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perfil_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param float limite: Número máximo de elementos
        :param float deslocamento: Número de deslocamento (offset) dos elementos
        :param str campos: Lista de campos para ser inclusivamente filtrados
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ListaPerfilUsuario, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limite', 'deslocamento', 'campos']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method perfil_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limite' in local_var_params:
            query_params.append(('limite', local_var_params['limite']))  # noqa: E501
        if 'deslocamento' in local_var_params:
            query_params.append(('deslocamento', local_var_params['deslocamento']))  # noqa: E501
        if 'campos' in local_var_params:
            query_params.append(('campos', local_var_params['campos']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Api-Key']  # noqa: E501

        return self.api_client.call_api(
            '/perfil/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListaPerfilUsuario',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
