from django.shortcuts import render
from web.models import Category,Item
def index(request):
    items = Item.objects.filter()[0:5]
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'items':items,
    }
    return render(request,'web/index.html',context)

def index2(request):
    return render(request,"web/index2.html")

def detail(request):
    return render(request,'web/detail.html')