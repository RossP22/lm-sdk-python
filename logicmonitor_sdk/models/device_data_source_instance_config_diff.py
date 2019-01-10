# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeviceDataSourceInstanceConfigDiff(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'row_no': 'int',
        'type': 'str',
        'content': 'str'
    }

    attribute_map = {
        'row_no': 'rowNo',
        'type': 'type',
        'content': 'content'
    }

    def __init__(self, row_no=None, type=None, content=None):  # noqa: E501
        """DeviceDataSourceInstanceConfigDiff - a model defined in Swagger"""  # noqa: E501

        self._row_no = None
        self._type = None
        self._content = None
        self.discriminator = None

        if row_no is not None:
            self.row_no = row_no
        if type is not None:
            self.type = type
        if content is not None:
            self.content = content

    @property
    def row_no(self):
        """Gets the row_no of this DeviceDataSourceInstanceConfigDiff.  # noqa: E501


        :return: The row_no of this DeviceDataSourceInstanceConfigDiff.  # noqa: E501
        :rtype: int
        """
        return self._row_no

    @row_no.setter
    def row_no(self, row_no):
        """Sets the row_no of this DeviceDataSourceInstanceConfigDiff.


        :param row_no: The row_no of this DeviceDataSourceInstanceConfigDiff.  # noqa: E501
        :type: int
        """

        self._row_no = row_no

    @property
    def type(self):
        """Gets the type of this DeviceDataSourceInstanceConfigDiff.  # noqa: E501


        :return: The type of this DeviceDataSourceInstanceConfigDiff.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceDataSourceInstanceConfigDiff.


        :param type: The type of this DeviceDataSourceInstanceConfigDiff.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def content(self):
        """Gets the content of this DeviceDataSourceInstanceConfigDiff.  # noqa: E501


        :return: The content of this DeviceDataSourceInstanceConfigDiff.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this DeviceDataSourceInstanceConfigDiff.


        :param content: The content of this DeviceDataSourceInstanceConfigDiff.  # noqa: E501
        :type: str
        """

        self._content = content

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DeviceDataSourceInstanceConfigDiff, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceDataSourceInstanceConfigDiff):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other