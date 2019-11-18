from django.shortcuts import render, redirect
from .models import Subway

# Create your views here.
def index(request):
    orders = Subway.objects.all()
    context = {
        'orders' : orders
    }
    return render(request, 'subway/index.html', context)

def new(request):
    if request.method=="POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        menu = request.POST.get('menu')
        bread = request.POST.get('bread')
        vegetable = request.POST.get('vegetable')
        sauce = request.POST.get('sauce')
        drink = request.POST.get('drink')

        subway = Subway()

        subway.name = name
        subway.address = address
        subway.phone = phone
        subway.menu = menu
        subway.bread = bread
        subway.vegetable = vegetable
        subway.sauce = sauce
        subway.drink = drink

        subway.save()

        return redirect('subway:index')

    else:
        menu=['에그마요', '이탈리안 비엠티', '터키 베이컨 아보카도']
        bread = ['화이트', '하티', '파마산오레가노', '위트', '허니오트', '플랫']
        vegetable = ['토마토', '오이', '할라피뇨', '양상추']
        sauce = ['레드식초', '샤우젼아일랜드', '스위트칠리', '허니머스타드']
        drink = ['콜라', '사이다', '환타', '스프라이트']
        context= {
            'menu' : menu,
            'bread' : bread,
            'vegetable' : vegetable,
            'sauce' : sauce,
            'drink' : drink
        }
        return render(request, 'subway/new.html', context)

# def create(request):
#     name = request.POST.get('name')
#     address = request.POST.get('address')
#     phone = request.POST.get('phone')
#     menu = request.POST.get('menu')
#     bread = request.POST.get('bread')
#     vegetable = request.POST.get('vegetable')
#     sauce = request.POST.get('sauce')
#     drink = request.POST.get('drink')

#     subway = Subway()

#     subway.name = name
#     subway.address = address
#     subway.phone = phone
#     subway.menu = menu
#     subway.bread = bread
#     subway.vegetable = vegetable
#     subway.sauce = sauce
#     subway.drink = drink

#     subway.save()

#     return redirect('subway:index')

def detail(request, pk):
    order = Subway.objects.get(id=pk)
    context = {
        'order' : order
    }
    return render(request, 'subway/detail.html', context)

def update(request, pk):
    if request.method=="POST":
        order = Subway.objects.get(id=pk)

        menu = request.POST.get('menu')
        bread = request.POST.get('bread')
        vegetable = request.POST.get('vegetable')
        sauce = request.POST.get('sauce')
        drink = request.POST.get('drink')

        print(menu)

        order.menu = menu
        order.bread = bread
        order.vegetable = vegetable
        order.sauce = sauce
        order.drink = drink

        order.save()
        return redirect('subway:index')
    
    else:
        order = Subway.objects.get(id=pk)
        menu=['에그마요', '이탈리안 비엠티', '터키 베이컨 아보카도']
        bread = ['화이트', '하티', '파마산오레가노', '위트', '허니오트', '플랫']
        vegetable = ['토마토', '오이', '할라피뇨', '양상추']
        sauce = ['레드식초', '샤우젼아일랜드', '스위트칠리', '허니머스타드']
        drink = ['콜라', '사이다', '환타', '스프라이트']
        context= {
            'menu' : menu,
            'bread' : bread,
            'vegetable' : vegetable,
            'sauce' : sauce,
            'drink' : drink,
            'order': order
        }
        return render(request, 'subway/update.html', context)

# def change(request, pk):
#     order = Subway.objects.get(id=pk)

#     menu = request.POST.get('menu')
#     bread = request.POST.get('bread')
#     vegetable = request.POST.get('vegetable')
#     sauce = request.POST.get('sauce')
#     drink = request.POST.get('drink')

#     print(menu)

#     order.menu = menu
#     order.bread = bread
#     order.vegetable = vegetable
#     order.sauce = sauce
#     order.drink = drink

#     order.save()
#     return redirect('subway:index')

def delete(request, pk):
    order = Subway.objects.get(id=pk)

    if request.method=="POST":
        order.delete()

        return redirect('subway:index')
    
    else:
        return redirect('subway:detail', order.id)