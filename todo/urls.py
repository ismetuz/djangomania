from django.urls import path
from todo.views import home_view,todo_detail_view, category_view,tag_view
from config.view import logout_view

urlpatterns = [
    path('', home_view,name="home" ),
    path('category/<slug:category_slug>', category_view, name='category_view'),
    path('tag/<slug:tag_slug>', tag_view, name='tag_view'),
    path('category/<slug:category_slug>/todo/<int:id>/',todo_detail_view, name="todo_detail_view"),
    path('logout/',logout_view,name='logout_view'),
]