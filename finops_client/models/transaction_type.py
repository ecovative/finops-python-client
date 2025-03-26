# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TransactionType(str, Enum):
    """
    TransactionType
    """

    """
    allowed enum values
    """
    BILL = 'Bill'
    BILLPAYMENTCHECK = 'BillPaymentCheck'
    BILLPAYMENTCREDITCARD = 'BillPaymentCreditCard'
    BUILDASSEMBLY = 'BuildAssembly'
    CHECK = 'Check'
    CREDITCARDCHARGE = 'CreditCardCharge'
    CREDITCARDCREDIT = 'CreditCardCredit'
    CREDITMEMO = 'CreditMemo'
    DEPOSIT = 'Deposit'
    ESTIMATE = 'Estimate'
    INVOICE = 'Invoice'
    INVENTORYADJUSTMENT = 'InventoryAdjustment'
    ITEMRECEIPT = 'ItemReceipt'
    JOURNALENTRY = 'JournalEntry'
    PAYCHECK = 'Paycheck'
    PAYROLLLIABILITYCHECK = 'PayrollLiabilityCheck'
    PURCHASEORDER = 'PurchaseOrder'
    RECEIVEPAYMENT = 'ReceivePayment'
    SALESORDER = 'SalesOrder'
    SALESRECEIPT = 'SalesReceipt'
    SALESTAXPAYMENTCHECK = 'SalesTaxPaymentCheck'
    TRANSFER = 'Transfer'
    VENDORCREDIT = 'VendorCredit'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionType from a JSON string"""
        return cls(json.loads(json_str))


