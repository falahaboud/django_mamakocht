from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def singup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = UserCreationForm()

    form = UserCreationForm()
    return render(request, 'registration/singup.html', {
        'form': form
    })
@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(TemplateView):
    template_name = 'secret_page.html'
