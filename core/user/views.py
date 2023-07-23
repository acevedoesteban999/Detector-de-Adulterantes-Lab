from django.shortcuts import render,redirect
from django.views.generic import UpdateView,ListView,CreateView,DeleteView
from core.log.utils import MyLoginRequiredMixin
from core.user.models import User
from .forms import UserForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
#Create your views here.

class UserListView(MyLoginRequiredMixin,ListView):
    model=User
    template_name='list_user.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "Listado de Usuarios"
        return context

class UserCreateView(MyLoginRequiredMixin,CreateView):
    model=User
    template_name = 'update_user.html'
    form_class=UserForm
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form=self.get_form()
            form.save()
            messages.success(self.request,'Creado usuario {} correctamente'.format(form.data.get('username')))
        else:
            messages.error(request,'Error al crear')
        
        return redirect('user_list')
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "Actualizar Información"
        #context['url_cancel']=reverse_lazy('user_list')
        return context
    
class UserUpdateView(MyLoginRequiredMixin,UpdateView):
    model=User
    template_name = 'update_user.html'
    form_class=UserForm
    
    def dispatch(self, request, *args, **kwargs):
        kwargs['pk'] = self.request.user.id
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form=self.get_form()
            form.save()
            messages.success(self.request,'Actualizado  usuario {} correctamente'.format(form.data.get('username')))
        else:
            messages.error(request,'Error al Actualizar')
        
        return redirect('user_list')
        
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "Actualizar Información"
        context['url_cancel']=reverse_lazy('user_list')
        return context
    
class UserActDesactView(MyLoginRequiredMixin,DeleteView):
    model=User
    template_name = 'act_desact.html'
    
    # def dispatch(self, request, *args, **kwargs):
    #     kwargs['pk'] = self.request.user.id
    #     self.object = self.get_object()
    #     return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        self.object.is_active=not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('user_list'))
        
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "Actualizar Información"
        context['url_cancel']=reverse_lazy('user_list')
        context['active']=self.object.is_active
        context['username']=self.object.username
        return context
    
    
