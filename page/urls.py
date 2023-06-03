from django.urls import path
from page.views import (
    about_us_view, 
    contact_us_view, 
    visions_view, 
    index_view,
    page_view,)


urlpatterns = [
    path('', index_view, name ="home"),
    # path('hakkimizda/', about_us_view, name= "about_us"),
    # path('iletisim/', contact_us_view, name= "contact_us")¨ 
    # path('vizyonumuz/', visions_view, name = "vision"),
    path('<slug:slug>/', page_view ),
]