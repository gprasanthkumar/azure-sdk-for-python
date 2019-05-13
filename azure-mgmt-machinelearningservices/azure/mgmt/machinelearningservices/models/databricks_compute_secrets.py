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

from .compute_secrets import ComputeSecrets


class DatabricksComputeSecrets(ComputeSecrets):
    """Secrets related to a Machine Learning compute based on Databricks.

    All required parameters must be populated in order to send to Azure.

    :param compute_type: Required. Constant filled by server.
    :type compute_type: str
    :param databricks_access_token: access token for databricks account.
    :type databricks_access_token: str
    """

    _validation = {
        'compute_type': {'required': True},
    }

    _attribute_map = {
        'compute_type': {'key': 'computeType', 'type': 'str'},
        'databricks_access_token': {'key': 'databricksAccessToken', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DatabricksComputeSecrets, self).__init__(**kwargs)
        self.databricks_access_token = kwargs.get('databricks_access_token', None)
        self.compute_type = 'Databricks'
