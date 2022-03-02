# coding: utf-8

"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@qase.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from qaseio.api_client import ApiClient


class CasesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_case(self, body, code, **kwargs):  # noqa: E501
        """Create a new test case.  # noqa: E501

        This method allows to create a new test case in selected project.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_case(body, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TestCaseCreate body: (required)
        :param str code: Code of project, where to search entities. (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_case_with_http_info(body, code, **kwargs)  # noqa: E501
        else:
            (data) = self.create_case_with_http_info(body, code, **kwargs)  # noqa: E501
            return data

    def create_case_with_http_info(self, body, code, **kwargs):  # noqa: E501
        """Create a new test case.  # noqa: E501

        This method allows to create a new test case in selected project.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_case_with_http_info(body, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TestCaseCreate body: (required)
        :param str code: Code of project, where to search entities. (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_case" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_case`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `create_case`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/case/{code}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_case(self, code, id, **kwargs):  # noqa: E501
        """Delete test case.  # noqa: E501

        This method completely deletes a test case from repository.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_case(code, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Code of project, where to search entities. (required)
        :param int id: Identifier. (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_case_with_http_info(code, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_case_with_http_info(code, id, **kwargs)  # noqa: E501
            return data

    def delete_case_with_http_info(self, code, id, **kwargs):  # noqa: E501
        """Delete test case.  # noqa: E501

        This method completely deletes a test case from repository.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_case_with_http_info(code, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Code of project, where to search entities. (required)
        :param int id: Identifier. (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_case" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `delete_case`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_case`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/case/{code}/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_case(self, code, id, **kwargs):  # noqa: E501
        """Get a specific test case.  # noqa: E501

        This method allows to retrieve a specific test case.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_case(code, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Code of project, where to search entities. (required)
        :param int id: Identifier. (required)
        :return: TestCaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_case_with_http_info(code, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_case_with_http_info(code, id, **kwargs)  # noqa: E501
            return data

    def get_case_with_http_info(self, code, id, **kwargs):  # noqa: E501
        """Get a specific test case.  # noqa: E501

        This method allows to retrieve a specific test case.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_case_with_http_info(code, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Code of project, where to search entities. (required)
        :param int id: Identifier. (required)
        :return: TestCaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_case" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_case`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_case`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/case/{code}/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TestCaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cases(self, code, **kwargs):  # noqa: E501
        """Get all test cases.  # noqa: E501

        This method allows to retrieve all test cases stored in selected project.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cases(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Code of project, where to search entities. (required)
        :param Filters filters:
        :param int limit: A number of entities in result set.
        :param int offset: How many entities should be skipped.
        :return: TestCaseListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cases_with_http_info(code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cases_with_http_info(code, **kwargs)  # noqa: E501
            return data

    def get_cases_with_http_info(self, code, **kwargs):  # noqa: E501
        """Get all test cases.  # noqa: E501

        This method allows to retrieve all test cases stored in selected project.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cases_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Code of project, where to search entities. (required)
        :param Filters filters:
        :param int limit: A number of entities in result set.
        :param int offset: How many entities should be skipped.
        :return: TestCaseListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code', 'filters', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cases" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_cases`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

        query_params = []
        if 'filters' in params:
            query_params.append(('filters', params['filters']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/case/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TestCaseListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_case(self, body, code, id, **kwargs):  # noqa: E501
        """Update test case.  # noqa: E501

        This method updates a test case.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_case(body, code, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TestCaseUpdate body: (required)
        :param str code: Code of project, where to search entities. (required)
        :param int id: Identifier. (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_case_with_http_info(body, code, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_case_with_http_info(body, code, id, **kwargs)  # noqa: E501
            return data

    def update_case_with_http_info(self, body, code, id, **kwargs):  # noqa: E501
        """Update test case.  # noqa: E501

        This method updates a test case.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_case_with_http_info(body, code, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TestCaseUpdate body: (required)
        :param str code: Code of project, where to search entities. (required)
        :param int id: Identifier. (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'code', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_case" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_case`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `update_case`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_case`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/case/{code}/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
