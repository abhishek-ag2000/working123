"""
Forms
"""
from django import forms
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from accounting_entry.models import LedgerMaster
from bracketline.forms import DateInput
from .models import StockItem
from .models_purchase import PurchaseVoucher, PurchaseStock, PurchaseTerm, PurchaseTax


class PurchaseForm(forms.ModelForm):
    """
    Purchase Form
    """
    class Meta:
        model = PurchaseVoucher
        fields = ('nature_transactions_purchase', 'voucher_date', 'consignee_name', 'consignee_address', 'consignee_pan',
                  'consignee_gstin', 'consignee_contact', 'consignee_state', 'consignee_country', 'supply_state', 'other_details',
                  'delivery_note', 'supplier_ref', 'ref_no', 'party_ac', 'doc_ledger',
                  'gst_details', 'receipt_no', 'despatch_info', 'destination', 'delivery_terms', 'bill_no',
                  'bill_date', 'port_code', 'shipper_place', 'flight_no', 'loading_port', 'discharge_port', 'to_country')
        widgets = {
            'voucher_date': DateInput(),
            'bill_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        self.company = kwargs.pop('Company', None)
        super(PurchaseForm, self).__init__(*args, **kwargs)

        self.fields['voucher_date'].widget.attrs = {'class': 'form-control', }
        self.fields['ref_no'].widget.attrs = {'class': 'form-control', }
        self.fields['party_ac'].queryset = LedgerMaster.objects.filter(
            Q(company=self.company),
            Q(ledger_group__group_base__name__exact='Sundry Creditors') |
            Q(ledger_group__group_base__name__exact='Bank Accounts') |
            Q(ledger_group__group_base__name__exact='Cash-in-Hand'))
        self.fields['party_ac'].widget.attrs = {
            'class': 'select2_demo_2 form-control', }
        self.fields['doc_ledger'].queryset = LedgerMaster.objects.filter(
            Q(company=self.company),
            Q(ledger_group__group_base__name__exact='Purchase Accounts'))
        self.fields['doc_ledger'].widget.attrs = {
            'class': 'select2_demo_2 form-control', }
        self.fields['consignee_name'].widget.attrs = {
            'class': 'form-control', }
        self.fields['consignee_address'].widget.attrs = {'class': 'form-control', }
        self.fields['consignee_gstin'].widget.attrs = {'class': 'form-control', }
        self.fields['consignee_pan'].widget.attrs = {'class': 'form-control', }
        self.fields['consignee_gstin'].widget.attrs['disabled'] = True
        self.fields['consignee_pan'].widget.attrs['disabled'] = True
        self.fields['consignee_contact'].widget.attrs = {
            'class': 'form-control', }
        self.fields['other_details'].widget.attrs = {
                'class': 'form-control', }
        self.fields['consignee_country'].widget.attrs = {
            'class': 'select2_demo_2 form-control', 'onchange': 'country_details_value(this)', }
        self.fields['consignee_state'].widget.attrs = {'class': 'form-control', }
        self.fields['consignee_state'].widget.attrs['disabled'] = True
        self.fields['receipt_no'].widget.attrs = {'class': 'form-control', }
        self.fields['despatch_info'].widget.attrs = {'class': 'form-control', }
        self.fields['destination'].widget.attrs = {'class': 'form-control', }
        self.fields['delivery_terms'].widget.attrs = {
            'class': 'form-control', }
        self.fields['nature_transactions_purchase'].widget.attrs = {
            'class': 'select2_demo_2 form-control', 'onchange': 'gst_change(this)', }
        self.fields['supply_state'].widget.attrs = {
            'class': 'select2_demo_2 form-control', }
        self.fields['delivery_note'].widget.attrs = {'class': 'form-control', }
        self.fields['supplier_ref'].widget.attrs = {'class': 'form-control', }
        self.fields['gst_details'].widget.attrs = {
            'class': 'select2_demo_2 form-control', 'onchange': 'gst_details_value(this)', }
        self.fields['bill_no'].widget.attrs = {'class': 'form-control', }
        self.fields['bill_date'].widget.attrs = {'class': 'form-control', }
        self.fields['port_code'].widget.attrs = {'class': 'form-control', }
        self.fields['shipper_place'].widget.attrs = {'class': 'form-control', }
        self.fields['flight_no'].widget.attrs = {'class': 'form-control', }
        self.fields['loading_port'].widget.attrs = {'class': 'form-control', }
        self.fields['discharge_port'].widget.attrs = {
            'class': 'form-control', }
        self.fields['to_country'].widget.attrs = {
            'class': 'select2_demo_2 form-control', }

    def clean_supply_place(self):
        """
        Clean Method to raise Validatiom Error if Place of Supply do not match with Nature of Transaction provided.
        """
        nature_transactions_purchase = self.cleaned_data['nature_transactions_purchase']
        supply_state = self.cleaned_data['supply_state']

        if self.company.organisation.state == supply_state and nature_transactions_purchase == 'Interstate Purchase - Taxable':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.organisation.state == supply_state and nature_transactions_purchase == 'Imports Exempt':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.organisation.state == supply_state and nature_transactions_purchase == 'Imports Nil Rated':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.organisation.state == supply_state and nature_transactions_purchase == 'Imports Taxable':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.organisation.state == supply_state and nature_transactions_purchase == 'Interstate Purchase exempt':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.organisation.state == supply_state and nature_transactions_purchase == 'Interstate Purchase from Unregistered Dealer - Exempt':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.organisation.state == supply_state and nature_transactions_purchase == 'Interstate Purchase from Unregistered Dealer - Nil Rated':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.organisation.state == supply_state and nature_transactions_purchase == 'Interstate Purchase from Unregistered Dealer - Taxable':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.organisation.state == supply_state and nature_transactions_purchase == 'Interstate Purchase  - Nil Rated':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.organisation.state == supply_state and nature_transactions_purchase == 'Purchase Deemed Exports - Exempt':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.organisation.state == supply_state and nature_transactions_purchase == 'Purchase Deemed Exports - Nil Rated':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.organisation.state == supply_state and nature_transactions_purchase == 'Purchase Deemed Exports - Taxable':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.State != supply_state and nature_transactions_purchase == 'Intrastate Purchase Deemed Exports - Exempt':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.State != supply_state and nature_transactions_purchase == 'Intrastate Purchase Deemed Exports - Nil Rated':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.State != supply_state and nature_transactions_purchase == 'Intrastate Purchase Deemed Exports - Taxable':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.State != supply_state and nature_transactions_purchase == 'Purchase Exempt':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.State != supply_state and nature_transactions_purchase == 'Purchase From Unregister Dealer - Exempt':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.State != supply_state and nature_transactions_purchase == 'Purchase From Unregister Dealer - Nil Rated':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.State != supply_state and nature_transactions_purchase == 'Purchase From Unregister Dealer - Taxable':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.State != supply_state and nature_transactions_purchase == 'Purchase Nil Rated':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        if self.company.State != supply_state and nature_transactions_purchase == 'Intrastate Purchase Taxable':
            raise ValidationError(
                "This nature of transaction in not valid for the given Place of Supply")
        return supply_state

    def clean_ref_no(self):
        """
        Clean function to raise Validation Error if Invoice Number already exist in a company.
        """
        ref_no = self.cleaned_data['ref_no']
        master_id = 0

        if self.instance:
            # master id is used to exclude current master so that it is not checked as duplicate
            master_id = self.instance.id

        if PurchaseVoucher.objects.filter(company=self.company, ref_no__iexact=ref_no).exclude(id=master_id).exists():
            raise forms.ValidationError("This Invoice Number already exists")
        return ref_no


class PurchaseFormAdmin(forms.ModelForm):
    """
    Purchase Form for Admin
    """
    class Meta:
        model = PurchaseVoucher
        fields = ('nature_transactions_purchase', 'voucher_date', 'consignee_name', 'consignee_address', 'consignee_pan', 'consignee_pan',
                  'consignee_contact', 'consignee_state', 'consignee_country', 'supply_state', 'delivery_note',
                  'supplier_ref', 'ref_no', 'party_ac', 'doc_ledger', 'sub_total', 'gst_details', 'receipt_no',
                  'despatch_info', 'destination', 'delivery_terms', 'bill_no', 'bill_date', 'port_code', 'shipper_place',
                  'flight_no', 'loading_port', 'discharge_port', 'supply_country','other_details')
        widgets = {
            'voucher_date': DateInput(),
            'bill_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        self.company = kwargs.pop('company', None)
        super(PurchaseFormAdmin, self).__init__(*args, **kwargs)

        self.fields['voucher_date'].widget.attrs = {'class': 'form-control', }
        self.fields['ref_no'].widget.attrs = {'class': 'form-control', }
        self.fields['billname'].widget.attrs = {'class': 'form-control', }
        self.fields['party_ac'].queryset = LedgerMaster.objects.filter(
            Q(ledger_group___group_base__name__exact='Sundry Creditors') |
            Q(ledger_group___group_base__name__exact='Bank Accounts') |
            Q(ledger_group___group_base__name__exact='Cash-in-Hand'))
        self.fields['party_ac'].widget.attrs = {
            'class': 'select2_demo_2 form-control', }
        self.fields['doc_ledger'].queryset = LedgerMaster.objects.filter(
            Q(ledger_group___group_base__name__exact='Purchase Accounts'))
        self.fields['doc_ledger'].widget.attrs = {
            'class': 'select2_demo_2 form-control', }
        self.fields['consignee_name'].widget.attrs = {
            'class': 'form-control', }
        self.fields['consignee_address'].widget.attrs = {'class': 'form-control', }
        self.fields['consignee_pan'].widget.attrs = {'class': 'form-control', }
        self.fields['consignee_gstin'].widget.attrs = {'class': 'form-control', }
        self.fields['consignee_pan'].widget.attrs['disabled'] = True
        self.fields['consignee_gstin'].widget.attrs['disabled'] = True
        self.fields['consignee_contact'].widget.attrs = {
            'class': 'form-control', }
        self.fields['consignee_country'].widget.attrs = {
            'class': 'select2_demo_2 form-control', 'onchange': 'country_details_value(this)', }
        self.fields['consignee_state'].widget.attrs = {'class': 'form-control', }
        self.fields['consignee_state'].widget.attrs['disabled'] = True
        self.fields['receipt_no'].widget.attrs = {'class': 'form-control', }
        self.fields['despatch_info'].widget.attrs = {'class': 'form-control', }
        self.fields['destination'].widget.attrs = {'class': 'form-control', }
        self.fields['delivery_terms'].widget.attrs = {
            'class': 'form-control', }
        self.fields['nature_transactions_purchase'].widget.attrs = {
            'class': 'select2_demo_2 form-control', 'onchange': 'gst_change(this)', }
        self.fields['sub_total'].widget.attrs = {'class': 'form-control', }
        self.fields['supply_state'].widget.attrs = {
            'class': 'select2_demo_2 form-control', }
        self.fields['Contact'].widget.attrs = {'class': 'form-control', }
        self.fields['delivery_note'].widget.attrs = {'class': 'form-control', }
        self.fields['supplier_ref'].widget.attrs = {'class': 'form-control', }
        self.fields['Mode'].widget.attrs = {'class': 'form-control', }
        self.fields['gst_details'].widget.attrs = {
            'class': 'select2_demo_2 form-control', 'onchange': 'gst_details_value(this)', }
        self.fields['bill_no'].widget.attrs = {'class': 'form-control', }
        self.fields['bill_date'].widget.attrs = {'class': 'form-control', }
        self.fields['port_code'].widget.attrs = {'class': 'form-control', }
        self.fields['shipper_place'].widget.attrs = {'class': 'form-control', }
        self.fields['flight_no'].widget.attrs = {'class': 'form-control', }
        self.fields['loading_port'].widget.attrs = {'class': 'form-control', }
        self.fields['discharge_port'].widget.attrs = {
            'class': 'form-control', }
        self.fields['supply_country'].widget.attrs = {
            'class': 'select2_demo_2 form-control', }

    def clean(self):
        party_ac = self.cleaned_data['party_ac']
        doc_ledger = self.cleaned_data['doc_ledger']
        if party_ac not in LedgerMaster.objects.filter(
                Q(ledger_group___group_base__name__exact='Sundry Creditors') |
                Q(ledger_group___group_base__name__exact='Bank Accounts') |
                Q(ledger_group___group_base__name__exact='Cash-in-Hand')):
            raise forms.ValidationError(
                "Party Account should be for that ledgers which is present under of Sundry Creditors, Bank Accounts & Cash-in-Hand")
        if doc_ledger not in LedgerMaster.objects.filter(
                Q(ledger_group___group_base__name__exact='Purchase Accounts') |
                Q(ledger_group___group_base__name__exact='Purchase Accounts')):
            raise forms.ValidationError(
                "Purchase Ledgers should be for that ledgers which is present under of Purchase Accounts")


class PurchaseStockForm(forms.ModelForm):
    """
    Purchase Stock Form
    """
    class Meta:
        model = PurchaseStock
        fields = ('stock_item', 'quantity', 'rate', 'disc', 'total')

    def __init__(self, *args, **kwargs):
        self.company = kwargs.pop('company', None)
        super(PurchaseStockForm, self).__init__(*args, **kwargs)

        self.fields['stock_item'].queryset = StockItem.objects.filter(
            company=self.company)
        self.fields['stock_item'].widget.attrs = {
            'class': 'select2_demo_2 form-control', 'onchange': 'stock_based_value(this)' }
        self.fields['quantity'].widget.attrs = {'class': 'form-control', 'onchange': 'calcProductTotalPurchase(this)'}
        self.fields['rate'].widget.attrs = {
            'class': 'form-control', 'onchange': 'calcProductTotalPurchase(this)','step': 'any'}
        self.fields['disc'].widget.attrs = {'class': 'form-control','step': 'any','onchange': 'calcProductTotalPurchase(this)' }
        self.fields['total'].widget.attrs = {
            'class': 'form-control', 'onchange': 'calcProductRate(this)','step': 'any'}

    def clean_stock_item(self):
        stock_item = self.cleaned_data['stock_item']
        print(self.company)
        if not stock_item:
            raise forms.ValidationError("Product must be selected")
        return stock_item

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be zero or negative")
        print(quantity)
        return quantity

    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate < 0:
            raise forms.ValidationError("Rate cannot be negative")
        return rate

    def clean_total(self):
        total = self.cleaned_data['total']
        if total < 0:
            raise forms.ValidationError("Sub total cannot be negative")
        return total


class PurchaseStockFormSet(forms.BaseInlineFormSet):

    def clean(self):
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on its own
            return

        form_changed_count = 0

        for form in self.forms:
            if form.has_changed():
                form_changed_count += 1
                # stock_item = form.cleaned_data.get('stock_item', '')
                # if not stock_item:
                #     raise forms.ValidationError("Please choose a product", "error")

        if form.changed_data and form_changed_count == 0:
            raise forms.ValidationError('Provide atleast one stock') #code stops here

PURCHASE_STOCK_FORM_SET = inlineformset_factory(
    PurchaseVoucher,
    PurchaseStock,
    form=PurchaseStockForm,
    formset=PurchaseStockFormSet,
    extra=1,
    min_num=1,
    max_num=100,
    validate_max=True,
    can_delete=True
)




class PurchaseTermForm(forms.ModelForm):
    """
    Purchase Term Form
    """
    class Meta:
        model = PurchaseTerm
        fields = ('ledger', 'rate', 'total')

    def __init__(self, *args, **kwargs):
        self.company = kwargs.pop('company', None)
        super(PurchaseTermForm, self).__init__(*args, **kwargs)

        self.fields['ledger'].queryset = LedgerMaster.objects.filter(
            Q(company=self.company),
            Q(ledger_group__group_base__name__exact='Purchase Accounts') |
            Q(ledger_group__group_base__name__exact='Indirect Expenses') |
            Q(ledger_group__group_base__name__exact='Direct Expenses') |
            Q(ledger_group__group_base__name__exact='Indirect Incomes') |
            Q(ledger_group__group_base__name__exact='Direct Incomes') |
            Q(ledger_group__group_base__name__exact='Fixed Assets'))
        self.fields['ledger'].widget.attrs = {
            'class': 'select2_demo_2 form-control', 'onchange': 'additional_ledger_value(this)'}
        self.fields['rate'].widget.attrs = {
            'class': 'form-control', 'step': 'any','onchange': 'additional_ledger_changed_rate(this)',}
        self.fields['total'].widget.attrs = {
            'class': 'form-control', 'step': 'any'}




PURCHASE_TERM_FORM_SET = inlineformset_factory(
    PurchaseVoucher,
    PurchaseTerm, 
    form=PurchaseTermForm, 
    extra=1,
    min_num=1,
    max_num=100,
    validate_max=True,
    can_delete=True
)


class PurchaseTaxForm(forms.ModelForm):
    """
    Purchase Tax Form
    """
    class Meta:
        model = PurchaseTax
        fields = ('ledger', 'total')

    def __init__(self, *args, **kwargs):
        self.company = kwargs.pop('company', None)
        super(PurchaseTaxForm, self).__init__(*args, **kwargs)

        self.fields['ledger'].queryset = LedgerMaster.objects.filter(
            Q(company=self.company),
            Q(ledger_group__group_base__name__exact='Duties & Taxes'))
        self.fields['ledger'].widget.attrs = {
            'class': 'select2_demo_2 form-control', 'onchange': 'additional_gst_value(this)',}
        self.fields['total'].widget.attrs = {
            'class': 'form-control', 'step': 'any'}


PURCHASE_TAX_FORM_SET = inlineformset_factory(
    PurchaseVoucher, 
    PurchaseTax, 
    form=PurchaseTaxForm, 
    extra=2,
    min_num=1,
    max_num=100,
    validate_max=True,
    can_delete=True
)
