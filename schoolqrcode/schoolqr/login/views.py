from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import UserForm
from .models import User

def get_form(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_url())
    context = {
        'title': 'Login',
        'form': form
    }
    return render(request, 'login.html', context)

def success(request, id):
    context = {
        'title': 'Success',
        'id': id
    }
    return render(request, 'success.html', context)

def remove(request, id):
    if request.method == 'POST':
        item = get_object_or_404(User, id=id)
        item.delete()
        return HttpResponseRedirect('/login/')
    return HttpResponseRedirect('/login/')