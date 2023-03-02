from django.shortcuts import render


def products(request):
    title = "Продукты/каталог"

    context = {
        'title': title,
    }

    return render(request, 'products.html', context)


