from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import TODO

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import os
# Create your views here.

class HomepageView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'
    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'
    
			    
    def register(request):
        if request.method == 'POST':
           form = UserCreationForm(request.POST)
           if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
        else:
            form = UserCreationForm()

        context = {'form': form}
        return render(request, 'registration/signup.html', context)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context_var'] = 'Context Data!'

        return context
   
    def context_function(self):
        return 'Context Function Return!'

    def todo_list(request):
        todos = TODO.objects.all()
        return JsonResponse({'todos': list(todos.values())})   

    def todo_create(request):
        if request.method == 'POST':
           todo_name = request.POST.get('todo_name')
           todo = TODO.objects.filter(name=todo_name)

        # we need to make sure that this todo does not exist in the database
        if todo.exists():
            return JsonResponse({'status': 'error'})

        todo = TODO.objects.create(name=todo_name)
        return JsonResponse({'todo_name': todo.name, 'status': 'created'}) 

    def todo_edit(request):
       if request.method == "POST":
          todo_name = request.POST.get('todo_name')
          new_todo_name = request.POST.get('new_todo_name')
          edited_todo = TODO.objects.get(name=todo_name)

        # if a todo with a name equal to `new_todo_name`
        # we return an error message
          if TODO.objects.filter(name=new_todo_name).exists():
             return JsonResponse({'status': 'error'})

          edited_todo.name = new_todo_name
          edited_todo.save()
        
          context = {
            'new_todo_name': new_todo_name,
            'status': 'updated'
        }
          return JsonResponse(context)      


    def todo_delete(request):
       if request.method == 'POST':
          todo_name = request.POST.get('todo_name')
          TODO.objects.filter(name=todo_name).delete()
          return JsonResponse({'status': "deleted"})            
