from django.contrib import admin
from printer3d.models import Printer3D, Reservation
# Register your models here.

class Printer3DAdmin(admin.ModelAdmin):
    list_display = ('title','manufacturer','price','thumb_img','detail_img',
                    'description','create_date',
                    'reservation_user_name','reservation_user_address',
                    'reservation_user_email','reservation_user_phone',
                    'reservation_start_date','reservation_end_date',
                    'reservation_status')

admin.site.register(Printer3D, Printer3DAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('title','email','phone','start','finish')

admin.site.register(Reservation, ReservationAdmin)


