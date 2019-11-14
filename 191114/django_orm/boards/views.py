from django.shortcuts import render
from boards.models import Subway

# Create your views here.
def index(request):
    return render(request, "boards/index.html")

def subway_order(request):
    menu=['에그마요', '이탈리안 비엠티', '터키 베이컨 아보카도']
    size=['15cm','30cm']
    bread=['화이트', '하티', '파마산오레가노', '위트', '허니오트', '플랫']
    add=['토마토', '오이', '할라피뇨', '레드식초', '샤우젼아일랜드']
    context={
        'menu':menu,
        'size':size,
        'bread':bread,
        'add':add
    }
    return render(request, 'subway_order.html', context)

def reciept(request):
    name=request.POST.get('name')
    date=request.POST.get('date')
    menu=request.POST.get('menu')
    size=request.POST.get('size')
    bread=request.POST.get('bread')
    add=request.POST.get('add')
    
    subway_new = Subway.objects.create(name=name, date=date, menu=menu, size=size, bread=bread, add=add)
    subway_new.save()
    
    get = Subway.objects.all()

    context = {
        'orders' : get
    }

    return render(request, 'reciept.html', context)

def id_order(request, id):
    call_info = Subway.objects.get(id=id)
    context = {
        'order' : call_info
    }

    return render(request, 'id_order.html', context)