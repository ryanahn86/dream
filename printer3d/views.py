from django.shortcuts import render
from  django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from printer3d.models import Printer3D, Reservation
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class Printer3DLV(ListView):
    model = Printer3D

class Printer3DDV(DetailView):
    model = Printer3D

class Printer3D_CreateView(CreateView):
    model = Printer3D
    fields = ['title','manufacturer','price','thumb_img','detail_img','description']
    success_url = reverse_lazy('list')

class Printer3D_UpdateView(UpdateView):
    model = Printer3D
    fields = ['title', 'manufacturer', 'price', 'thumb_img', 'detail_img',
              'description']
    success_url = reverse_lazy('list')

class Printer3D_UpdateExtraView(UpdateView):
    model = Printer3D
    #template_name = "printer3d_form_extra.html"
    fields = ['reservation_user_name','reservation_user_address',
                    'reservation_user_email','reservation_user_phone',
                    'reservation_start_date','reservation_end_date',
                    'reservation_status']
    success_url = reverse_lazy('list')


class Printer3D_DeleteView(DeleteView):
    model = Printer3D
    success_url = reverse_lazy('list')

class Reservation_CreateView(CreateView):
    model = Reservation
    fields = ['title','email','phone','start','finish']
    success_url = reverse_lazy('reservation_list')

class Reservation_ListView(ListView):
    model = Reservation



