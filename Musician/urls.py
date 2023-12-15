from django.urls import path,include
from . import views
urlpatterns = [
    path('Musician/',views.add_musician,name='musician'),
    path('edit/<int:id>',views.edit_musician,name='edit_musician'),
    path('delete/<int:id>',views.delete_musician,name='delete_musician'),
]

