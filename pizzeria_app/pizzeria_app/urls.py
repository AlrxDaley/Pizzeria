from django.contrib import admin
from django.urls import path
from table_app.views import index, table_booking, update_booking, booking_options, contact, booking_search, update_record

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name='index'),
    path('booking_options', booking_options , name='booking_options'),
    path("contact", contact, name="contact"),
    path('table_booking/', table_booking, name='table_booking'),
    path('booking_search/', booking_search, name='booking_search'),
    path('update_booking/<str:booking_ref>', update_booking, name='update_booking'),
    path('booking_search/update_record/<str:booking_ref>', update_record, name='update_record')
]
