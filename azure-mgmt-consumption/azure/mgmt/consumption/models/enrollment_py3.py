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


class Enrollment(Model):
    """Current entity level details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar start_date: Enrollment Start Date
    :vartype start_date: datetime
    :ivar end_date: Enrollment End Date
    :vartype end_date: datetime
    :ivar currency: The currency associated with enrollment
    :vartype currency: str
    :ivar channel: The channel for Enrollment
    :vartype channel: str
    :ivar policies: The attributes associated with legacy enrollment.
    :vartype policies: ~azure.mgmt.consumption.models.EnrollmentPolicies
    :ivar language: The language for Enrollment
    :vartype language: str
    :ivar country_code: The countryCode for Enrollment
    :vartype country_code: str
    :ivar status: Enrollment status
    :vartype status: str
    :ivar billing_cycle: Enrollment billing cycle
    :vartype billing_cycle: str
    """

    _validation = {
        'start_date': {'readonly': True},
        'end_date': {'readonly': True},
        'currency': {'readonly': True},
        'channel': {'readonly': True},
        'policies': {'readonly': True},
        'language': {'readonly': True},
        'country_code': {'readonly': True},
        'status': {'readonly': True},
        'billing_cycle': {'readonly': True},
    }

    _attribute_map = {
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'currency': {'key': 'currency', 'type': 'str'},
        'channel': {'key': 'channel', 'type': 'str'},
        'policies': {'key': 'policies', 'type': 'EnrollmentPolicies'},
        'language': {'key': 'language', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'billing_cycle': {'key': 'billingCycle', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Enrollment, self).__init__(**kwargs)
        self.start_date = None
        self.end_date = None
        self.currency = None
        self.channel = None
        self.policies = None
        self.language = None
        self.country_code = None
        self.status = None
        self.billing_cycle = None
