from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from login.models import User


def homepage(request):
    context = {
        'title': 'Home',
        'content': User.objects.all,
    }
    return render(request, 'home.html', context)


def delete_item(request, id):
    if request.method == 'POST':
        item = get_object_or_404(User, id=id)
        item.delete()
        return HttpResponseRedirect('/')
    return item