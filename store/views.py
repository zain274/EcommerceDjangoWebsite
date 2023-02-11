from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    return render(request,"store/index.html")


def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category ,}
    return render(request,"store/collections.html",context)


def collectionsview(request,slug):
    if(Category.objects.filter(slug =slug , status=0)):
        products= Product.objects.filter(category__slug =slug)

       
        category = Category.objects.filter(slug=slug).first()
        context = {'products':products , 'category':category}
        return render(request,"store/product/index.html",context)
    else :
        # messages.warning(request,"no product found")
        return "no such category"
        

def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug =cate_slug , status=0)):
        if(Product.objects.filter(slug =prod_slug , status=0)):
             products= Product.objects.filter(slug=prod_slug , statuc=0).first
             context = {'products':products}
        else:
            messages.error(request,"no product found")
            return redirect('collections')

    else:
        messages.error(request,"no category found")
        return redirect('collections')
        
    return render(request,"store/product/view.html",context)
        
