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


class Amount(Model):
    """Object to represent monetary quantities.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar currency: The currency for the amount value.
    :vartype currency: str
    :ivar value: Amount value.
    :vartype value: float
    """

    _validation = {
        'currency': {'readonly': True},
        'value': {'readonly': True},
    }

    _attribute_map = {
        'currency': {'key': 'currency', 'type': 'str'},
        'value': {'key': 'value', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(Amount, self).__init__(**kwargs)
        self.currency = None
        self.value = None
