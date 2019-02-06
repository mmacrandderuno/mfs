from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import CustForm, ProdForm, ServiceForm
from .models import Cust, Product, Service
from django.shortcuts import redirect
from django.views.generic.base import TemplateView # new


def home(request):
    products = Product.objects.filter(productdelete=False).order_by('pickupdate')
    services = Service.objects.filter(servicedelete=False).order_by('servicedate')
    return render(request,'mfs/home.html',({'services': services , 'products': products}))

def cust_list(request):
    custs = Cust.objects.filter(custdelete=False).order_by('lastname','firstname')
    return render(request, 'mfs/cust_list.html', {'custs': custs})

def deleted_customers(request):
    custs = Cust.objects.filter(custdelete=True).order_by('lastname','firstname')
    return render(request, 'mfs/cust_list.html', {'custs': custs})

def cust_detail(request, pk):
    cust = get_object_or_404(Cust, pk=pk)
    return render(request, 'mfs/cust_detail.html', {'cust': cust})

def cust_new(request):
    if request.method == "POST":
        form = CustForm(request.POST)
        if form.is_valid():
            cust = form.save(commit=False)
            cust.custaddedby = request.user
            cust.custadd_date = timezone.now()
            cust.save()
            return redirect('cust_detail', pk=cust.pk)
    else:
        form = CustForm()
    return render(request, 'mfs/cust_new.html', {'form': form})

def prod_new(request, custid):
    cust = get_object_or_404(Cust, pk=custid)
    if request.method == "POST":
        form = ProdForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.custid = cust
            product.prodaddedby = request.user
            product.prodadd_date = timezone.now()
            product.save()
            return redirect('prod_detail', pk=product.pk)
    else:
        form = ProdForm()
    return render(request, 'mfs/prod_new.html', {'form': form,'custid':custid})

def service_new(request, custid):
    cust = get_object_or_404(Cust, pk=custid)
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.custid = cust
            service.servaddedby = request.user
            service.servadd_date = timezone.now()
            service.save()
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm()
    return render(request, 'mfs/service_new.html', {'form': form, 'custid':custid})

def cust_edit(request, pk):
    cust = get_object_or_404(Cust, pk=pk)
    if request.method == "POST":
        form = CustForm(request.POST, instance=cust)
        if form.is_valid():
            cust = form.save(commit=False)
            cust.custupdatedby = request.user
            cust.custupdate_date = timezone.now()
            cust.save()
            return redirect('cust_detail', pk=cust.pk)
    else:
        form = CustForm(instance=cust)
    return render(request, 'mfs/cust_edit.html', {'form': form, 'cust':cust})

def prod_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProdForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.produpdatedby = request.user
            product.produpdate_date = timezone.now()
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProdForm(instance=product)
    return render(request, 'mfs/prod_edit.html', {'form': form, 'product':product})

def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            service = form.save(commit=False)
            service.servupdatedby = request.user
            service.servupdate_date = timezone.now()
            service.save()
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'mfs/service_edit.html', {'form': form, 'service':service})

def orders(request, custid):
    products = Product.objects.filter(custid_id=custid, productdelete = False).order_by('pickupdate')
    services = Service.objects.filter(custid_id=custid, servicedelete = False).order_by('servicedate')
    return render(request, 'mfs/orders.html', ({'services': services , 'products': products,'custid':custid}))

def deletedorders(request, custid):
    products = Product.objects.filter(custid=custid, productdelete = True).order_by('pickupdate')
    services = Service.objects.filter(custid=custid, servicedelete = True).order_by('servicedate')
    return render(request, 'mfs/orders.html', ({'services': services , 'products': products, 'custid':custid}))

def prod_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'mfs/prod_detail.html', {'product': product})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'mfs/service_detail.html', {'service': service})




