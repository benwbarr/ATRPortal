from django.db import models
from django_matplotlib import MatplotlibFigureField


class Activity(models.Model):
    jobnumber = models.CharField('Job Number', max_length=120)
    refnumber = models.IntegerField('Reference Number')
    rdate = models.DateTimeField('Receiving Date')
    company = models.CharField('Company', max_length=120)
    location = models.CharField('Location', max_length=120)
    quantity = models.IntegerField('Quantity')
    weight = models.IntegerField('Weight')

    def __str__(self):
        return self.jobnumber

class users(models.Model):
    first_name = models.CharField('First Name', max_length=120)
    last_name = models.CharField('Last Name', max_length=120)
    company = models.CharField('Company', max_length=120)
    email = models.EmailField('Email', blank=True)
    phone = models.CharField('Company', max_length=120)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class client_profile(models.Model):
    company_name = models.CharField('Company Name', max_length=120)
    location = models.CharField('Locations', max_length=120)
    job_numbers = models.CharField('Job Numbers', max_length=800)
    reused_quantity = models.IntegerField('Total Reused Quantity')
    recycled_quantity = models.IntegerField('Total Recycled Quantity')
    total_quantity = models.IntegerField('Total Quantity')
    reused_weight = models.IntegerField('Total Reused Weight')
    recycled_weight = models.IntegerField('Total Recycled Weight')
    total_weight = models.IntegerField('Total Weight')
    rdate = models.DateTimeField('Receiving Date')
    totla_recovery = models.IntegerField('Total Recovery')
    freight = models.IntegerField('Freight')
    hd_quantity = models.IntegerField('HD Quantity')
    hd_sanitization = models.IntegerField('HD Sanitization')
    asset_quantity = models.IntegerField('Asset Quantity')
    asset_cost = models.IntegerField('Asset Cost')
    ewaste_fee = models.IntegerField('eWaste Fee')
    other_fees = models.IntegerField('Other Fees')
    total_cost = models.IntegerField('Total Cost')
    balance = models.IntegerField('Balance')

    def __str__(self):
        return self.company_name