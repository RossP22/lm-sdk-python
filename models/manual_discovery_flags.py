# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ManualDiscoveryFlags(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'winprocess': 'bool',
        'winservice': 'bool',
        'linuxprocess': 'bool'
    }

    attribute_map = {
        'winprocess': 'winprocess',
        'winservice': 'winservice',
        'linuxprocess': 'linuxprocess'
    }

    def __init__(self, winprocess=None, winservice=None, linuxprocess=None):
        """
        ManualDiscoveryFlags - a model defined in Swagger
        """

        self._winprocess = None
        self._winservice = None
        self._linuxprocess = None

        if winprocess is not None:
          self.winprocess = winprocess
        if winservice is not None:
          self.winservice = winservice
        if linuxprocess is not None:
          self.linuxprocess = linuxprocess

    @property
    def winprocess(self):
        """
        Gets the winprocess of this ManualDiscoveryFlags.

        :return: The winprocess of this ManualDiscoveryFlags.
        :rtype: bool
        """
        return self._winprocess

    @winprocess.setter
    def winprocess(self, winprocess):
        """
        Sets the winprocess of this ManualDiscoveryFlags.

        :param winprocess: The winprocess of this ManualDiscoveryFlags.
        :type: bool
        """

        self._winprocess = winprocess

    @property
    def winservice(self):
        """
        Gets the winservice of this ManualDiscoveryFlags.

        :return: The winservice of this ManualDiscoveryFlags.
        :rtype: bool
        """
        return self._winservice

    @winservice.setter
    def winservice(self, winservice):
        """
        Sets the winservice of this ManualDiscoveryFlags.

        :param winservice: The winservice of this ManualDiscoveryFlags.
        :type: bool
        """

        self._winservice = winservice

    @property
    def linuxprocess(self):
        """
        Gets the linuxprocess of this ManualDiscoveryFlags.

        :return: The linuxprocess of this ManualDiscoveryFlags.
        :rtype: bool
        """
        return self._linuxprocess

    @linuxprocess.setter
    def linuxprocess(self, linuxprocess):
        """
        Sets the linuxprocess of this ManualDiscoveryFlags.

        :param linuxprocess: The linuxprocess of this ManualDiscoveryFlags.
        :type: bool
        """

        self._linuxprocess = linuxprocess

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ManualDiscoveryFlags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
