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


class UserAccountCredentials(Model):
    """Settings for user account that gets created on each on the nodes of a
    compute.

    All required parameters must be populated in order to send to Azure.

    :param admin_user_name: Required. User name. Name of the administrator
     user account which can be used to SSH to nodes.
    :type admin_user_name: str
    :param admin_user_ssh_public_key: SSH public key. SSH public key of the
     administrator user account.
    :type admin_user_ssh_public_key: str
    :param admin_user_password: Password. Password of the administrator user
     account.
    :type admin_user_password: str
    """

    _validation = {
        'admin_user_name': {'required': True},
    }

    _attribute_map = {
        'admin_user_name': {'key': 'adminUserName', 'type': 'str'},
        'admin_user_ssh_public_key': {'key': 'adminUserSshPublicKey', 'type': 'str'},
        'admin_user_password': {'key': 'adminUserPassword', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(UserAccountCredentials, self).__init__(**kwargs)
        self.admin_user_name = kwargs.get('admin_user_name', None)
        self.admin_user_ssh_public_key = kwargs.get('admin_user_ssh_public_key', None)
        self.admin_user_password = kwargs.get('admin_user_password', None)
