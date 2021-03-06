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


class Statistics(Model):
    """Definition of the statistic.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar counter_property: Gets the property value of the statistic.
    :vartype counter_property: str
    :ivar counter_value: Gets the value of the statistic.
    :vartype counter_value: long
    :ivar start_time: Gets the startTime of the statistic.
    :vartype start_time: datetime
    :ivar end_time: Gets the endTime of the statistic.
    :vartype end_time: datetime
    :ivar id: Gets the id.
    :vartype id: str
    """

    _validation = {
        'counter_property': {'readonly': True},
        'counter_value': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'id': {'readonly': True},
    }

    _attribute_map = {
        'counter_property': {'key': 'counterProperty', 'type': 'str'},
        'counter_value': {'key': 'counterValue', 'type': 'long'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Statistics, self).__init__(**kwargs)
        self.counter_property = None
        self.counter_value = None
        self.start_time = None
        self.end_time = None
        self.id = None
