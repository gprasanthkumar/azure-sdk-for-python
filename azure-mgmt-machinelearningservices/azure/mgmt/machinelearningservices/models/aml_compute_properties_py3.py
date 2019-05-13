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


class AmlComputeProperties(Model):
    """AML Compute properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param vm_size: Virtual Machine Size
    :type vm_size: str
    :param vm_priority: Virtual Machine priority. Possible values include:
     'Dedicated', 'LowPriority'
    :type vm_priority: str or
     ~azure.mgmt.machinelearningservices.models.VmPriority
    :param scale_settings: Scale settings for AML Compute
    :type scale_settings:
     ~azure.mgmt.machinelearningservices.models.ScaleSettings
    :param user_account_credentials: User account credentials. Credentials for
     an administrator user account that will be created on each compute node.
    :type user_account_credentials:
     ~azure.mgmt.machinelearningservices.models.UserAccountCredentials
    :param subnet: Subnet. Virtual network subnet resource ID the compute
     nodes belong to.
    :type subnet: ~azure.mgmt.machinelearningservices.models.ResourceId
    :ivar allocation_state: Allocation state. Allocation state of the compute.
     Possible values are: steady - Indicates that the compute is not resizing.
     There are no changes to the number of compute nodes in the compute in
     progress. A compute enters this state when it is created and when no
     operations are being performed on the compute to change the number of
     compute nodes. resizing - Indicates that the compute is resizing; that is,
     compute nodes are being added to or removed from the compute. Possible
     values include: 'Steady', 'Resizing'
    :vartype allocation_state: str or
     ~azure.mgmt.machinelearningservices.models.AllocationState
    :ivar allocation_state_transition_time: Allocation state transition time.
     The time at which the compute entered its current allocation state.
    :vartype allocation_state_transition_time: datetime
    :ivar errors: Errors. Collection of errors encountered by various compute
     nodes during node setup.
    :vartype errors:
     list[~azure.mgmt.machinelearningservices.models.MachineLearningServiceError]
    :ivar current_node_count: Current node count. The number of compute nodes
     currently assigned to the compute.
    :vartype current_node_count: int
    :ivar target_node_count: Target node count. The target number of compute
     nodes for the compute. If the allocationState is resizing, this property
     denotes the target node count for the ongoing resize operation. If the
     allocationState is steady, this property denotes the target node count for
     the previous resize operation.
    :vartype target_node_count: int
    :ivar node_state_counts: Node state counts. Counts of various node states
     on the compute.
    :vartype node_state_counts:
     ~azure.mgmt.machinelearningservices.models.NodeStateCounts
    """

    _validation = {
        'allocation_state': {'readonly': True},
        'allocation_state_transition_time': {'readonly': True},
        'errors': {'readonly': True},
        'current_node_count': {'readonly': True},
        'target_node_count': {'readonly': True},
        'node_state_counts': {'readonly': True},
    }

    _attribute_map = {
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'vm_priority': {'key': 'vmPriority', 'type': 'str'},
        'scale_settings': {'key': 'scaleSettings', 'type': 'ScaleSettings'},
        'user_account_credentials': {'key': 'userAccountCredentials', 'type': 'UserAccountCredentials'},
        'subnet': {'key': 'subnet', 'type': 'ResourceId'},
        'allocation_state': {'key': 'allocationState', 'type': 'str'},
        'allocation_state_transition_time': {'key': 'allocationStateTransitionTime', 'type': 'iso-8601'},
        'errors': {'key': 'errors', 'type': '[MachineLearningServiceError]'},
        'current_node_count': {'key': 'currentNodeCount', 'type': 'int'},
        'target_node_count': {'key': 'targetNodeCount', 'type': 'int'},
        'node_state_counts': {'key': 'nodeStateCounts', 'type': 'NodeStateCounts'},
    }

    def __init__(self, *, vm_size: str=None, vm_priority=None, scale_settings=None, user_account_credentials=None, subnet=None, **kwargs) -> None:
        super(AmlComputeProperties, self).__init__(**kwargs)
        self.vm_size = vm_size
        self.vm_priority = vm_priority
        self.scale_settings = scale_settings
        self.user_account_credentials = user_account_credentials
        self.subnet = subnet
        self.allocation_state = None
        self.allocation_state_transition_time = None
        self.errors = None
        self.current_node_count = None
        self.target_node_count = None
        self.node_state_counts = None
