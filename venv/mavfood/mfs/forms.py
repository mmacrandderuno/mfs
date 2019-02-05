from django import forms
from .models import Cust, Service, Product

class CustForm(forms.ModelForm):
    class Meta:
        model = Cust
        fields = ('custdelete','accountno','firstname','lastname','custemail','custphone','custorg','custrole','address',
                  'custbldgroom','city','state','zip','notes')

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('servicedelete','servicecategory','servicedesc','servicelocation','servicedate',
                  'setuptime','cleanuptime','cost')

class ProdForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('productdelete','product','productdesc','productquantity','pickupdate','pickuptime','charge')
        