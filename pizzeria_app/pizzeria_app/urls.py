from django.contrib import admin
from django.urls import path
from table_app.views import index, table_booking, add_booking, booking_options, contact, booking_search_update, update_booking, delete_booking, booking_search_delete
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name='index'),
    path('booking_options', booking_options , name='booking_options'),
    path("contact", contact, name="contact"),
    path('table_booking/', table_booking, name='table_booking'),
    path('booking_search_update/', booking_search_update, name='booking_search_update'),
    path('add_booking/<str:booking_ref>', add_booking, name='add_booking'),
    path('booking_search_update/update_booking/<str:booking_ref>', update_booking, name='update_booking'),
    path('booking_search_delete/', booking_search_delete, name='booking_search_delete'),
    path('delete_booking/<str:booking_ref>', delete_booking, name='delete_booking'),
]

urlpatterns += staticfiles_urlpatterns()