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


class Agent(Model):
    """The agent details.

    :param tenant_id: The tenant Id.
    :type tenant_id: str
    :param machine_id: The machine Id.
    :type machine_id: str
    :param credential: The agent credential details.
    :type credential:
     list[~azure.mgmt.adhybridhealthservice.models.Credential]
    :param machine_name: The machine name.
    :type machine_name: str
    :param agent_version: The agent version.
    :type agent_version: str
    :param created_date: The date and time, in UTC, when the agent was
     created.
    :type created_date: datetime
    :param key:  The connector hash key.
    :type key: str
    """

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'machine_id': {'key': 'machineId', 'type': 'str'},
        'credential': {'key': 'credential', 'type': '[Credential]'},
        'machine_name': {'key': 'machineName', 'type': 'str'},
        'agent_version': {'key': 'agentVersion', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'key': {'key': 'key', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Agent, self).__init__(**kwargs)
        self.tenant_id = kwargs.get('tenant_id', None)
        self.machine_id = kwargs.get('machine_id', None)
        self.credential = kwargs.get('credential', None)
        self.machine_name = kwargs.get('machine_name', None)
        self.agent_version = kwargs.get('agent_version', None)
        self.created_date = kwargs.get('created_date', None)
        self.key = kwargs.get('key', None)