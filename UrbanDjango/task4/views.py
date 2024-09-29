from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'fourth_task/main_page.html')


def shop_page(request):
    items = {'games': [
        'Atomic Heart',
        'Cyberpunk 2077',
        'PayDay 2'
    ]}
    return render(request, 'fourth_task/shop_page.html', {'items': items})


def cart_page(request):
    return render(request, 'fourth_task/cart_page.html')
