from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import User
# Create your views here.

class UserListView(ListView):
    model = User

class UserCreateView(CreateView):
    model = User
    fields = ['nome', 'idade']
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    fields = ['nome','idade']
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')
