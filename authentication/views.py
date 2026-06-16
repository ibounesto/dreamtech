from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import DetailView, UpdateView, DeleteView
from . import forms

class UserDeleteView(DeleteView):
    template_name = 'authentication/user_confirm_delete.html'
    success_url = '/'

class UserDetailView(DetailView):
    template_name = 'authentication/user_detail.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user
    
class UserUpdateView(UpdateView):
    template_name = 'authentication/user_update.html'
    form_class = forms.UpdateUserForm
    success_url = '/'

    def get_object(self):
        return self.request.user


def register_user(request):
    form = forms.RegisterUserForm()

    if request.method == 'POST':
        form = forms.RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        
        else:
            return render(request,'authentication/signup.html',context={
            'form':form,
        }) 
    else:
        return render(request,'authentication/signup.html',context={
            'form':form,
        })        