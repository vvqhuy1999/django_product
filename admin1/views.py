from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from .models import *
from .forms import *
from users.forms import *
from users.models import*
from accounts.forms import *
import math
# Create your views here.

@login_required
#@staff_member_required
def listCategory(request):
    categoryList = Category.objects.all()
    context={'categoryList':categoryList}
    return render(request,'category/list.html',context)

@login_required
#@staff_member_required
def createCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin1/staff')
    context = {'form':form}
    return render(request,'category/form.html',context) 

@login_required
#@staff_member_required
def updateCategory(request,pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('/admin1/staff')
    context = {'form':form}
    return render(request,'category/form.html',context)

@login_required
#@staff_member_required
def deleteCategory(request,pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('/admin1/staff')

@login_required
#@staff_member_required   
def listProduct(request):
    PAGE_SIZE = 4
    page = int(request.GET.get('page') or 1)
    categoryId = request.GET.get('categoryId','')
    categoryId = int(categoryId) if categoryId else ''

    name = request.GET.get('name','')
    productList = Product.objects.filter(Q(code__contains=name)
                    |Q(name__contains=name)
                    |Q(category__name__contains=name))
    if categoryId:
        productList = productList.filter(category__id__contains=categoryId)
    
    start = (page-1) * PAGE_SIZE
    end = start + PAGE_SIZE
    total = len(productList)                 # Tổng số bản ghi
    num_page = math.ceil(total / PAGE_SIZE)  # Tổng số trang
    prev_page = max(page - 1, 1)             # Trang trước
    next_page = min(page + 1, num_page)      # Trang sau
    productList = productList[start:end]

    categoryList = Category.objects.all()
    context={
                'categoryId':categoryId,
                'productList':productList,
                'name':name,
                'categoryList':categoryList,
                'start': start, 'total': total, 'num_page': num_page,
                'page': page, 'prev_page': prev_page, 'next_page': next_page,
            }
    return render(request,'product/list.html',context)

@login_required
#@staff_member_required
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin1/list_product')
    context = {'form':form}
    return render(request,'product/form.html',context)

@login_required
#@staff_member_required
def updateProduct(request,pk):
    product = Product.objects.get(pk=pk)
    form  = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/admin1/list_product')
    context = {'form':form}
    return render(request,'product/form.html',context)

@login_required
#@staff_member_required
def deleteProduct(request,pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('/admin1/list_product')

@login_required
def listOrder(request):
    name = request.GET.get('name','')
    orderList = Order.objects.filter(Q(fullname__contains=name)|Q(product__name=name))
    #orderList = Order.objects.all()
    orderList = orderList.order_by('status','dateOrder')
    context = {'orderList':orderList,'name':name}
    return render(request,'order/list.html',context)

@login_required
def viewOrder(request,pk):
    order = Order.objects.get(pk=pk)
    context = {'order':order}
    return render(request,'order/detail.html',context)

@login_required
def confirmOrder(request,pk):
    form = OrderConfirmForm()
    if request.method == 'POST':
        form = OrderConfirmForm(request.POST)
        if form.is_valid():
            order = Order.objects.get(pk=pk)
            order.status = Order.Status.DELIVERED
            order.deliverDate = form.cleaned_data['deliverDate']
            order.save()
            return redirect('/admin1/list_order')
    context = {'form':form}
    return render(request,'order/confirm.html',context)

@login_required
def cancelOrder(request,pk):
    if request.method == 'POST':
        order = Order.objects.get(pk=pk)
        order.status = Order.Status.CANCELED
        order.save()
        return redirect('/admin1/list_order')
    return render(request,'order/cancel.html')

def informationUer(request,pk):
    form = CustomUserCreationForm(instance=request.user)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/admin1/staff')
    context ={'form':form}
    return render(request,'infor/information.html',context)
