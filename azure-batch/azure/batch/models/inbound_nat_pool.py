# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InboundNATPool(Model):
    """A inbound NAT pool that can be used to address specific ports on compute
    nodes in a Batch pool externally.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the endpoint. The name must be unique
     within a Batch pool, can contain letters, numbers, underscores, periods,
     and hyphens. Names must start with a letter or number, must end with a
     letter, number, or underscore, and cannot exceed 77 characters.  If any
     invalid values are provided the request fails with HTTP status code 400.
    :type name: str
    :param protocol: Required. The protocol of the endpoint. Possible values
     include: 'tcp', 'udp'
    :type protocol: str or ~azure.batch.models.InboundEndpointProtocol
    :param backend_port: Required. The port number on the compute node. This
     must be unique within a Batch pool. Acceptable values are between 1 and
     65535 except for 22, 3389, 29876 and 29877 as these are reserved. If any
     reserved values are provided the request fails with HTTP status code 400.
    :type backend_port: int
    :param frontend_port_range_start: Required. The first port number in the
     range of external ports that will be used to provide inbound access to the
     backendPort on individual compute nodes. Acceptable values range between 1
     and 65534 except ports from 50000 to 55000 which are reserved. All ranges
     within a pool must be distinct and cannot overlap. Each range must contain
     at least 40 ports. If any reserved or overlapping values are provided the
     request fails with HTTP status code 400.
    :type frontend_port_range_start: int
    :param frontend_port_range_end: Required. The last port number in the
     range of external ports that will be used to provide inbound access to the
     backendPort on individual compute nodes. Acceptable values range between 1
     and 65534 except ports from 50000 to 55000 which are reserved by the Batch
     service. All ranges within a pool must be distinct and cannot overlap.
     Each range must contain at least 40 ports. If any reserved or overlapping
     values are provided the request fails with HTTP status code 400.
    :type frontend_port_range_end: int
    :param network_security_group_rules: A list of network security group
     rules that will be applied to the endpoint. The maximum number of rules
     that can be specified across all the endpoints on a Batch pool is 25. If
     no network security group rules are specified, a default rule will be
     created to allow inbound access to the specified backendPort. If the
     maximum number of network security group rules is exceeded the request
     fails with HTTP status code 400.
    :type network_security_group_rules:
     list[~azure.batch.models.NetworkSecurityGroupRule]
    """

    _validation = {
        'name': {'required': True},
        'protocol': {'required': True},
        'backend_port': {'required': True},
        'frontend_port_range_start': {'required': True},
        'frontend_port_range_end': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'protocol': {'key': 'protocol', 'type': 'InboundEndpointProtocol'},
        'backend_port': {'key': 'backendPort', 'type': 'int'},
        'frontend_port_range_start': {'key': 'frontendPortRangeStart', 'type': 'int'},
        'frontend_port_range_end': {'key': 'frontendPortRangeEnd', 'type': 'int'},
        'network_security_group_rules': {'key': 'networkSecurityGroupRules', 'type': '[NetworkSecurityGroupRule]'},
    }

    def __init__(self, **kwargs):
        super(InboundNATPool, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.protocol = kwargs.get('protocol', None)
        self.backend_port = kwargs.get('backend_port', None)
        self.frontend_port_range_start = kwargs.get('frontend_port_range_start', None)
        self.frontend_port_range_end = kwargs.get('frontend_port_range_end', None)
        self.network_security_group_rules = kwargs.get('network_security_group_rules', None)