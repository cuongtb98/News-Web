from django.urls import path
from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('chinhtrixahoi/', views.chinhtrixahoi, name="chinhtrixahoi"),
	path('doisong/', views.doisong, name="doisong"),
	path('thethao/', views.thethao, name="thethao"),
	path('suckhoe/', views.suckhoe, name="suckhoe"),
	path('khoahoc/', views.khoahoc, name="khoahoc"),
	path('dulich/', views.dulich, name="dulich"),
	path('result_search_post/', views.result_search_post, name="result_search_post"),

	path('post_detail/<int:pk>/', views.post_detail, name="post_detail"),
]