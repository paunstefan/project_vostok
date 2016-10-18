from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from vostok.models import Flight

urlpatterns = [url(r'^$', ListView.as_view(queryset=Flight.objects.all().order_by("id"),
                    template_name="vostok/home.html")),
                url(r'^usa$', ListView.as_view(queryset=Flight.objects.all().order_by("id"),
                                    template_name="vostok/usa.html")),
                url(r'^russia$', ListView.as_view(queryset=Flight.objects.all().order_by("id"),
                                    template_name="vostok/urss.html")),
                url(r'^china$', ListView.as_view(queryset=Flight.objects.all().order_by("id"),
                                    template_name="vostok/china.html")),
                url(r'^private$', ListView.as_view(queryset=Flight.objects.all().order_by("id"),
                                    template_name="vostok/private.html"))]
