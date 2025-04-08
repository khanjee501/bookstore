from django.urls import include, path

from .views import home_page_view

urlpatterns = [
    path("", home_page_view, name="home"),
]
