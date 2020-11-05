from django.shortcuts import render,get_object_or_404,redirect
from admin1.models import *
from .models import *
from .forms import OrderForm
from datetime import datetime
import math 
from django.db.models import Q
def index(request):
    PAGE_SIZE = 6
    page = int(request.GET.get('page')or 1)

    categoryId = request.GET.get('categoryId','')
    categoryId = int(categoryId) if categoryId else ''

    name = request.GET.get('name','')
    productList = Product.objects.filter(name__contains=name)
    if categoryId:
        productList = productList.filter(category__id=categoryId)   

    start = (page-1) * PAGE_SIZE
    end = start + PAGE_SIZE
    total =  len(productList)               # Tổng số bản ghi
    num_page = math.ceil( total / PAGE_SIZE)# Tổng số trang
    prev_page = max(page -1,1)              # Trang trước
    next_page = min(page + 1, num_page)     # Trang sau
    productList = productList[start:end]


    categoryList = Category.objects.all()
    context = {
                'categoryId':categoryId,
                'productList':productList,
                'name':name,
                'start': start, 'total': total, 'num_page': num_page,
                'page': page, 'prev_page': prev_page, 'next_page': next_page,
                'categoryList':categoryList,    
            }
    return render(request,'index.html',context)

def viewProduct(request,pk):
    product = get_object_or_404(Product,pk=pk)
    context = {'product':product}
    return render(request,'view_product.html',context)

def saveOrder(product, form_data):
    order = Order()
    order.product = product
    order.qty = form_data['qty']
    order.priceUnit = product.price
    order.fullname = form_data['fullname']
    order.phone = form_data['phone']
    order.address = form_data['address']
    order.dateOrder = datetime.now()
    order.status = Order.Status.PENDING
    order.save()

def orderProduct(request,pk):
    form = OrderForm(initial={'qty':1})
    product = get_object_or_404(Product,pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            saveOrder(product, form.cleaned_data)
            return redirect('/thank_you')
    context = {'product':product,'form':form}
    return render(request,'order_product.html',context)

def thankYou(request):
    return render(request,'thank_you.html')