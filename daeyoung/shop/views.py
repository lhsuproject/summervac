from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from .models import Item
from django.contrib.auth import get_user_model

# Create your views here.

#홈페이지
def home(request):
    return render(request,'index.html')
#우리를 소개합니당~
def about(request):
    return render(request,'about.html')

#아이템이 보여질 페이지
def shop(request):
    items = Item.objects.filter().order_by('-pk')
    return render(request, 'shop.html', {'items':items})
#마이 페이지
def my(request):
    return render(request, 'myPage.html')
    
#상품등록을 위한 페이지
def goodsRegist(request):
    return render(request,'goodsRegist.html')

#상품등록하기 위한 데이터를 저장하는 함수
def ItemCreate(request):
    # if request.method =='POST' or request.method == 'FILES':
    #     item = ItemForm(request.POST, request.FILES)
    #     if item.is_valid():
    #         item.save()
    #     return redirect('shop')
    # else:
    #     item = ItemForm()
    # return render(request,'goodsRegist.html',{'item':item})
    if request.method=='POST' or request.method == 'FILES':
        items = Item()
        items.image=request.FILES['image']
        items.title=request.POST['title']
        items.money=request.POST['money']
        items.option1=request.POST['option1']
        items.option2=request.POST['option2']
        items.body=request.POST['body']
        items.save()
    return redirect('shop')
        


def detail(request, item_id):
    item_detail = get_object_or_404(Item, pk=item_id)
    return render(request,'detail.html',{'item_detail':item_detail})