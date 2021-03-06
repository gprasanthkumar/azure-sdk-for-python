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


class ResourcesMoveInfo(Model):
    """Resource Move Info.

    :param target_resource_group: Target resource group.
    :type target_resource_group: str
    :param resources: Collection of Resources.
    :type resources: list[str]
    """

    _attribute_map = {
        'target_resource_group': {'key': 'targetResourceGroup', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[str]'},
    }

    def __init__(self, *, target_resource_group: str=None, resources=None, **kwargs) -> None:
        super(ResourcesMoveInfo, self).__init__(**kwargs)
        self.target_resource_group = target_resource_group
        self.resources = resources
