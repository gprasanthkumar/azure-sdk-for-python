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

from .resource_py3 import Resource


class ChargeSummaryByBillingAccount(Resource):
    """A charge summary resource by billing account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar billing_period_id: The id of the billing period resource that the
     usage belongs to.
    :vartype billing_period_id: str
    :ivar usage_start: Billing period start date.
    :vartype usage_start: str
    :ivar usage_end: Billing period end date.
    :vartype usage_end: str
    :ivar azure_charges: Azure Charges.
    :vartype azure_charges: ~azure.mgmt.consumption.models.Amount
    :ivar charges_billed_separately: Charges Billed separately.
    :vartype charges_billed_separately: ~azure.mgmt.consumption.models.Amount
    :ivar marketplace_charges: Marketplace Charges.
    :vartype marketplace_charges: ~azure.mgmt.consumption.models.Amount
    :ivar billing_account_id: The id of the billing account resource that the
     charge belongs to.
    :vartype billing_account_id: str
    :ivar billing_profile_id: The id of the billing profile resource that the
     charge belongs to.
    :vartype billing_profile_id: str
    :ivar invoice_section_id: The id of the invoice section resource that the
     charge belongs to.
    :vartype invoice_section_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
        'billing_period_id': {'readonly': True},
        'usage_start': {'readonly': True},
        'usage_end': {'readonly': True},
        'azure_charges': {'readonly': True},
        'charges_billed_separately': {'readonly': True},
        'marketplace_charges': {'readonly': True},
        'billing_account_id': {'readonly': True},
        'billing_profile_id': {'readonly': True},
        'invoice_section_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'billing_period_id': {'key': 'properties.billingPeriodId', 'type': 'str'},
        'usage_start': {'key': 'properties.usageStart', 'type': 'str'},
        'usage_end': {'key': 'properties.usageEnd', 'type': 'str'},
        'azure_charges': {'key': 'properties.azureCharges', 'type': 'Amount'},
        'charges_billed_separately': {'key': 'properties.chargesBilledSeparately', 'type': 'Amount'},
        'marketplace_charges': {'key': 'properties.marketplaceCharges', 'type': 'Amount'},
        'billing_account_id': {'key': 'properties.billingAccountId', 'type': 'str'},
        'billing_profile_id': {'key': 'properties.billingProfileId', 'type': 'str'},
        'invoice_section_id': {'key': 'properties.invoiceSectionId', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ChargeSummaryByBillingAccount, self).__init__(**kwargs)
        self.billing_period_id = None
        self.usage_start = None
        self.usage_end = None
        self.azure_charges = None
        self.charges_billed_separately = None
        self.marketplace_charges = None
        self.billing_account_id = None
        self.billing_profile_id = None
        self.invoice_section_id = None
