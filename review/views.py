from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from review.models import Product
from django.core.paginator import Paginator
# from math import ceil

def index(request):
    products=Product.objects.all()
    paginator=Paginator(products,9)
    page=request.GET.get('page')
    products=paginator.get_page(page)
    # n=len(products)
    # nslides=n//4 + ceil((n/4) -(n//4))
    # allprods=[]
    # catprods=Product.objects.values('catrgory')
    # cats={item['catrgory']for item in catprods}
    # for cat in cats:
        # prod=Product.objects.filter(catrgory=cat)
        # n=len(prod)
        # nslides=n//4 + ceil((n/4) -(n//4))
        # allprods.append([prod,range(1,nslides),nslides])
    # allprods=[[products,range(1,nslides),nslides],
    #           [products,range(1,nslides),nslides]]
    # params={'no_of_slides':nslides,'range':range(1,nslides+1),'products':products}
    # params={'allprods':allprods}
    params={'products':products}
    return render(request,'index.html',params)

def detail(request,pk):
    products=Product.objects.get(pk=pk)
    params={'products':products}
    return render(request,'test.html',params)


def about(request):
    return render(request,'review/about.html')

def contact(request):
    return render(request,'we are contact')

def tracker(request):
    return render(request,'we track order')

def search(request):
    return render(request,'we are search')

def prodView(request):
    return render(request,'we are prodView')

def checkout(request):
    return render(request,'we are checkout')

