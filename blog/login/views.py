from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

# Create your views here.
def add_user(request):
    # получили данные. нужно сохранить юзера в базу
    if request.method == "POST":
        # получаем данные из формы
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/users/')
    # это простой запрос, нужно показать форму
    else:
        form = UserForm()
        return render(request, "add_user.html", {'form': form})