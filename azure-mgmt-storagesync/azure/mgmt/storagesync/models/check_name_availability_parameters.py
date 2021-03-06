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


class CheckNameAvailabilityParameters(Model):
    """Parameters for a check name availability request.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name to check for availability
    :type name: str
    :ivar type: Required. The resource type. Must be set to
     Microsoft.StorageSync/storageSyncServices. Default value:
     "Microsoft.StorageSync/storageSyncServices" .
    :vartype type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "Microsoft.StorageSync/storageSyncServices"

    def __init__(self, **kwargs):
        super(CheckNameAvailabilityParameters, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
