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


class DiagnosticSettingsCategoryResourceCollection(Model):
    """Represents a collection of diagnostic setting category resources.

    :param value: The collection of diagnostic settings category resources.
    :type value:
     list[~microsoft.aadiam.models.DiagnosticSettingsCategoryResource]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DiagnosticSettingsCategoryResource]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(DiagnosticSettingsCategoryResourceCollection, self).__init__(**kwargs)
        self.value = value
