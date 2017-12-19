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


class Body(Model):
    """Body.

    :param name: Name of the list.
    :type name: str
    :param description: Description of the list.
    :type description: str
    :param metadata: Metadata of the list.
    :type metadata:
     ~azure.cognitiveservices.vision.contentmoderator.models.BodyMetadata
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': 'BodyMetadata'},
    }

    def __init__(self, name=None, description=None, metadata=None):
        super(Body, self).__init__()
        self.name = name
        self.description = description
        self.metadata = metadata