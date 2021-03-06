"""
Models
"""
import datetime
from django.conf import settings
from django.db import models
from bracketline.models import StateMaster, CountryMaster
from company.models import Company
from accounting_entry.models import LedgerMaster
from .models_sale_accounts import SaleVoucherAccounts
from django.db.models import Value, Sum
from django.db.models.functions import Coalesce



class CreditNoteAccountsVoucher(models.Model):
    """
    Credit Note Voucher For Accounts Only Model
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_credit_note_accounts')
    sale_voucher = models.ForeignKey(SaleVoucherAccounts, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='credit_note_sale_voucher_accounts')
    counter = models.IntegerField()
    url_hash = models.CharField(max_length=100)
    voucher_date = models.DateField(default=datetime.date.today)

    bool_list = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    manual = models.CharField(max_length=100, choices=bool_list, default='No')
    # manual entry field when ref voucher missing and manual value is Yes
    sales_invno = models.CharField(max_length=30, null=True, blank=True)
    sales_date = models.DateField(blank=True, null=True)
    sales_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    ref_no = models.CharField(max_length=100)
    party_ac = models.ForeignKey(LedgerMaster, on_delete=models.DO_NOTHING, related_name='party_ledger_credit_note_accounts')
    supply_place = models.ForeignKey(StateMaster, related_name="credit_note_supply_state_accounts", on_delete=models.DO_NOTHING, null=True, blank=True)

    transaction_types_sales = (
        ('Not Applicable', 'Not Applicable'),
        ('Branch Transfer outward', 'Branch Transfer outward'),
        ('Deemed Exports Exempt', 'Deemed Exports Exempt'),
        ('Deemed Exports Nil Rated', 'Deemed Exports Nil Rated'),
        ('Deemed Exports Taxable', 'Deemed Exports Taxable'),
        ('Exports Exempt', 'Exports Exempt'),
        ('Exports LUT/Bond', 'Exports LUT/Bond'),
        ('Exports Nil Rated', 'Exports Nil Rated'),
        ('Exports Taxable', 'Exports Taxable'),
        ('Interstate Sales Exempt', 'Interstate Sales Exempt'),
        ('Interstate Sales Nil Rated', 'Interstate Sales Nil Rated '),
        ('Interstate Sales - Taxable', 'Interstate Sales   - Taxable'),
        ('Interstate Sales to Embassy / UN Body Exempt',
         'Interstate Sales to Embassy / UN Body Exempt'),
        ('Interstate Sales to Embassy / UN Body Nil Rated',
         'Interstate Sales to Embassy / UN Body Nil Rated'),
        ('Interstate Sales to Embassy / UN Body Taxable',
         'Interstate Sales to Embassy / UN Body Taxable'),
        ('Interstate Deemed Exports Exempt', 'Interstate Deemed Exports Exempt'),
        ('Interstate Deemed Exports Nil Rated',
         'Interstate Deemed Exports Nil Rated'),
        ('Interstate Deemed Exports Taxable',
         'Interstate Deemed Exports Taxable'),
        ('Sales Exempt', 'Sales Exempt'),
        ('Sales Nil Rated', 'Sales Nil Rated'),
        ('Intrastate Sales Taxable', 'Intrastate Sales Taxable'),
        ('Sales to Consumer - Exempt', 'Sales to Consumer - Exempt'),
        ('Sales to Consumer - Nil Rated', 'Sales to Consumer - Nil Rated'),
        ('Sales to Consumer - Taxable', 'Sales to Consumer - Taxable'),
        ('Sales to SEZ - Exempt', 'Sales to SEZ - Exempt'),
        ('Sales to SEZ - LUT/Bond', 'Sales to SEZ - LUT/Bond'),
        ('Sales to SEZ - Nil Rated', 'Sales to SEZ - Nil Rated'),
        ('Sales to SEZ - Taxable', 'Sales to SEZ - Taxable'),
    )
    nature_transactions_sales = models.CharField(max_length=50, choices=transaction_types_sales, default='Not Applicable',blank=True)
    delivery_note = models.CharField(max_length=32, blank=True)
    supplier_ref = models.CharField(max_length=32, blank=True)
    mode = models.TextField(blank=True)
    sub_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    cgst_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    sgst_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    igst_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    cess_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    tax_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    gst_details = models.CharField(max_length=3, choices=bool_list, default='No')
    reason = (
        ('00', 'Not Applicable'),
        ('01', 'Sales Return'),
        ('02', 'Post Sales Discount'),
        ('03', 'Deficiency in services'),
        ('04', 'Correction in Invoices'),
        ('05', 'Change in POS'),
        ('06', 'Finalisation of provisional assessment'),
        ('07', 'Others'),
    )
    issue_reason = models.CharField(max_length=3, choices=reason, default='00')
    note_no = models.CharField(max_length=32, blank=True)
    date_after_no = models.DateField(default=datetime.date.today)
    bill_no = models.CharField(max_length=32, blank=True)
    bill_date = models.DateField(default=datetime.date.today,blank=True)
    port_code = models.CharField(max_length=32, blank=True)

    despatch_no = models.CharField(max_length=132, blank=True)
    despatch_info = models.CharField(max_length=132, blank=True)
    destination = models.CharField(max_length=132, blank=True)
    landing_bill = models.CharField(max_length=132, blank=True)
    landing_date = models.DateField(default=datetime.date.today)
    vechicle_no = models.CharField(max_length=132, blank=True)

    shipper_place = models.TextField(blank=True)
    flight_no = models.CharField(max_length=20, blank=True)
    loading_port = models.CharField(max_length=50, blank=True)
    discharge_port = models.CharField(max_length=50, blank=True)
    supply_country = models.ForeignKey(
        CountryMaster, default=12, related_name="credit_note_supply_country_accounts", on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return str(self.party_ac)

    def save(self, **kwargs):
        tax_total = self.credit_note_gst_accounts.aggregate(
        the_sum=Coalesce(Sum('total'), Value(0)))['the_sum']
        extra_total = self.credit_note_term_accounts.aggregate(
            the_sum=Coalesce(Sum('total'), Value(0)))['the_sum']

        if tax_total or extra_total:
            self.total = tax_total + extra_total
            self.sub_total = extra_total

        total_cgst_extra = self.credit_note_term_accounts.aggregate(
        the_sum=Coalesce(Sum('cgst_total'), Value(0)))['the_sum']
        total_sgst_extra = self.credit_note_term_accounts.aggregate(
            the_sum=Coalesce(Sum('sgst_total'), Value(0)))['the_sum']
        total_igst_extra = self.credit_note_term_accounts.aggregate(
            the_sum=Coalesce(Sum('igst_total'), Value(0)))['the_sum']

        if not total_cgst_extra:
            total_cgst_extra = 0

        if not total_sgst_extra:
            total_sgst_extra = 0

        if not total_igst_extra:
            total_igst_extra = 0

        self.cgst_total = total_cgst_extra

        self.sgst_total = total_sgst_extra
        
        self.igst_total = total_igst_extra

        if not self.url_hash:
            if self.user.profile.user_type == 'Bussiness user':
                self.url_hash = 'BU' + '-' + str(self.user.id) + '-' + 'P' + '-' + '1' + '-' + 'C' + str(
                    self.company.counter) + '-' + ('SP') + str(self.counter)
            else:
                self.url_hash = 'PU' + '-' + str(self.user.id) + '-' + 'P' + '-' + '1' + '-' + 'C' + str(
                    self.company.counter) + '-' + ('SP') + str(self.counter)

        super(CreditNoteAccountsVoucher, self).save()


class CreditNoteAccountsTerm(models.Model):
    """
    Credit Note Term For Accounts Only Model
    """
    credit_note = models.ForeignKey(CreditNoteAccountsVoucher, on_delete=models.CASCADE, related_name='credit_note_term_accounts')
    ledger = models.ForeignKey(LedgerMaster, on_delete=models.DO_NOTHING, related_name='credit_note_term_ledger_accounts')
    tax = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)  # composite tax percent
    cgst = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    sgst = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    igst = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    cess = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    cgst_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    sgst_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    igst_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    cess_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    tax_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.ledger)

    def save(self, **kwargs):
        """
        Save function to override the total value of particular ledger and their GST Totals
        """

        if self.ledger:
            if self.credit_note.company.gst_registration_type == 'Regular':
                if self.credit_note.nature_transactions_sales == 'Not Applicable':
                    if self.ledger.nature_transactions_sales == 'Intrastate Deemed Exports Taxable':
                        if self.ledger.central_tax != 0 or self.ledger.state_tax != 0:
                            self.cgst = self.ledger.central_tax
                            self.sgst = self.ledger.state_tax
                            self.igst = 0

                        else:
                            self.cgst = self.credit_note.company.central_tax
                            self.sgst = self.credit_note.company.state_tax
                            self.igst = 0

                    elif self.ledger.nature_transactions_sales == 'Intrastate Sales Taxable':
                        if self.ledger.central_tax != 0 or self.ledger.state_tax != 0:
                            self.cgst = self.ledger.central_tax
                            self.sgst = self.ledger.state_tax
                            self.igst = 0

                        else:
                            self.cgst = self.credit_note.company.central_tax
                            self.sgst = self.credit_note.company.state_tax
                            self.igst = 0

                    elif self.ledger.nature_transactions_sales == 'sales to Consumer - Taxable':
                        if self.ledger.central_tax != 0 or self.ledger.state_tax != 0:
                            self.cgst = self.ledger.central_tax
                            self.sgst = self.ledger.state_tax
                            self.igst = 0
                        else:
                            self.cgst = self.credit_note.company.central_tax
                            self.sgst = self.credit_note.company.state_tax
                            self.igst = 0
                    elif self.ledger.nature_transactions_sales == 'Deemed Exports Taxable':
                        if self.ledger.integrated_tax != 0:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.ledger.integrated_tax
                        else:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.credit_note.company.integrated_tax
                    elif self.ledger.nature_transactions_sales == 'Exports Taxable':
                        if self.ledger.integrated_tax != 0:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.ledger.integrated_tax
                        else:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.credit_note.company.integrated_tax
                    elif self.ledger.nature_transactions_sales == 'Interstate Sales - Taxable':
                        if self.ledger.integrated_tax != 0:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.ledger.integrated_tax
                        else:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.credit_note.company.integrated_tax
                    elif self.ledger.nature_transactions_sales == 'Interstate Sales to Embassy / UN Body Taxable':
                        if self.ledger.integrated_tax != 0:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.ledger.integrated_tax

                        else:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.credit_note.company.integrated_tax
                    elif self.ledger.nature_transactions_sales == 'Sales to SEZ - Taxable':
                        if self.ledger.integrated_tax != 0:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.ledger.integrated_tax
                        else:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.credit_note.company.integrated_tax
                    else:
                        self.cgst = 0
                        self.igst = 0
                        self.sgst = 0
                        self.sgst = 0
                else:
                    if self.credit_note.nature_transactions_sales == 'Intrastate Deemed Exports Taxable':
                        if self.ledger.central_tax != 0 or self.ledger.state_tax != 0:
                            self.cgst = self.ledger.central_tax
                            self.sgst = self.ledger.state_tax
                            self.igst = 0

                        else:
                            self.cgst = self.credit_note.company.central_tax
                            self.sgst = self.credit_note.company.state_tax
                            self.igst = 0

                    elif self.credit_note.nature_transactions_sales == 'Intrastate Sales Taxable':
                        if self.ledger.central_tax != 0 or self.ledger.state_tax != 0:
                            self.cgst = self.ledger.central_tax
                            self.sgst = self.ledger.state_tax
                            self.igst = 0

                        else:
                            self.cgst = self.credit_note.company.central_tax
                            self.sgst = self.credit_note.company.state_tax
                            self.igst = 0

                    elif self.credit_note.nature_transactions_sales == 'sales to Consumer - Taxable':
                        if self.ledger.central_tax != 0 or self.ledger.state_tax != 0:
                            self.cgst = self.ledger.central_tax
                            self.sgst = self.ledger.state_tax
                            self.igst = 0
                        else:
                            self.cgst = self.credit_note.company.central_tax
                            self.sgst = self.credit_note.company.state_tax
                            self.igst = 0
                    elif self.credit_note.nature_transactions_sales == 'Deemed Exports Taxable':
                        if self.ledger.integrated_tax != 0:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.ledger.integrated_tax
                        else:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.credit_note.company.integrated_tax
                    elif self.credit_note.nature_transactions_sales == 'Exports Taxable':
                        if self.ledger.integrated_tax != 0:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.ledger.integrated_tax
                        else:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.credit_note.company.integrated_tax
                    elif self.credit_note.nature_transactions_sales == 'Interstate Sales - Taxable':
                        if self.ledger.integrated_tax != 0:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.ledger.integrated_tax
                        else:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.credit_note.company.integrated_tax
                    elif self.credit_note.nature_transactions_sales == 'Interstate Sales to Embassy / UN Body Taxable':
                        if self.ledger.integrated_tax != 0:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.ledger.integrated_tax

                        else:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.credit_note.company.integrated_tax
                    elif self.credit_note.nature_transactions_sales == 'Sales to SEZ - Taxable':
                        if self.ledger.integrated_tax != 0:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.ledger.integrated_tax
                        else:
                            self.cgst = 0
                            self.sgst = 0
                            self.igst = self.credit_note.company.integrated_tax
                    else:
                        self.cgst = 0
                        self.igst = 0
                        self.sgst = 0
                        self.sgst = 0

            else:
                self.tax = self.ledger.integrated_tax

        if self.ledger: 
            if self.credit_note.company.gst_registration_type == 'Regular':
                if self.credit_note.nature_transactions_sales == 'Not Applicable':
                    if self.ledger.nature_transactions_sales == 'Intrastate Deemed Exports Taxable':
                        self.cgst_total = self.cgst * self.total / 100
                        self.sgst_total = self.sgst * self.total / 100

                    elif self.ledger.nature_transactions_sales == 'Intrastate Sales Taxable':
                        self.cgst_total = self.cgst * self.total / 100
                        self.sgst_total = self.sgst * self.total / 100

                    elif self.ledger.nature_transactions_sales == 'sales to Consumer - Taxable':
                        self.cgst_total = self.cgst * self.total / 100
                        self.sgst_total = self.sgst * self.total / 100

                    elif self.ledger.nature_transactions_sales == 'Deemed Exports Taxable':
                        self.cgst_total = 0
                        self.sgst_total = 0
                        self.igst_total = self.igst * self.total / 100

                    elif self.ledger.nature_transactions_sales == 'Exports Taxable':
                        self.cgst_total = 0
                        self.sgst_total = 0
                        self.igst_total = self.igst * self.total / 100

                    elif self.ledger.nature_transactions_sales == 'Interstate Sales - Taxable':
                        self.cgst_total = 0
                        self.sgst_total = 0
                        self.igst_total = self.igst * self.total / 100

                    elif self.ledger.nature_transactions_sales == 'Interstate Sales to Embassy / UN Body Taxable':
                        self.cgst_total = 0
                        self.sgst_total = 0
                        self.igst_total = self.igst * self.total / 100

                    elif self.ledger.nature_transactions_sales == 'Sales to SEZ - Taxable':
                        self.cgst_total = 0
                        self.sgst_total = 0
                        self.igst_total = self.igst * self.total / 100
                    else:
                        self.igst_total = self.igst * self.total / 100
                else:
                    if self.credit_note.nature_transactions_sales == 'Intrastate Deemed Exports Taxable':
                        self.cgst_total = self.cgst * self.total / 100
                        self.sgst_total = self.sgst * self.total / 100

                    elif self.credit_note.nature_transactions_sales == 'Intrastate Sales Taxable':
                        self.cgst_total = self.cgst * self.total / 100
                        self.sgst_total = self.sgst * self.total / 100

                    elif self.credit_note.nature_transactions_sales == 'sales to Consumer - Taxable':
                        self.cgst_total = self.cgst * self.total / 100
                        self.sgst_total = self.sgst * self.total / 100

                    elif self.credit_note.nature_transactions_sales == 'Deemed Exports Taxable':
                        self.cgst_total = 0
                        self.sgst_total = 0
                        self.igst_total = self.igst * self.total / 100

                    elif self.credit_note.nature_transactions_sales == 'Exports Taxable':
                        self.cgst_total = 0
                        self.sgst_total = 0
                        self.igst_total = self.igst * self.total / 100

                    elif self.credit_note.nature_transactions_sales == 'Interstate Sales - Taxable':
                        self.cgst_total = 0
                        self.sgst_total = 0
                        self.igst_total = self.igst * self.total / 100

                    elif self.credit_note.nature_transactions_sales == 'Interstate Sales to Embassy / UN Body Taxable':
                        self.cgst_total = 0
                        self.sgst_total = 0
                        self.igst_total = self.igst * self.total / 100

                    elif self.credit_note.nature_transactions_sales == 'Sales to SEZ - Taxable':
                        self.cgst_total = 0
                        self.sgst_total = 0
                        self.igst_total = self.igst * self.total / 100
                    else:
                        self.igst_total = self.igst * self.total / 100

            else:
                self.tax_total = self.tax * self.total / 100
        super(CreditNoteAccountsTerm, self).save()


class CreditNoteAccountTax(models.Model):
    """
    Credit Note Tax For Accounts Only Model
    """
    credit_note = models.ForeignKey(CreditNoteAccountsVoucher, on_delete=models.CASCADE, related_name='credit_note_gst_accounts')
    ledger = models.ForeignKey(LedgerMaster, on_delete=models.DO_NOTHING, related_name='credit_note_tax_ledger_accounts')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.ledger)

    def save(self, **kwargs):
        """
        Save method to override the total value as per the ledger Selected in a voucher
        """
        if self.ledger:
            if self.ledger.tax_type == 'Central Tax':
                self.total = self.credit_note.cgst_total
            elif self.ledger.tax_type == 'State Tax':
                self.total = self.credit_note.sgst_total
            elif self.ledger.tax_type == 'Integrated Tax':
                self.total = self.credit_note.igst_total
            else:
                self.total = self.credit_note.cess_total
        super(CreditNoteAccountTax, self).save()
