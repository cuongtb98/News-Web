from django.shortcuts import render
from .models import ProductDev
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
import requests
from bs4 import BeautifulSoup
# Create your views here.
def store(request):
	result = ProductDev.objects.all()
	products = ProductDev.objects.all()
	newposts = products[::-1][:3]

	products_data = [itm for itm in products if itm in result]

	paginator = Paginator(products_data, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'page_obj': page_obj, 'result':result, 'newposts':newposts, 'data':get_metaweather()}

	return render(request, 'SnewStore/ketquatimkiem.html', context)

def get_metaweather():
	url = 'https://nchmf.gov.vn/Kttvsite/vi-VN/1/tp-ha-noi-w28.html'
	source = requests.get(url)
	soup = BeautifulSoup(source.text, 'html.parser')
	try:
		nhietdo = soup.find('div', class_='uk-width-3-4').text
	except:
		nhietdo = ''
	try:
		time = soup.find('div', class_='time-update').text
	except:
		time = ''

	data ={
		'nhietdo':nhietdo,
		'time':time,
	}
	return data


def chinhtrixahoi(request):

	result = ProductDev.objects.filter(category=0)
	products = ProductDev.objects.all()
	newposts = products[::-1][:3]

	products_data = [itm for itm in products if itm in result]

	paginator = Paginator(products_data, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'page_obj': page_obj, 'result':result, 'newposts':newposts, 'data':get_metaweather()}

	return render(request, 'SnewStore/chinhtrixahoi.html', context)

def result_search_post(request):
	if request.method == 'POST':
		searched = request.POST['searched']
		result = ProductDev.objects.filter(title__contains=searched)
		products = ProductDev.objects.all()
		newposts = products[::-1][:3]
		#result1 = ProductDev.objects.filter(category=1)

		paginator = Paginator(result, 6)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context = {'page_obj': page_obj, 'result':result, 'newposts':newposts, 'data':get_metaweather()}
		return render(request, 'SnewStore/ketquatimkiem.html', context)

def doisong(request):
	result = ProductDev.objects.filter(category=1)
	products = ProductDev.objects.all()
	newposts = products[::-1][:3]

	products_data = [itm for itm in products if itm in result]

	paginator = Paginator(products_data, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'page_obj': page_obj, 'result':result, 'newposts':newposts, 'data':get_metaweather()}
	return render(request, 'SnewStore/doisong.html', context)

def thethao(request):
	result = ProductDev.objects.filter(category=2)
	products = ProductDev.objects.all()
	newposts = products[::-1][:3]

	products_data = [itm for itm in products if itm in result]

	paginator = Paginator(products_data, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'page_obj': page_obj, 'result':result, 'newposts':newposts, 'data':get_metaweather()}
	return render(request, 'SnewStore/thethao.html', context)

def suckhoe(request):
	result = ProductDev.objects.filter(category=3)
	products = ProductDev.objects.all()
	newposts = products[::-1][:3]

	products_data = [itm for itm in products if itm in result]

	paginator = Paginator(products_data, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'page_obj': page_obj, 'result':result, 'newposts':newposts, 'data':get_metaweather()}
	return render(request, 'SnewStore/suckhoe.html', context)

def khoahoc(request):
	result = ProductDev.objects.filter(category=4)
	products = ProductDev.objects.all()
	newposts = products[::-1][:3]

	products_data = [itm for itm in products if itm in result]

	paginator = Paginator(products_data, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'page_obj': page_obj, 'result':result, 'newposts':newposts, 'data':get_metaweather()}
	return render(request, 'SnewStore/khoahoc.html', context)

def dulich(request):
	result = ProductDev.objects.filter(category=5)
	products = ProductDev.objects.all()
	newposts = products[::-1][:3]

	products_data = [itm for itm in products if itm in result]

	paginator = Paginator(products_data, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'page_obj': page_obj, 'result':result, 'newposts':newposts, 'data':get_metaweather()}
	return render(request, 'SnewStore/dulich.html', context)


def post_detail(request, pk):
	detail = get_object_or_404(ProductDev, pk=pk)
	context = {'detail':detail, 'data':get_metaweather()}
	return render(request, 'SnewStore/post_detail.html', context)