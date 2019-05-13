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


class Usage(Model):
    """Describes AML Resource Usage.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar unit: An enum describing the unit of usage measurement. Possible
     values include: 'Count'
    :vartype unit: str or ~azure.mgmt.machinelearningservices.models.UsageUnit
    :ivar current_value: The current usage of the resource.
    :vartype current_value: long
    :ivar limit: The maximum permitted usage of the resource.
    :vartype limit: long
    :ivar name: The name of the type of usage.
    :vartype name: ~azure.mgmt.machinelearningservices.models.UsageName
    """

    _validation = {
        'unit': {'readonly': True},
        'current_value': {'readonly': True},
        'limit': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'unit': {'key': 'unit', 'type': 'str'},
        'current_value': {'key': 'currentValue', 'type': 'long'},
        'limit': {'key': 'limit', 'type': 'long'},
        'name': {'key': 'name', 'type': 'UsageName'},
    }

    def __init__(self, **kwargs):
        super(Usage, self).__init__(**kwargs)
        self.unit = None
        self.current_value = None
        self.limit = None
        self.name = None
