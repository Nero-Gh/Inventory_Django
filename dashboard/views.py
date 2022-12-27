from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm
from django.contrib.auth.models import User


# Create your views here.
@login_required
def index(request):
    return render(request,'dashboard/index.html')

@login_required
def staff(request):
    workers = User.objects.all()

    context = {
        'workers':workers
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
    # items = Product.objects.raw('SELECT * FROM dashboard_product') 

    if request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm()
        # return redirect('dashboard-products')
    context={
        'items':items,
        'form':form,
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

    context={
        'orders':orders
    }
    return render(request,'dashboard/orders.html',context)
