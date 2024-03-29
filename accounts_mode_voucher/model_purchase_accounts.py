"""
Models
"""
import datetime
from django.conf import settings
from django.db.models import Value, Sum
from django.db.models.functions import Coalesce
from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
from bracketline.models import StateMaster, CountryMaster
from company.models import Company
from accounting_entry.models import LedgerMaster, PeriodSelected


class PurchaseVoucherAccounts(models.Model):
    """
    Purchase Voucher Model
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='company_purchase_accounts')
    counter = models.IntegerField()
    url_hash = models.CharField(max_length=100)
    voucher_date = models.DateField(default=datetime.date.today)
    ref_no = models.CharField(max_length=100)
    party_ac = models.ForeignKey(
        LedgerMaster, on_delete=models.DO_NOTHING, related_name='party_ledger_purchase_accounts')
    consignee_name = models.CharField(
        max_length=200, default='Customer', blank=True)
    consignee_address = models.TextField(blank=True)
    consignee_gstin = models.CharField(max_length=15, blank=True)
    consignee_pan = models.CharField(max_length=15, blank=True)
    consignee_contact = models.CharField(max_length=15, blank=True)
    consignee_state = models.ForeignKey(
        StateMaster, related_name="purchase_consignee_state_accounts", on_delete=models.DO_NOTHING, blank=True, null=True)
    consignee_country = models.ForeignKey(
        CountryMaster, default=12, related_name="purchase_consignee_country_accounts", on_delete=models.DO_NOTHING, blank=True)
    supply_state = models.ForeignKey(
        StateMaster, related_name="purchase_supply_state_accounts", on_delete=models.DO_NOTHING, blank=True, null=True)
    supply_country = models.ForeignKey(
        CountryMaster, default=12, related_name="purchase_supply_country_accounts", on_delete=models.DO_NOTHING, blank=True)
    other_details = models.CharField(max_length=100, blank=True)
    transaction_types = (
        ('Not Applicable', 'Not Applicable'),
        ('Branch Transfer Inward', 'Branch Transfer Inward'),
        ('Imports Exempt', 'Imports Exempt'),
        ('Imports Nil Rated', 'Imports Nil Rated'),
        ('Imports Taxable', 'Imports Taxable'),
        ('Interstate Purchase Exempt', 'Interstate Purchase Exempt'),
        ('Interstate Purchase from Unregistered Dealer - Exempt',
         'Interstate Purchase from Unregistered Dealer - Exempt'),
        ('Interstate Purchase from Unregistered Dealer - Nil Rated',
         'Interstate Purchase from Unregistered Dealer - Nil Rated'),
        ('Interstate Purchase from Unregistered Dealer - Services',
         'Interstate Purchase from Unregistered Dealer - Services'),
        ('Interstate Purchase from Unregistered Dealer - Taxable',
         'Interstate Purchase from Unregistered Dealer - Taxable'),
        ('Interstate Purchase - Nil Rated',
         'Interstate Purchase  - Nil Rated '),
        ('Interstate Purchase - Taxable', 'Interstate Purchase  - Taxable'),
        ('Interstate Purchase Deemed Exports - Exempt',
         'Interstate Purchase Deemed Exports - Exempt'),
        ('Interstate Purchase Deemed Exports - Nil Rated',
         'Interstate Purchase Deemed Exports - Nil Rated'),
        ('Interstate Purchase Deemed Exports - Taxable',
         'Interstate Purchase Deemed Exports - Taxable'),
        ('Purchase Deemed Exports - Exempt',
         'Purchase Deemed Exports - Exempt'),
        ('Purchase Deemed Exports - Nil Rated',
         'Purchase Deemed Exports - Nil Rated'),
        ('Purchase Deemed Exports - Taxable',
         'Purchase Deemed Exports - Taxable'),
        ('Purchase Exempt', 'Purchase Exempt'),
        ('Purchase From Composition Dealer',
         'Purchase From Composition Dealer'),
        ('Purchase From SEZ - Exempt', 'Purchase From SEZ - Exempt'),
        ('Purchase From SEZ - LUT/Bond', 'Purchase From SEZ - LUT/Bond'),
        ('Purchase From SEZ - Nil Rated ', 'Purchase From SEZ - Nil Rated'),
        ('Purchase From SEZ - Taxable', 'Purchase From SEZ - Taxable'),
        ('Purchase From SEZ (Without Bill Of Entry) - Exempt',
         'Purchase From SEZ (Without Bill Of Entry) - Exempt'),
        ('Purchase From SEZ (Without Bill Of Entry) - Nil Rated',
         'Purchase From SEZ (Without Bill Of Entry) - Nil Rated'),
        ('Purchase From SEZ (Without Bill Of Entry) - Taxable',
         'Purchase From SEZ (Without Bill Of Entry) - Taxable'),
        ('Purchase From Unregister Dealer - Exempt',
         'Purchase From Unregister Dealer - Exempt'),
        ('Purchase From Unregister Dealer - Nil Rated',
         'Purchase From Unregister Dealer - Nil Rated'),
        ('Purchase From Unregister Dealer - Taxable',
         'Purchase From Unregister Dealer - Taxable'),
        ('Purchase Nil Rated', 'Purchase Nil Rated'),
        ('Intrastate Purchase Taxable', 'Intrastate Purchase Taxable'),
    )
    nature_transactions_purchase = models.CharField(
        max_length=100, choices=transaction_types, default='Not Applicable',blank=True)
    receipt_no = models.CharField(max_length=132, blank=True)
    despatch_info = models.CharField(max_length=132, blank=True)
    destination = models.CharField(max_length=132, blank=True)
    delivery_terms = models.TextField(blank=True)
    delivery_note = models.CharField(max_length=32, blank=True)
    supplier_ref = models.CharField(max_length=32, blank=True)
    sub_total = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    cgst_total = models.DecimalField(
        default=0, max_digits=20, decimal_places=2)
    sgst_total = models.DecimalField(
        default=0, max_digits=20, decimal_places=2)
    igst_total = models.DecimalField(
        default=0, max_digits=20, decimal_places=2)
    cess_total = models.DecimalField(
        default=0, max_digits=20, decimal_places=2)
    tax_total = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    shipper_place = models.CharField(max_length=132, blank=True)
    flight_no = models.CharField(max_length=132, blank=True)
    loading_port = models.CharField(max_length=132, blank=True)
    discharge_port = models.CharField(max_length=132, blank=True)
    to_country = models.ForeignKey(
        CountryMaster, default=12, related_name="purchase_to_country_accounts", on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return str(self.ref_no)

    def get_absolute_url(self, **kwargs):
        """
        Get the absolute URL
        """
        company = get_object_or_404(Company, pk=self.kwargs['company_pk'])
        period_selected = get_object_or_404(
            PeriodSelected, pk=kwargs['period_pk'])
        return reverse("stock_keeping:purchasedetail", kwargs={'purchase_voucher_pk': self.pk, 'company_pk': company.pk, 'period_pk': period_selected.pk})

    def save(self, **kwargs):
        tax_total = self.purchase_voucher_tax_accounts.aggregate(
            the_sum=Coalesce(Sum('total'), Value(0)))['the_sum']
        extra_total = self.purchase_voucher_term_accounts.aggregate(
            the_sum=Coalesce(Sum('total'), Value(0)))['the_sum']
        if tax_total or extra_total:
            self.total = tax_total + extra_total
            self.sub_total = extra_total

        total_cgst_extra = self.purchase_voucher_term_accounts.aggregate(
        the_sum=Coalesce(Sum('cgst_total'), Value(0)))['the_sum']
        total_sgst_extra = self.purchase_voucher_term_accounts.aggregate(
            the_sum=Coalesce(Sum('sgst_total'), Value(0)))['the_sum']
        total_igst_extra = self.purchase_voucher_term_accounts.aggregate(
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
                    self.company.counter) + '-' + ('PV') + str(self.counter)
            else:
                self.url_hash = 'PU' + '-' + str(self.user.id) + '-' + 'P' + '-' + '1' + '-' + 'C' + str(
                    self.company.counter) + '-' + ('PV') + str(self.counter)
        super(PurchaseVoucherAccounts, self).save()



class PurchaseTermAccounts(models.Model):
    """
    Purchase Term Model
    """
    purchase_voucher = models.ForeignKey(
        PurchaseVoucherAccounts, on_delete=models.CASCADE, related_name='purchase_voucher_term_accounts')
    ledger = models.ForeignKey(
        LedgerMaster, on_delete=models.CASCADE, related_name='purchase_term_ledger_accounts')
    rate = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    tax = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    cgst = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    sgst = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    igst = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    cess = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    cgst_total = models.DecimalField(
        max_digits=20, decimal_places=2, default=0.00)
    sgst_total = models.DecimalField(
        max_digits=20, decimal_places=2, default=0.00)
    igst_total = models.DecimalField(
        max_digits=20, decimal_places=2, default=0.00)
    cess_total = models.DecimalField(
        max_digits=20, decimal_places=2, default=0.00)
    tax_total = models.DecimalField(
        max_digits=20, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00,blank=True)

    def __str__(self):
        return str(self.ledger)

    def save(self, **kwargs):
        if not self.total:
            self.total = 0

        if self.ledger:
            if self.ledger.ledger_group.group_base.name != 'Direct Incomes' and self.ledger.ledger_group.group_base.name != 'Indirect Incomes' and self.ledger.ledger_group.group_base.name != 'Sales Accounts':     
                if self.purchase_voucher.company.gst_registration_type == 'Regular':
                    if self.purchase_voucher.nature_transactions_purchase == 'Not Applicable':
                        if self.ledger.nature_transactions_purchase == 'Purchase Deemed Exports - Taxable':
                            if self.ledger.central_tax != 0 or self.ledger.state_tax != 0:
                                self.cgst = self.ledger.central_tax
                                self.sgst = self.ledger.state_tax
                                self.igst = 0

                            else:
                                self.cgst = self.purchase_voucher.company.central_tax
                                self.sgst = self.purchase_voucher.company.state_tax
                                self.igst = 0

                        elif self.ledger.nature_transactions_purchase == 'Intrastate Purchase Taxable':
                            if self.ledger.central_tax != 0 or self.ledger.state_tax != 0:
                                self.cgst = self.ledger.central_tax
                                self.sgst = self.ledger.state_tax
                                self.igst = 0

                            else:
                                self.cgst = self.purchase_voucher.company.central_tax
                                self.sgst = self.purchase_voucher.company.state_tax
                                self.igst = 0

                        elif self.ledger.nature_transactions_purchase == 'Interstate Purchase Deemed Exports - Taxable':
                            print('Deemed')
                            if self.ledger.integrated_tax != 0:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.ledger.integrated_tax

                            else:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.purchase_voucher.company.integrated_tax

                        elif self.ledger.nature_transactions_purchase == 'Interstate Purchase - Taxable':
                            if self.ledger.integrated_tax != 0:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.ledger.integrated_tax

                            else:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.purchase_voucher.company.integrated_tax

                        elif self.ledger.nature_transactions_purchase == 'Purchase From SEZ (Without Bill Of Entry) - Taxable':
                            if self.ledger.integrated_tax != 0:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.ledger.integrated_tax

                            else:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.purchase_voucher.company.integrated_tax

                        elif self.ledger.nature_transactions_purchase == 'Purchase From SEZ - Taxable':
                            if self.ledger.integrated_tax != 0:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.ledger.integrated_tax

                            else:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.purchase_voucher.company.integrated_tax


                        else:
                            self.cgst = 0
                            self.igst = 0
                            self.sgst = 0

                    else:
                        if self.purchase_voucher.nature_transactions_purchase == 'Purchase Deemed Exports - Taxable':
                            if self.ledger.central_tax != 0 or self.ledger.state_tax != 0:
                                self.cgst = self.ledger.central_tax
                                self.sgst = self.ledger.state_tax
                                self.igst = 0

                            else:
                                self.cgst = self.purchase_voucher.company.central_tax
                                self.sgst = self.purchase_voucher.company.state_tax
                                self.igst = 0

                        elif self.purchase_voucher.nature_transactions_purchase == 'Intrastate Purchase Taxable':
                            if self.ledger.central_tax != 0 or self.ledger.state_tax != 0:
                                self.cgst = self.ledger.central_tax
                                self.sgst = self.ledger.state_tax
                                self.igst = 0

                            else:
                                self.cgst = self.purchase_voucher.company.central_tax
                                self.sgst = self.purchase_voucher.company.state_tax
                                self.igst = 0

                        elif self.purchase_voucher.nature_transactions_purchase == 'Interstate Purchase Deemed Exports - Taxable':
                            print('Deemed Tax')
                            if self.ledger.integrated_tax != 0:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.ledger.integrated_tax
                                print(self.igst)
                            else:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.purchase_voucher.company.integrated_tax

                        elif self.purchase_voucher.nature_transactions_purchase == 'Interstate Purchase - Taxable':
                            if self.ledger.integrated_tax != 0:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.ledger.integrated_tax

                            else:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.purchase_voucher.company.integrated_tax

                        elif self.purchase_voucher.nature_transactions_purchase == 'Purchase From SEZ (Without Bill Of Entry) - Taxable':
                            if self.ledger.integrated_tax != 0:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.ledger.integrated_tax

                            else:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.purchase_voucher.company.integrated_tax

                        elif self.purchase_voucher.nature_transactions_purchase == 'Purchase From SEZ - Taxable':
                            if self.ledger.integrated_tax != 0:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.ledger.integrated_tax

                            else:
                                self.cgst = 0
                                self.sgst = 0
                                self.igst = self.purchase_voucher.company.integrated_tax
                        

                        else:
                            self.cgst = 0
                            self.igst = 0
                            self.sgst = 0
                else:
                    self.tax = self.ledger.integrated_tax

        if self.ledger:
            if self.ledger.ledger_group.group_base.name != 'Direct Incomes' and self.ledger.ledger_group.group_base.name != 'Indirect Incomes' and self.ledger.ledger_group.group_base.name != 'Sales Accounts':
                if self.purchase_voucher.company.gst_registration_type == 'Regular':
                    if self.purchase_voucher.nature_transactions_purchase == 'Not Applicable':
                        if self.ledger.nature_transactions_purchase == 'Purchase Deemed Exports - Taxable':
                            self.cgst_total = self.cgst * self.total / 100
                            self.sgst_total = self.sgst * self.total / 100

                        elif self.ledger.nature_transactions_purchase == 'Intrastate Purchase Taxable':
                            self.cgst_total = self.cgst * self.total / 100
                            self.sgst_total = self.sgst * self.total / 100

                        elif self.ledger.nature_transactions_purchase == 'Interstate Purchase Deemed Exports - Taxable':
                            print('Deemed total')
                            self.cgst_total = 0
                            self.sgst_total = 0
                            self.igst_total = self.igst * self.total / 100
                            
                        elif self.ledger.nature_transactions_purchase == 'Imports Taxable':
                            self.cgst_total = 0
                            self.sgst_total = 0
                            self.igst_total = 0

                        elif self.ledger.nature_transactions_purchase == 'Interstate Purchase - Taxable':
                            self.cgst_total = 0
                            self.sgst_total = 0
                            self.igst_total = self.igst * self.total / 100

                        elif self.ledger.nature_transactions_purchase == 'Purchase From SEZ (Without Bill Of Entry) - Taxable':
                            self.cgst_total = 0
                            self.sgst_total = 0
                            self.igst_total = self.igst * self.total / 100

                        elif self.ledger.nature_transactions_purchase == 'Purchase From SEZ - Taxable':
                            self.cgst_total = 0
                            self.sgst_total = 0
                            self.igst_total = self.igst * self.total / 100
                        else:
                            self.igst_total = self.igst * self.total / 100
                    else:
                        if self.purchase_voucher.nature_transactions_purchase == 'Purchase Deemed Exports - Taxable':
                            self.cgst_total = self.cgst * self.total / 100
                            self.sgst_total = self.sgst * self.total / 100

                        elif self.purchase_voucher.nature_transactions_purchase == 'Intrastate Purchase Taxable':
                            self.cgst_total = self.cgst * self.total / 100
                            self.sgst_total = self.sgst * self.total / 100

                        elif self.purchase_voucher.nature_transactions_purchase == 'Interstate Purchase Deemed Exports - Taxable':
                            print('Not deemed total')
                            self.cgst_total = 0
                            self.sgst_total = 0
                            self.igst_total = self.igst * self.total / 100
                            print(self.igst_total)
                        elif self.purchase_voucher.nature_transactions_purchase == 'Imports Taxable':
                            self.cgst_total = 0
                            self.sgst_total = 0
                            self.igst_total = 0

                        elif self.purchase_voucher.nature_transactions_purchase == 'Interstate Purchase - Taxable':
                            self.cgst_total = 0
                            self.sgst_total = 0
                            self.igst_total = self.igst * self.total / 100

                        elif self.purchase_voucher.nature_transactions_purchase == 'Purchase From SEZ (Without Bill Of Entry) - Taxable':
                            self.cgst_total = 0
                            self.sgst_total = 0
                            self.igst_total = self.igst * self.total / 100

                        elif self.purchase_voucher.nature_transactions_purchase == 'Purchase From SEZ - Taxable':
                            self.cgst_total = 0
                            self.sgst_total = 0
                            self.igst_total = self.igst * self.total / 100
                        else:
                            self.igst_total = self.igst * self.total / 100
                else:
                    self.tax_total = self.tax * self.total / 100

        super(PurchaseTermAccounts, self).save()


class PurchaseTaxAccounts(models.Model):
    """
    Purchase Tax Model
    """
    purchase_voucher = models.ForeignKey(PurchaseVoucherAccounts, on_delete=models.CASCADE, related_name='purchase_voucher_tax_accounts')
    ledger = models.ForeignKey(LedgerMaster, on_delete=models.DO_NOTHING, related_name='purchase_tax_ledger_accounts')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.ledger)

    def save(self, **kwargs):
        """
        Save method to override the total value as per the ledger Selected in a voucher
        """
        if self.ledger:
            if self.ledger.tax_type == 'Central Tax':
                self.total = self.purchase_voucher.cgst_total
            elif self.ledger.tax_type == 'State Tax':
                self.total = self.purchase_voucher.sgst_total
            elif self.ledger.tax_type == 'Integrated Tax':
                self.total = self.purchase_voucher.igst_total
            else:
                self.total = self.purchase_voucher.cess_total

        super(PurchaseTaxAccounts, self).save()
