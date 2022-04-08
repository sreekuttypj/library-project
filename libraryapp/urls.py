from django.urls import path
from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home),
    path('admin_reg/',views.admin_reg),
    path('admin_login/',views.admin_login),
    path('stud_login/',views.stud_login),
    path('stud_reg/',views.stud_reg),
    path('stud_home/',views.stud_home),
    path('admin_home/',views.admin_home),
    path('admin_add_book/',views.admin_add_book),
    path('admin_view_book/',views.admin_view_book),
    path('delete_book/(?<id>)',views.delete_book),
    path('update',views.update),

    path('stud_view_book/',views.stud_view_book),

    path('logout/',views.Logout),
]

