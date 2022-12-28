from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
@login_required
def index(request):

    orders = Order.objects.all()    
    products = Product.objects.all()
    items_count=Product.objects.all().count()
    orders_count = Order.objects.all().count()
    workers_count = User.objects.all().count()


    if request.method  =='POST':
        myform = OrderForm(request.POST)
        if myform.is_valid():
            instance = myform.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        myform = OrderForm()
    context = {
        'orders':orders,
        'myform':myform,
        'product':products,
        'workers_count':workers_count,
        'items_count':items_count,
        'orders_count':orders_count
    }
    return render(request,'dashboard/index.html',context)





@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = User.objects.all().count()
    items_count=Product.objects.all().count()
    orders_count = Order.objects.all().count()

    context = {
        'workers':workers,
        'workers_count':workers_count,
        'items_count':items_count,
        'orders_count':orders_count
    }
    return render(request,'dashboard/staff.html',context)


@login_required
def staff_detail(request,pk):
    worker = User.objects.get(id=pk)
    context={
        'worker':worker
    }
    return render(request,'dashboard/worker_detail.html',context)


@login_required
def products(request):
    items = Product.objects.all() 
    items_count=Product.objects.all().count()
    # items = Product.objects.raw('SELECT * FROM dashboard_product') 

    orders_count = Order.objects.all().count()
    workers_count = User.objects.all().count()

    if request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
            return redirect('dashboard-products')
    else:
        form = ProductForm()
        # return redirect('dashboard-products')
    context={
        'items':items,
        'items_count':items_count,
        'form':form,
        'workers_count':workers_count,
        'orders_count':orders_count
    }
    return render(request,'dashboard/products.html',context)


@login_required
def product_delete(request,pk):
    item = Product.objects.filter(id=pk)

    if item.exists():
        item.delete()
        return redirect('dashboard-products')

    return render(request,'dashboard/products.html')


@login_required
def product_update(request,pk):
    item = Product.objects.get(id=pk)
    if request.method =='POST':
        form = ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context={
        'form':form
    }
    return render(request,'dashboard/update_product.html',context)

@login_required
def orders(request):
    orders = Order.objects.all()
    orders_count = Order.objects.all().count()
    items_count=Product.objects.all().count()
    workers_count = User.objects.all().count()
    context={
        'orders':orders,
        'orders_count':orders_count,
        'items_count':items_count,
        'workers_count':workers_count,
    }
    return render(request,'dashboard/orders.html',context)
