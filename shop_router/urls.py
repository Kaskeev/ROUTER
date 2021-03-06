from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('basket/', views.basket, name='basket'),
    path('form/', views.form, name='form'),
    path('order/', views.order, name='order'),
    path('product/<int:id_obj>', views.product, name='product'),
    path('routers/<int:id_object>', views.routers, name='routers'),
    path('about/', views.about, name='about'),
    path('addProductToBascet/<int:id_object>', views.addProductToBascet, name='addProductToBascet'),
    path('addCount/<int:id_object>', views.addCountOrder, name='addCount'),
    path('minusCount/<int:id_object>', views.minusCountOrder, name='minusCount'),
    path('minusCount/<int:id_object>', views.minusCountOrder, name='minusCount'),
    path('category/<int:id_object>', views.category_set, name='category'),
    path('search/', views.Search.as_view(), name='search'),
    path('category/<int:id>/children', views.getChildrenCategories, name='categoryChildren'),

]
