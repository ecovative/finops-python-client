# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from finops_client.models.accounting_source import AccountingSource
from finops_client.models.cash_flow_classification import CashFlowClassification
from finops_client.models.statement_level import StatementLevel
from finops_client.models.type_of_account import TypeOfAccount
from typing import Optional, Set
from typing_extensions import Self

class AccountUpdate(BaseModel):
    """
    AccountUpdate
    """ # noqa: E501
    list_id: StrictStr = Field(alias="ListID")
    time_modified: Optional[datetime] = Field(default=None, alias="TimeModified")
    edit_sequence: Optional[StrictInt] = Field(default=None, alias="EditSequence")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    full_name: Optional[StrictStr] = Field(default=None, alias="FullName")
    is_active: Optional[StrictBool] = Field(default=None, alias="IsActive")
    parent_ref_list_id: Optional[StrictStr] = Field(default=None, alias="ParentRefListID")
    parent_ref_full_name: Optional[StrictStr] = Field(default=None, alias="ParentRefFullName")
    sublevel: Optional[StrictInt] = Field(default=None, alias="Sublevel")
    account_type: Optional[TypeOfAccount] = Field(default=None, alias="AccountType")
    special_account_type: Optional[StrictStr] = Field(default=None, alias="SpecialAccountType")
    is_tax_account: Optional[StrictBool] = Field(default=None, alias="IsTaxAccount")
    account_number: Optional[StrictInt] = Field(default=None, alias="AccountNumber")
    bank_number: Optional[StrictStr] = Field(default=None, alias="BankNumber")
    desc: Optional[StrictStr] = Field(default=None, alias="Desc")
    description: Optional[StrictStr] = Field(default=None, alias="Description")
    open_balance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="OpenBalance")
    total_balance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="TotalBalance")
    open_balance_date: Optional[datetime] = Field(default=None, alias="OpenBalanceDate")
    sales_tax_code_ref_list_id: Optional[StrictStr] = Field(default=None, alias="SalesTaxCodeRefListID")
    sales_tax_code_ref_full_name: Optional[StrictStr] = Field(default=None, alias="SalesTaxCodeRefFullName")
    tax_code_ref_list_id: Optional[StrictStr] = Field(default=None, alias="TaxCodeRefListID")
    tax_code_ref_full_name: Optional[StrictStr] = Field(default=None, alias="TaxCodeRefFullName")
    tax_line_info_ret_tax_line_id: Optional[StrictStr] = Field(default=None, alias="TaxLineInfoRetTaxLineID")
    tax_line_info_ret_tax_line_name: Optional[StrictStr] = Field(default=None, alias="TaxLineInfoRetTaxLineName")
    cash_flow_classification: Optional[CashFlowClassification] = Field(default=None, alias="CashFlowClassification")
    currency_ref_list_id: Optional[StrictStr] = Field(default=None, alias="CurrencyRefListID")
    currency_ref_full_name: Optional[StrictStr] = Field(default=None, alias="CurrencyRefFullName")
    time_created: Optional[datetime] = Field(default=None, alias="TimeCreated")
    source: Optional[AccountingSource] = Field(default=None, alias="Source")
    statement_level: Optional[StatementLevel] = Field(default=None, alias="StatementLevel")
    default_currency: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=3)]] = Field(default=None, alias="DefaultCurrency")
    is_intercompany: Optional[StrictBool] = Field(default=None, alias="IsIntercompany")
    db_created_by: Optional[StrictStr] = Field(default=None, alias="DbCreatedBy")
    db_time_created: Optional[datetime] = Field(default=None, alias="DbTimeCreated")
    db_time_modified: Optional[datetime] = Field(default=None, alias="DbTimeModified")
    __properties: ClassVar[List[str]] = ["ListID", "TimeModified", "EditSequence", "Name", "FullName", "IsActive", "ParentRefListID", "ParentRefFullName", "Sublevel", "AccountType", "SpecialAccountType", "IsTaxAccount", "AccountNumber", "BankNumber", "Desc", "Description", "OpenBalance", "TotalBalance", "OpenBalanceDate", "SalesTaxCodeRefListID", "SalesTaxCodeRefFullName", "TaxCodeRefListID", "TaxCodeRefFullName", "TaxLineInfoRetTaxLineID", "TaxLineInfoRetTaxLineName", "CashFlowClassification", "CurrencyRefListID", "CurrencyRefFullName", "TimeCreated", "Source", "StatementLevel", "DefaultCurrency", "IsIntercompany", "DbCreatedBy", "DbTimeCreated", "DbTimeModified"]

    @field_validator('default_currency')
    def default_currency_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BOV', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHE', 'CHF', 'CHW', 'CLF', 'CLP', 'CNY', 'COP', 'COU', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MXV', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'USN', 'UYI', 'UYU', 'UYW', 'UZS', 'VED', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XBA', 'XBB', 'XBC', 'XBD', 'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'XSU', 'XTS', 'XUA', 'XXX', 'YER', 'ZAR', 'ZMW', 'ZWL']):
            raise ValueError("must be one of enum values ('AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BOV', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHE', 'CHF', 'CHW', 'CLF', 'CLP', 'CNY', 'COP', 'COU', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MXV', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'USN', 'UYI', 'UYU', 'UYW', 'UZS', 'VED', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XBA', 'XBB', 'XBC', 'XBD', 'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'XSU', 'XTS', 'XUA', 'XXX', 'YER', 'ZAR', 'ZMW', 'ZWL')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AccountUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if time_modified (nullable) is None
        # and model_fields_set contains the field
        if self.time_modified is None and "time_modified" in self.model_fields_set:
            _dict['TimeModified'] = None

        # set to None if edit_sequence (nullable) is None
        # and model_fields_set contains the field
        if self.edit_sequence is None and "edit_sequence" in self.model_fields_set:
            _dict['EditSequence'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['Name'] = None

        # set to None if full_name (nullable) is None
        # and model_fields_set contains the field
        if self.full_name is None and "full_name" in self.model_fields_set:
            _dict['FullName'] = None

        # set to None if is_active (nullable) is None
        # and model_fields_set contains the field
        if self.is_active is None and "is_active" in self.model_fields_set:
            _dict['IsActive'] = None

        # set to None if parent_ref_list_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_ref_list_id is None and "parent_ref_list_id" in self.model_fields_set:
            _dict['ParentRefListID'] = None

        # set to None if parent_ref_full_name (nullable) is None
        # and model_fields_set contains the field
        if self.parent_ref_full_name is None and "parent_ref_full_name" in self.model_fields_set:
            _dict['ParentRefFullName'] = None

        # set to None if sublevel (nullable) is None
        # and model_fields_set contains the field
        if self.sublevel is None and "sublevel" in self.model_fields_set:
            _dict['Sublevel'] = None

        # set to None if account_type (nullable) is None
        # and model_fields_set contains the field
        if self.account_type is None and "account_type" in self.model_fields_set:
            _dict['AccountType'] = None

        # set to None if special_account_type (nullable) is None
        # and model_fields_set contains the field
        if self.special_account_type is None and "special_account_type" in self.model_fields_set:
            _dict['SpecialAccountType'] = None

        # set to None if is_tax_account (nullable) is None
        # and model_fields_set contains the field
        if self.is_tax_account is None and "is_tax_account" in self.model_fields_set:
            _dict['IsTaxAccount'] = None

        # set to None if account_number (nullable) is None
        # and model_fields_set contains the field
        if self.account_number is None and "account_number" in self.model_fields_set:
            _dict['AccountNumber'] = None

        # set to None if bank_number (nullable) is None
        # and model_fields_set contains the field
        if self.bank_number is None and "bank_number" in self.model_fields_set:
            _dict['BankNumber'] = None

        # set to None if desc (nullable) is None
        # and model_fields_set contains the field
        if self.desc is None and "desc" in self.model_fields_set:
            _dict['Desc'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['Description'] = None

        # set to None if open_balance (nullable) is None
        # and model_fields_set contains the field
        if self.open_balance is None and "open_balance" in self.model_fields_set:
            _dict['OpenBalance'] = None

        # set to None if total_balance (nullable) is None
        # and model_fields_set contains the field
        if self.total_balance is None and "total_balance" in self.model_fields_set:
            _dict['TotalBalance'] = None

        # set to None if open_balance_date (nullable) is None
        # and model_fields_set contains the field
        if self.open_balance_date is None and "open_balance_date" in self.model_fields_set:
            _dict['OpenBalanceDate'] = None

        # set to None if sales_tax_code_ref_list_id (nullable) is None
        # and model_fields_set contains the field
        if self.sales_tax_code_ref_list_id is None and "sales_tax_code_ref_list_id" in self.model_fields_set:
            _dict['SalesTaxCodeRefListID'] = None

        # set to None if sales_tax_code_ref_full_name (nullable) is None
        # and model_fields_set contains the field
        if self.sales_tax_code_ref_full_name is None and "sales_tax_code_ref_full_name" in self.model_fields_set:
            _dict['SalesTaxCodeRefFullName'] = None

        # set to None if tax_code_ref_list_id (nullable) is None
        # and model_fields_set contains the field
        if self.tax_code_ref_list_id is None and "tax_code_ref_list_id" in self.model_fields_set:
            _dict['TaxCodeRefListID'] = None

        # set to None if tax_code_ref_full_name (nullable) is None
        # and model_fields_set contains the field
        if self.tax_code_ref_full_name is None and "tax_code_ref_full_name" in self.model_fields_set:
            _dict['TaxCodeRefFullName'] = None

        # set to None if tax_line_info_ret_tax_line_id (nullable) is None
        # and model_fields_set contains the field
        if self.tax_line_info_ret_tax_line_id is None and "tax_line_info_ret_tax_line_id" in self.model_fields_set:
            _dict['TaxLineInfoRetTaxLineID'] = None

        # set to None if tax_line_info_ret_tax_line_name (nullable) is None
        # and model_fields_set contains the field
        if self.tax_line_info_ret_tax_line_name is None and "tax_line_info_ret_tax_line_name" in self.model_fields_set:
            _dict['TaxLineInfoRetTaxLineName'] = None

        # set to None if cash_flow_classification (nullable) is None
        # and model_fields_set contains the field
        if self.cash_flow_classification is None and "cash_flow_classification" in self.model_fields_set:
            _dict['CashFlowClassification'] = None

        # set to None if currency_ref_list_id (nullable) is None
        # and model_fields_set contains the field
        if self.currency_ref_list_id is None and "currency_ref_list_id" in self.model_fields_set:
            _dict['CurrencyRefListID'] = None

        # set to None if currency_ref_full_name (nullable) is None
        # and model_fields_set contains the field
        if self.currency_ref_full_name is None and "currency_ref_full_name" in self.model_fields_set:
            _dict['CurrencyRefFullName'] = None

        # set to None if time_created (nullable) is None
        # and model_fields_set contains the field
        if self.time_created is None and "time_created" in self.model_fields_set:
            _dict['TimeCreated'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['Source'] = None

        # set to None if statement_level (nullable) is None
        # and model_fields_set contains the field
        if self.statement_level is None and "statement_level" in self.model_fields_set:
            _dict['StatementLevel'] = None

        # set to None if default_currency (nullable) is None
        # and model_fields_set contains the field
        if self.default_currency is None and "default_currency" in self.model_fields_set:
            _dict['DefaultCurrency'] = None

        # set to None if is_intercompany (nullable) is None
        # and model_fields_set contains the field
        if self.is_intercompany is None and "is_intercompany" in self.model_fields_set:
            _dict['IsIntercompany'] = None

        # set to None if db_created_by (nullable) is None
        # and model_fields_set contains the field
        if self.db_created_by is None and "db_created_by" in self.model_fields_set:
            _dict['DbCreatedBy'] = None

        # set to None if db_time_created (nullable) is None
        # and model_fields_set contains the field
        if self.db_time_created is None and "db_time_created" in self.model_fields_set:
            _dict['DbTimeCreated'] = None

        # set to None if db_time_modified (nullable) is None
        # and model_fields_set contains the field
        if self.db_time_modified is None and "db_time_modified" in self.model_fields_set:
            _dict['DbTimeModified'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccountUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ListID": obj.get("ListID"),
            "TimeModified": obj.get("TimeModified"),
            "EditSequence": obj.get("EditSequence"),
            "Name": obj.get("Name"),
            "FullName": obj.get("FullName"),
            "IsActive": obj.get("IsActive"),
            "ParentRefListID": obj.get("ParentRefListID"),
            "ParentRefFullName": obj.get("ParentRefFullName"),
            "Sublevel": obj.get("Sublevel"),
            "AccountType": obj.get("AccountType"),
            "SpecialAccountType": obj.get("SpecialAccountType"),
            "IsTaxAccount": obj.get("IsTaxAccount"),
            "AccountNumber": obj.get("AccountNumber"),
            "BankNumber": obj.get("BankNumber"),
            "Desc": obj.get("Desc"),
            "Description": obj.get("Description"),
            "OpenBalance": obj.get("OpenBalance"),
            "TotalBalance": obj.get("TotalBalance"),
            "OpenBalanceDate": obj.get("OpenBalanceDate"),
            "SalesTaxCodeRefListID": obj.get("SalesTaxCodeRefListID"),
            "SalesTaxCodeRefFullName": obj.get("SalesTaxCodeRefFullName"),
            "TaxCodeRefListID": obj.get("TaxCodeRefListID"),
            "TaxCodeRefFullName": obj.get("TaxCodeRefFullName"),
            "TaxLineInfoRetTaxLineID": obj.get("TaxLineInfoRetTaxLineID"),
            "TaxLineInfoRetTaxLineName": obj.get("TaxLineInfoRetTaxLineName"),
            "CashFlowClassification": obj.get("CashFlowClassification"),
            "CurrencyRefListID": obj.get("CurrencyRefListID"),
            "CurrencyRefFullName": obj.get("CurrencyRefFullName"),
            "TimeCreated": obj.get("TimeCreated"),
            "Source": obj.get("Source"),
            "StatementLevel": obj.get("StatementLevel"),
            "DefaultCurrency": obj.get("DefaultCurrency"),
            "IsIntercompany": obj.get("IsIntercompany"),
            "DbCreatedBy": obj.get("DbCreatedBy"),
            "DbTimeCreated": obj.get("DbTimeCreated"),
            "DbTimeModified": obj.get("DbTimeModified")
        })
        return _obj


