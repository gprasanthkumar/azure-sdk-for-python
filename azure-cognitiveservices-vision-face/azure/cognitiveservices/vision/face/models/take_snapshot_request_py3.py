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


class TakeSnapshotRequest(Model):
    """Request body for taking snapshot operation.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. User specified type for the source object to take
     snapshot from. Currently FaceList, PersonGroup, LargeFaceList and
     LargePersonGroup are supported. Possible values include: 'FaceList',
     'LargeFaceList', 'LargePersonGroup', 'PersonGroup'
    :type type: str or
     ~azure.cognitiveservices.vision.face.models.SnapshotObjectType
    :param object_id: Required. User specified source object id to take
     snapshot from.
    :type object_id: str
    :param apply_scope: Required. User specified array of target Face
     subscription ids for the snapshot. For each snapshot, only subscriptions
     included in the applyScope of Snapshot - Take can apply it.
    :type apply_scope: list[str]
    :param user_data: User specified data about the snapshot for any purpose.
     Length should not exceed 16KB.
    :type user_data: str
    """

    _validation = {
        'type': {'required': True},
        'object_id': {'required': True, 'max_length': 64, 'pattern': r'^[a-z0-9-_]+$'},
        'apply_scope': {'required': True},
        'user_data': {'max_length': 16384},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'SnapshotObjectType'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'apply_scope': {'key': 'applyScope', 'type': '[str]'},
        'user_data': {'key': 'userData', 'type': 'str'},
    }

    def __init__(self, *, type, object_id: str, apply_scope, user_data: str=None, **kwargs) -> None:
        super(TakeSnapshotRequest, self).__init__(**kwargs)
        self.type = type
        self.object_id = object_id
        self.apply_scope = apply_scope
        self.user_data = user_data
