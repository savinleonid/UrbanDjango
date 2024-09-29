from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'fourth_task/main_page.html')


def shop_page(request):
    items = {'items': [
        'Игровая приставка',
        'Комплект игр',
        'Игровая мышь'
    ]}
    return render(request, 'fourth_task/shop_page.html', {'items': items})


def cart_page(request):
    return render(request, 'fourth_task/cart_page.html')
