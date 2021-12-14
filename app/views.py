from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Table, Product

import requests



def index(request):
    table_state = Table.objects.first()
    products = Product.objects.all()

    response = requests.get('https://my.api.mockaroo.com/groceries.json?key=b350f720').json()
    context = {'response':response, 'table_state':table_state, 'products':products}
    return render(request, 'app/index.html', context)

def reset(request):
    table_state = Table.objects.first()
    table_state.state = 'full'
    table_state.save()

    return redirect('index')

def id_gt_15(request):
    messages.success(request, mark_safe('session.query(Product).filter(Product.id>15)<br>session.commit()'))

    table_state = Table.objects.first()
    table_state.state = 'id_gt_15'
    table_state.save()

    return redirect('index')

def has_a_price_bw_150_250(request):
    messages.success(request, mark_safe('session.query(Product).filter(and_(Product.name.like("%Chicken%"),'
                                        '(''Product.price.between(150, 300))))<br>session.commit()'))

    table_state = Table.objects.first()
    table_state.state = 'has_a_price_bw_150_250'
    table_state.save()

    return redirect('index')


def num_lt_50_or_gt_100(request):
    messages.success(request, mark_safe('session.query(Product).filter(or_(Product.how_many<50), '
                                        '(Product.price>100))<br>session.commit()'))
    table_state = Table.objects.first()
    table_state.state = "num_lt_50_or_gt_100"
    table_state.save()

    return redirect('index')


def delete_chinese(request):
    messages.success(request, mark_safe("session.query(Product).filter(Product.imported_from=='China').delete("
                                        "synchronize_session=False)<br>session.commit()"))
    table_state = Table.objects.first()
    table_state.state = "delete_chinese"
    table_state.save()

    return redirect('index')

def magic(request):
    return render(request, 'app/magic.html')