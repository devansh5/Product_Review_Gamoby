# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="shophome"),
    path('<int:pk>/',views.detail,name="detailproduct"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="search"),
    path("productview/",views.prodView,name="Product"),
    path("checkout/",views.checkout,name="Checkout"),
]
