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

from logicmonitor_sdk.models.exclude_duplicate_ips import ExcludeDuplicateIps  # noqa: F401,E501
from logicmonitor_sdk.models.netscan import Netscan  # noqa: F401,E501
from logicmonitor_sdk.models.rest_schedule import RestSchedule  # noqa: F401,E501


class AWSNetscan(Netscan):
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
        'creator': 'str',
        'collector_group_name': 'str',
        'method': 'str',
        'collector_group': 'int',
        'description': 'str',
        'next_start': 'str',
        'duplicate': 'ExcludeDuplicateIps',
        'version': 'int',
        'collector': 'int',
        'schedule': 'RestSchedule',
        'collector_description': 'str',
        'name': 'str',
        'next_start_epoch': 'int',
        'id': 'int',
        'nsg_id': 'int',
        'group': 'str',
        'access_id': 'str',
        'account_id': 'str',
        'assumed_role_arn': 'str',
        'secret_key': 'str',
        'root_name': 'str',
        'group_id': 'int',
        'aws_az': 'str',
        'external_id': 'str',
        'aws_service': 'str'
    }

    attribute_map = {
        'creator': 'creator',
        'collector_group_name': 'collectorGroupName',
        'method': 'method',
        'collector_group': 'collectorGroup',
        'description': 'description',
        'next_start': 'nextStart',
        'duplicate': 'duplicate',
        'version': 'version',
        'collector': 'collector',
        'schedule': 'schedule',
        'collector_description': 'collectorDescription',
        'name': 'name',
        'next_start_epoch': 'nextStartEpoch',
        'id': 'id',
        'nsg_id': 'nsgId',
        'group': 'group',
        'access_id': 'accessId',
        'account_id': 'accountId',
        'assumed_role_arn': 'assumedRoleArn',
        'secret_key': 'secretKey',
        'root_name': 'rootName',
        'group_id': 'groupId',
        'aws_az': 'awsAZ',
        'external_id': 'externalId',
        'aws_service': 'awsService'
    }

    def __init__(self, creator=None, collector_group_name=None, method=None, collector_group=None, description=None, next_start=None, duplicate=None, version=None, collector=None, schedule=None, collector_description=None, name=None, next_start_epoch=None, id=None, nsg_id=None, group=None, access_id=None, account_id=None, assumed_role_arn=None, secret_key=None, root_name=None, group_id=None, aws_az=None, external_id=None, aws_service=None):  # noqa: E501
        """AWSNetscan - a model defined in Swagger"""  # noqa: E501

        self._creator = None
        self._collector_group_name = None
        self._method = None
        self._collector_group = None
        self._description = None
        self._next_start = None
        self._duplicate = None
        self._version = None
        self._collector = None
        self._schedule = None
        self._collector_description = None
        self._name = None
        self._next_start_epoch = None
        self._id = None
        self._nsg_id = None
        self._group = None
        self._access_id = None
        self._account_id = None
        self._assumed_role_arn = None
        self._secret_key = None
        self._root_name = None
        self._group_id = None
        self._aws_az = None
        self._external_id = None
        self._aws_service = None
        self.discriminator = None

        if creator is not None:
            self.creator = creator
        if collector_group_name is not None:
            self.collector_group_name = collector_group_name
        self.method = method
        if collector_group is not None:
            self.collector_group = collector_group
        if description is not None:
            self.description = description
        if next_start is not None:
            self.next_start = next_start
        self.duplicate = duplicate
        if version is not None:
            self.version = version
        self.collector = collector
        if schedule is not None:
            self.schedule = schedule
        if collector_description is not None:
            self.collector_description = collector_description
        self.name = name
        if next_start_epoch is not None:
            self.next_start_epoch = next_start_epoch
        if id is not None:
            self.id = id
        if nsg_id is not None:
            self.nsg_id = nsg_id
        if group is not None:
            self.group = group
        if access_id is not None:
            self.access_id = access_id
        if account_id is not None:
            self.account_id = account_id
        if assumed_role_arn is not None:
            self.assumed_role_arn = assumed_role_arn
        if secret_key is not None:
            self.secret_key = secret_key
        if root_name is not None:
            self.root_name = root_name
        if group_id is not None:
            self.group_id = group_id
        if aws_az is not None:
            self.aws_az = aws_az
        if external_id is not None:
            self.external_id = external_id
        if aws_service is not None:
            self.aws_service = aws_service

    @property
    def creator(self):
        """Gets the creator of this AWSNetscan.  # noqa: E501

        The user that created the policy  # noqa: E501

        :return: The creator of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this AWSNetscan.

        The user that created the policy  # noqa: E501

        :param creator: The creator of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def collector_group_name(self):
        """Gets the collector_group_name of this AWSNetscan.  # noqa: E501

        The name of the group of the Collector associated with this Netscan  # noqa: E501

        :return: The collector_group_name of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._collector_group_name

    @collector_group_name.setter
    def collector_group_name(self, collector_group_name):
        """Sets the collector_group_name of this AWSNetscan.

        The name of the group of the Collector associated with this Netscan  # noqa: E501

        :param collector_group_name: The collector_group_name of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._collector_group_name = collector_group_name

    @property
    def method(self):
        """Gets the method of this AWSNetscan.  # noqa: E501

        The method that should be used to discover devices. Options are nmap (ICMP Ping), nec2 (EC2), and script  # noqa: E501

        :return: The method of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this AWSNetscan.

        The method that should be used to discover devices. Options are nmap (ICMP Ping), nec2 (EC2), and script  # noqa: E501

        :param method: The method of this AWSNetscan.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def collector_group(self):
        """Gets the collector_group of this AWSNetscan.  # noqa: E501

        The ID of the group of the Collector associated with this Netscan  # noqa: E501

        :return: The collector_group of this AWSNetscan.  # noqa: E501
        :rtype: int
        """
        return self._collector_group

    @collector_group.setter
    def collector_group(self, collector_group):
        """Sets the collector_group of this AWSNetscan.

        The ID of the group of the Collector associated with this Netscan  # noqa: E501

        :param collector_group: The collector_group of this AWSNetscan.  # noqa: E501
        :type: int
        """

        self._collector_group = collector_group

    @property
    def description(self):
        """Gets the description of this AWSNetscan.  # noqa: E501

        The description of the Netscan Policy  # noqa: E501

        :return: The description of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AWSNetscan.

        The description of the Netscan Policy  # noqa: E501

        :param description: The description of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def next_start(self):
        """Gets the next_start of this AWSNetscan.  # noqa: E501

        The date and time of the next start time of the scan - displayed as manual if the scan does not run on a schedule  # noqa: E501

        :return: The next_start of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._next_start

    @next_start.setter
    def next_start(self, next_start):
        """Sets the next_start of this AWSNetscan.

        The date and time of the next start time of the scan - displayed as manual if the scan does not run on a schedule  # noqa: E501

        :param next_start: The next_start of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._next_start = next_start

    @property
    def duplicate(self):
        """Gets the duplicate of this AWSNetscan.  # noqa: E501

        Information that determines how duplicate discovered devices should be handled  # noqa: E501

        :return: The duplicate of this AWSNetscan.  # noqa: E501
        :rtype: ExcludeDuplicateIps
        """
        return self._duplicate

    @duplicate.setter
    def duplicate(self, duplicate):
        """Sets the duplicate of this AWSNetscan.

        Information that determines how duplicate discovered devices should be handled  # noqa: E501

        :param duplicate: The duplicate of this AWSNetscan.  # noqa: E501
        :type: ExcludeDuplicateIps
        """
        if duplicate is None:
            raise ValueError("Invalid value for `duplicate`, must not be `None`")  # noqa: E501

        self._duplicate = duplicate

    @property
    def version(self):
        """Gets the version of this AWSNetscan.  # noqa: E501

        The Id of the device  # noqa: E501

        :return: The version of this AWSNetscan.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AWSNetscan.

        The Id of the device  # noqa: E501

        :param version: The version of this AWSNetscan.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def collector(self):
        """Gets the collector of this AWSNetscan.  # noqa: E501

        The ID of the Collector associated with this Netscan  # noqa: E501

        :return: The collector of this AWSNetscan.  # noqa: E501
        :rtype: int
        """
        return self._collector

    @collector.setter
    def collector(self, collector):
        """Sets the collector of this AWSNetscan.

        The ID of the Collector associated with this Netscan  # noqa: E501

        :param collector: The collector of this AWSNetscan.  # noqa: E501
        :type: int
        """
        if collector is None:
            raise ValueError("Invalid value for `collector`, must not be `None`")  # noqa: E501

        self._collector = collector

    @property
    def schedule(self):
        """Gets the schedule of this AWSNetscan.  # noqa: E501

        Information related to the recurring execution schedule for the Netscan Policy  # noqa: E501

        :return: The schedule of this AWSNetscan.  # noqa: E501
        :rtype: RestSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this AWSNetscan.

        Information related to the recurring execution schedule for the Netscan Policy  # noqa: E501

        :param schedule: The schedule of this AWSNetscan.  # noqa: E501
        :type: RestSchedule
        """

        self._schedule = schedule

    @property
    def collector_description(self):
        """Gets the collector_description of this AWSNetscan.  # noqa: E501

        The description of the Collector associated with this Netscan  # noqa: E501

        :return: The collector_description of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._collector_description

    @collector_description.setter
    def collector_description(self, collector_description):
        """Sets the collector_description of this AWSNetscan.

        The description of the Collector associated with this Netscan  # noqa: E501

        :param collector_description: The collector_description of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._collector_description = collector_description

    @property
    def name(self):
        """Gets the name of this AWSNetscan.  # noqa: E501

        The name of the Netscan Policy  # noqa: E501

        :return: The name of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AWSNetscan.

        The name of the Netscan Policy  # noqa: E501

        :param name: The name of this AWSNetscan.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def next_start_epoch(self):
        """Gets the next_start_epoch of this AWSNetscan.  # noqa: E501

        The epoch of the next start time of the scan - displayed as 0 if the scan does not run on a schedule  # noqa: E501

        :return: The next_start_epoch of this AWSNetscan.  # noqa: E501
        :rtype: int
        """
        return self._next_start_epoch

    @next_start_epoch.setter
    def next_start_epoch(self, next_start_epoch):
        """Sets the next_start_epoch of this AWSNetscan.

        The epoch of the next start time of the scan - displayed as 0 if the scan does not run on a schedule  # noqa: E501

        :param next_start_epoch: The next_start_epoch of this AWSNetscan.  # noqa: E501
        :type: int
        """

        self._next_start_epoch = next_start_epoch

    @property
    def id(self):
        """Gets the id of this AWSNetscan.  # noqa: E501

        The ID of the Netscan Policy  # noqa: E501

        :return: The id of this AWSNetscan.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AWSNetscan.

        The ID of the Netscan Policy  # noqa: E501

        :param id: The id of this AWSNetscan.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def nsg_id(self):
        """Gets the nsg_id of this AWSNetscan.  # noqa: E501

        The ID of the group the policy belongs to  # noqa: E501

        :return: The nsg_id of this AWSNetscan.  # noqa: E501
        :rtype: int
        """
        return self._nsg_id

    @nsg_id.setter
    def nsg_id(self, nsg_id):
        """Sets the nsg_id of this AWSNetscan.

        The ID of the group the policy belongs to  # noqa: E501

        :param nsg_id: The nsg_id of this AWSNetscan.  # noqa: E501
        :type: int
        """

        self._nsg_id = nsg_id

    @property
    def group(self):
        """Gets the group of this AWSNetscan.  # noqa: E501

        The group the Netscan policy should belong to  # noqa: E501

        :return: The group of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AWSNetscan.

        The group the Netscan policy should belong to  # noqa: E501

        :param group: The group of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def access_id(self):
        """Gets the access_id of this AWSNetscan.  # noqa: E501


        :return: The access_id of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._access_id

    @access_id.setter
    def access_id(self, access_id):
        """Sets the access_id of this AWSNetscan.


        :param access_id: The access_id of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._access_id = access_id

    @property
    def account_id(self):
        """Gets the account_id of this AWSNetscan.  # noqa: E501


        :return: The account_id of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AWSNetscan.


        :param account_id: The account_id of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def assumed_role_arn(self):
        """Gets the assumed_role_arn of this AWSNetscan.  # noqa: E501


        :return: The assumed_role_arn of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._assumed_role_arn

    @assumed_role_arn.setter
    def assumed_role_arn(self, assumed_role_arn):
        """Sets the assumed_role_arn of this AWSNetscan.


        :param assumed_role_arn: The assumed_role_arn of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._assumed_role_arn = assumed_role_arn

    @property
    def secret_key(self):
        """Gets the secret_key of this AWSNetscan.  # noqa: E501


        :return: The secret_key of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this AWSNetscan.


        :param secret_key: The secret_key of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def root_name(self):
        """Gets the root_name of this AWSNetscan.  # noqa: E501


        :return: The root_name of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._root_name

    @root_name.setter
    def root_name(self, root_name):
        """Sets the root_name of this AWSNetscan.


        :param root_name: The root_name of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._root_name = root_name

    @property
    def group_id(self):
        """Gets the group_id of this AWSNetscan.  # noqa: E501


        :return: The group_id of this AWSNetscan.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AWSNetscan.


        :param group_id: The group_id of this AWSNetscan.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def aws_az(self):
        """Gets the aws_az of this AWSNetscan.  # noqa: E501


        :return: The aws_az of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._aws_az

    @aws_az.setter
    def aws_az(self, aws_az):
        """Sets the aws_az of this AWSNetscan.


        :param aws_az: The aws_az of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._aws_az = aws_az

    @property
    def external_id(self):
        """Gets the external_id of this AWSNetscan.  # noqa: E501


        :return: The external_id of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this AWSNetscan.


        :param external_id: The external_id of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def aws_service(self):
        """Gets the aws_service of this AWSNetscan.  # noqa: E501


        :return: The aws_service of this AWSNetscan.  # noqa: E501
        :rtype: str
        """
        return self._aws_service

    @aws_service.setter
    def aws_service(self, aws_service):
        """Sets the aws_service of this AWSNetscan.


        :param aws_service: The aws_service of this AWSNetscan.  # noqa: E501
        :type: str
        """

        self._aws_service = aws_service

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
        if issubclass(AWSNetscan, dict):
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
        if not isinstance(other, AWSNetscan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other