from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'third_task/main_page.html')


def shop_page(request):
    items = {
        'item1': 'Игровая приставка',
        'item2': 'Комплект игр',
        'item3': 'Игровая мышь'
    }
    return render(request, 'third_task/shop_page.html', {'items': items})


def cart_page(request):
    return render(request, 'third_task/cart_page.html')
