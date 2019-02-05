from django.conf import settings
from django.db import models
from django.utils import timezone

class Cust(models.Model):
    accountno = models.IntegerField("Account Number",default=0)
    custdelete = models.BooleanField("Delete",default=False)
    firstname = models.CharField("First Name",max_length=50)
    lastname = models.CharField("Last Name",max_length=50)
    custemail = models.CharField("Customer E-Mail",max_length = 255)
    custphone = models.CharField("Customer Phone",max_length = 15)
    custorg= models.CharField("Customer Organization",max_length = 100)
    custrole = models.CharField("Customer Role",max_length = 100)
    address = models.CharField("Customer Street Address",max_length=50)
    custbldgroom = models.CharField("Customer Building And/Or Room",max_length = 50, blank=True, null=True)
    city = models.CharField("Customer City",max_length = 50)
    state = models.CharField("Customer State",max_length = 2)
    zip = models.CharField("Customer ZIP Code",max_length = 6)
    notes = models.TextField("Customer Notes",blank=True, null=True)
    custadd_date = models.DateTimeField(blank=True, null=True)
    custupdateby = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    custupdate_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        if(add_date is None):
            self.custadd_date = timezone.now()
            self.custupdateby = (settings.AUTH_USER_MODEL)
            self.custupdate_date = timezone.now()
        else:
            self.custupdateby = (settings.AUTH_USER_MODEL)
            self.custupdate_date = timezone.now()
        self.save()

    def __str__(self):
        return ("%s, %s - %s %s" % (self.lastname, self.firstname, self.custorg, self.custrole))

class Service(models.Model):
    servicedelete = models.BooleanField("Delete",default=False)
    custid = models.ForeignKey(Cust,verbose_name="Customer", on_delete = models.PROTECT)
    servicecategory = models.CharField("Service Category",max_length = 100)
    servicedesc = models.TextField("Service Description")
    servicelocation = models.CharField("Service Location",max_length = 100)
    servicedate = models.DateField("Service Date")
    setuptime = models.TimeField("Setup Time")
    cleanuptime = models.TimeField("Cleanup Time")
    cost = models.DecimalField("Service Cost",max_digits = 15, decimal_places = 2)
    servadd_date = models.DateTimeField(blank=True, null=True)
    servupdateby = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    servupdate_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        if(add_date is None):
            self.servadd_date = timezone.now()
            self.servupdateby = (settings.AUTH_USER_MODEL)
            self.servupdate_date = timezone.now()
        else:
            self.servupdateby = (settings.AUTH_USER_MODEL)
            self.servupdate_date = timezone.now()
        self.save()

    def __str__(self):
        return ("%s %s %s" % (str(self.custid), self.servicecategory, str(self.servicedate)))

class Product(models.Model):
    productdelete = models.BooleanField("Delete",default=False)
    custid = models.ForeignKey(Cust, verbose_name="Customer",on_delete = models.PROTECT)
    product = models.CharField("Product Type",max_length = 100)
    productdesc = models.TextField("Product Description",blank=True, null=True)
    productquantity = models.IntegerField("Quantity")
    pickupdate = models.DateField("Pickup Date")
    pickuptime = models.TimeField("Pickup Time (If Applicable)",blank=True,null=True)
    charge = models.DecimalField("Product Cost",max_digits = 15, decimal_places = 2)
    prodadd_date = models.DateTimeField(blank=True, null=True)
    produpdateby = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    produpdate_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        if(add_date is None):
            self.prodadd_date = timezone.now()
            self.produpdateby = (settings.AUTH_USER_MODEL)
            self.produpdate_date = timezone.now()
        else:
            self.produpdateby = (settings.AUTH_USER_MODEL)
            self.produpdate_date = timezone.now()
        self.save()

    def __str__(self):
        return str("%s %s %s" % (str(self.custid), self.product, str(self.pickupdate)))