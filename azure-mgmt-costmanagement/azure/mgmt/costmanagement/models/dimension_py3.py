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

from .resource_py3 import Resource


class Dimension(Resource):
    """Dimension.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :param description:
    :type description: str
    :param filter_enabled:
    :type filter_enabled: bool
    :param grouping_enabled:
    :type grouping_enabled: bool
    :param data:
    :type data: list[str]
    :param total:
    :type total: int
    :param category:
    :type category: str
    :param usage_start:
    :type usage_start: datetime
    :param usage_end:
    :type usage_end: datetime
    :param next_link:
    :type next_link: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'filter_enabled': {'key': 'properties.filterEnabled', 'type': 'bool'},
        'grouping_enabled': {'key': 'properties.groupingEnabled', 'type': 'bool'},
        'data': {'key': 'properties.data', 'type': '[str]'},
        'total': {'key': 'properties.total', 'type': 'int'},
        'category': {'key': 'properties.category', 'type': 'str'},
        'usage_start': {'key': 'properties.usageStart', 'type': 'iso-8601'},
        'usage_end': {'key': 'properties.usageEnd', 'type': 'iso-8601'},
        'next_link': {'key': 'properties.nextLink', 'type': 'str'},
    }

    def __init__(self, *, description: str=None, filter_enabled: bool=None, grouping_enabled: bool=None, data=None, total: int=None, category: str=None, usage_start=None, usage_end=None, next_link: str=None, **kwargs) -> None:
        super(Dimension, self).__init__(**kwargs)
        self.description = description
        self.filter_enabled = filter_enabled
        self.grouping_enabled = grouping_enabled
        self.data = data
        self.total = total
        self.category = category
        self.usage_start = usage_start
        self.usage_end = usage_end
        self.next_link = next_link
