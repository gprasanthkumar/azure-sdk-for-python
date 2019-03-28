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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.adds_services_operations import AddsServicesOperations
from .operations.alerts_operations import AlertsOperations
from .operations.configuration_operations import ConfigurationOperations
from .operations.dimensions_operations import DimensionsOperations
from .operations.adds_service_members_operations import AddsServiceMembersOperations
from .operations.ad_domain_service_members_operations import AdDomainServiceMembersOperations
from .operations.adds_services_user_preference_operations import AddsServicesUserPreferenceOperations
from .operations.adds_service_operations import AddsServiceOperations
from .operations.adds_services_replication_status_operations import AddsServicesReplicationStatusOperations
from .operations.adds_services_service_members_operations import AddsServicesServiceMembersOperations
from .operations.operations import Operations
from .operations.reports_operations import ReportsOperations
from .operations.services_operations import ServicesOperations
from .operations.service_operations import ServiceOperations
from .operations.service_members_operations import ServiceMembersOperations
from . import models


class ADHybridHealthServiceConfiguration(AzureConfiguration):
    """Configuration for ADHybridHealthService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ADHybridHealthServiceConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-adhybridhealthservice/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class ADHybridHealthService(SDKClient):
    """REST APIs for Azure Active Directory Connect Health

    :ivar config: Configuration for client.
    :vartype config: ADHybridHealthServiceConfiguration

    :ivar adds_services: AddsServices operations
    :vartype adds_services: azure.mgmt.adhybridhealthservice.operations.AddsServicesOperations
    :ivar alerts: Alerts operations
    :vartype alerts: azure.mgmt.adhybridhealthservice.operations.AlertsOperations
    :ivar configuration: Configuration operations
    :vartype configuration: azure.mgmt.adhybridhealthservice.operations.ConfigurationOperations
    :ivar dimensions: Dimensions operations
    :vartype dimensions: azure.mgmt.adhybridhealthservice.operations.DimensionsOperations
    :ivar adds_service_members: AddsServiceMembers operations
    :vartype adds_service_members: azure.mgmt.adhybridhealthservice.operations.AddsServiceMembersOperations
    :ivar ad_domain_service_members: AdDomainServiceMembers operations
    :vartype ad_domain_service_members: azure.mgmt.adhybridhealthservice.operations.AdDomainServiceMembersOperations
    :ivar adds_services_user_preference: AddsServicesUserPreference operations
    :vartype adds_services_user_preference: azure.mgmt.adhybridhealthservice.operations.AddsServicesUserPreferenceOperations
    :ivar adds_service: AddsService operations
    :vartype adds_service: azure.mgmt.adhybridhealthservice.operations.AddsServiceOperations
    :ivar adds_services_replication_status: AddsServicesReplicationStatus operations
    :vartype adds_services_replication_status: azure.mgmt.adhybridhealthservice.operations.AddsServicesReplicationStatusOperations
    :ivar adds_services_service_members: AddsServicesServiceMembers operations
    :vartype adds_services_service_members: azure.mgmt.adhybridhealthservice.operations.AddsServicesServiceMembersOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.adhybridhealthservice.operations.Operations
    :ivar reports: Reports operations
    :vartype reports: azure.mgmt.adhybridhealthservice.operations.ReportsOperations
    :ivar services: Services operations
    :vartype services: azure.mgmt.adhybridhealthservice.operations.ServicesOperations
    :ivar service: Service operations
    :vartype service: azure.mgmt.adhybridhealthservice.operations.ServiceOperations
    :ivar service_members: ServiceMembers operations
    :vartype service_members: azure.mgmt.adhybridhealthservice.operations.ServiceMembersOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = ADHybridHealthServiceConfiguration(credentials, base_url)
        super(ADHybridHealthService, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2014-01-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.adds_services = AddsServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.alerts = AlertsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.configuration = ConfigurationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.dimensions = DimensionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.adds_service_members = AddsServiceMembersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.ad_domain_service_members = AdDomainServiceMembersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.adds_services_user_preference = AddsServicesUserPreferenceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.adds_service = AddsServiceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.adds_services_replication_status = AddsServicesReplicationStatusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.adds_services_service_members = AddsServicesServiceMembersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.reports = ReportsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.services = ServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.service = ServiceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.service_members = ServiceMembersOperations(
            self._client, self.config, self._serialize, self._deserialize)