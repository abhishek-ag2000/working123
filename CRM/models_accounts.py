import arrow
from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _

# from common.models import User
from django.conf import settings    #import user
from company.models import Company  #import company
from CRMcommon.utils import INDCHOICES, COUNTRIES

#from common.models import User
from CRMcommon.utils import INDCHOICES, COUNTRIES
# from .models_leads import Lead
from .models import Tags

from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify
from .models_contacts import Contact
from bracketline.models import CountryMaster, StateMaster 


class Account(models.Model):

    ACCOUNT_STATUS_CHOICE = (
        ("open", "Open"),
        ('close', 'Close')
    )
    # adding company details
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_accounts')

    # adding user
    created_by = models.ForeignKey(
            settings.AUTH_USER_MODEL, related_name='account_created_by',
            on_delete=models.SET_NULL, null=True)
    assigned_to = models.ManyToManyField(
            settings.AUTH_USER_MODEL, related_name='account_assigned_users')




    name = models.CharField(pgettext_lazy(
        "Name of Account", "Name"), max_length=64)
    email = models.EmailField()
    phone = PhoneNumberField(null=True)
    industry = models.CharField(
        _("Industry Type"),
        max_length=255, choices=INDCHOICES,
        blank=True, null=True)
    # billing_address = models.ForeignKey(
    #     Address, related_name='account_billing_address', on_delete=models.CASCADE, blank=True, null=True)
    # shipping_address = models.ForeignKey(
    #     Address, related_name='account_shipping_address', on_delete=models.CASCADE, blank=True, null=True)
    billing_address_line = models.CharField(
        _("Address"), max_length=255, blank=True, null=True)
    billing_street = models.CharField(
        _("Street"), max_length=55, blank=True, null=True)
    billing_city = models.CharField(
        _("City"), max_length=255, blank=True, null=True)
    billing_accounts_state = models.ForeignKey(StateMaster, on_delete=models.DO_NOTHING, related_name='account_state',blank=True, null=True)
    billing_postcode = models.CharField(
        _("Post/Zip-code"), max_length=64, blank=True, null=True)
    billing_accounts_country =  models.ForeignKey(CountryMaster, on_delete=models.DO_NOTHING, default=12, related_name="account_country",blank=True, null=True)
    website = models.URLField(_("Website"), blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, blank=True)
    status = models.CharField(
        choices=ACCOUNT_STATUS_CHOICE, max_length=64, default='open')
    # lead = models.ForeignKey(
    #     Lead, related_name="account_leads",
    #     on_delete=models.SET_NULL, null=True)
    contact_name = models.CharField(pgettext_lazy(
        "Name of Contact", "Contact Name"), max_length=120)
    contacts = models.ManyToManyField(
        Contact, related_name="account_contacts")
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_on']

    def get_complete_address(self):
        address = ""
        if self.billing_address_line:
            address += self.billing_address_line
        if self.billing_street:
            if address:
                address += ", " + self.billing_street
            else:
                address += self.billing_street
        if self.billing_city:
            if address:
                address += ", " + self.billing_city
            else:
                address += self.billing_city
        # if self.billing_accounts_state:
        #     if address:
        #         address += ", " + self.billing_accounts_state
        #     else:
        #         address += self.billing_accounts_state
        if self.billing_postcode:
            if address:
                address += ", " + self.billing_postcode
            else:
                address += self.billing_postcode
        # if self.billing_accounts_country:
        #     if address:
        #         address += ", " + self.get_billing_country_display()
        #     else:
        #         address += self.get_billing_country_display()
        return address

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()

    @property
    def contact_values(self):
        contacts = list(self.contacts.values_list('id', flat=True))
        return ','.join(str(contact) for contact in contacts)


class Email(models.Model):
    from_account = models.ForeignKey(
        Account, related_name='sent_email', on_delete=models.SET_NULL, null=True)
    # recipients = models.ManyToManyField(Contact, related_name='recieved_email')
    message_subject = models.TextField(null=True)
    message_body = models.TextField(null=True)
    timezone = models.CharField(max_length=100, default='UTC')
    scheduled_date_time = models.DateTimeField(null=True)
    scheduled_later = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    from_email = models.EmailField()
    rendered_message_body = models.TextField(null=True)


    def __str__(self):
        return self.message_subject



class EmailLog(models.Model):
    """ this model is used to track if the email is sent or not """

    # email = models.ForeignKey(Email, related_name='email_log', on_delete=models.SET_NULL, null=True)
    # contact = models.ForeignKey(Contact, related_name='contact_email_log', on_delete=models.SET_NULL, null=True)
    is_sent = models.BooleanField(default=False)