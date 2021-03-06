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

try:
    from .resource_py3 import Resource
    from .purchase_plan_py3 import PurchasePlan
    from .open_shift_router_profile_py3 import OpenShiftRouterProfile
    from .network_profile_py3 import NetworkProfile
    from .open_shift_managed_cluster_master_pool_profile_py3 import OpenShiftManagedClusterMasterPoolProfile
    from .open_shift_managed_cluster_agent_pool_profile_py3 import OpenShiftManagedClusterAgentPoolProfile
    from .open_shift_managed_cluster_base_identity_provider_py3 import OpenShiftManagedClusterBaseIdentityProvider
    from .open_shift_managed_cluster_identity_provider_py3 import OpenShiftManagedClusterIdentityProvider
    from .open_shift_managed_cluster_auth_profile_py3 import OpenShiftManagedClusterAuthProfile
    from .open_shift_managed_cluster_py3 import OpenShiftManagedCluster
    from .open_shift_managed_cluster_aad_identity_provider_py3 import OpenShiftManagedClusterAADIdentityProvider
    from .tags_object_py3 import TagsObject
except (SyntaxError, ImportError):
    from .resource import Resource
    from .purchase_plan import PurchasePlan
    from .open_shift_router_profile import OpenShiftRouterProfile
    from .network_profile import NetworkProfile
    from .open_shift_managed_cluster_master_pool_profile import OpenShiftManagedClusterMasterPoolProfile
    from .open_shift_managed_cluster_agent_pool_profile import OpenShiftManagedClusterAgentPoolProfile
    from .open_shift_managed_cluster_base_identity_provider import OpenShiftManagedClusterBaseIdentityProvider
    from .open_shift_managed_cluster_identity_provider import OpenShiftManagedClusterIdentityProvider
    from .open_shift_managed_cluster_auth_profile import OpenShiftManagedClusterAuthProfile
    from .open_shift_managed_cluster import OpenShiftManagedCluster
    from .open_shift_managed_cluster_aad_identity_provider import OpenShiftManagedClusterAADIdentityProvider
    from .tags_object import TagsObject
from .open_shift_managed_cluster_paged import OpenShiftManagedClusterPaged
from .container_service_client_enums import (
    OSType,
    OpenShiftContainerServiceVMSize,
    OpenShiftAgentPoolProfileRole,
)

__all__ = [
    'Resource',
    'PurchasePlan',
    'OpenShiftRouterProfile',
    'NetworkProfile',
    'OpenShiftManagedClusterMasterPoolProfile',
    'OpenShiftManagedClusterAgentPoolProfile',
    'OpenShiftManagedClusterBaseIdentityProvider',
    'OpenShiftManagedClusterIdentityProvider',
    'OpenShiftManagedClusterAuthProfile',
    'OpenShiftManagedCluster',
    'OpenShiftManagedClusterAADIdentityProvider',
    'TagsObject',
    'OpenShiftManagedClusterPaged',
    'OSType',
    'OpenShiftContainerServiceVMSize',
    'OpenShiftAgentPoolProfileRole',
]
