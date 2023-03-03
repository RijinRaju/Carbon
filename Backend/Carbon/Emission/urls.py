from django.urls import path
from . import views

urlpatterns = [
    path('insert',views.insert_emission,name="insert details"),
    path('display',views.display_emission,name="display emission"),
    path('limit',views.set_limit,name="set limit"),
    path('compare',views.compare_emission,name="compare"),
    path('details',views.admin_view,name="admin view"),
    path('delete_user',views.delete_user,name="delete user")

]
