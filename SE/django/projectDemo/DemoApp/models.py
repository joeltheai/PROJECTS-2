
# Create your models here.
from django.db import models

# Create your models here.
class bankDetails(models.Model):
    bankname = models.CharField(max_length = 40) 
    address = models.CharField(max_length=40, blank=True, null=True) 
    DoE = models.DateTimeField() #Date of Establishment 
    bankID = models.IntegerField(null=False) 
    url = models.URLField(default='www.rbi.co.in')
    def str (self):
        return (self.bankname)
class bankAccount (models. Model):
    username = models.CharField(max_length=40) 
    mybankname = models.ForeignKey(bankDetails, on_delete = models.CASCADE) # #Create Foreignkey! 
    surname = models.CharField(max_length = 40, blank=True, null=True) 
    emailid = models.EmailField(max_length=40) 
    DOI = models.DateTimeField() #Date of Initiation 
    accnumber = models.IntegerField() 
    url = models.URLField(default='www.google.com')
    def str_(self):
        return (self.username + " account details")