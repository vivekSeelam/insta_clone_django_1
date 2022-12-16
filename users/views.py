from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .form import UserSignUpForm


# Create your views here.
def index(request):
    count_of_users = User.objects.count()

    users = User.objects.all()
    for user in users:
        print(user.name)

    context = {
        "count_of_users": count_of_users,
        "users": users
    }
    return render(request, 'users/index.html', context)


def signup(request):

    form = UserSignUpForm()
    errors = []
    message = None

    if request.method == "POST":
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            message = "new User is created"
        else:
            errors = form.errors

    context = {
        'form': form,
        'errors': errors,
        'message': message
    }
    return render(request, 'users/signup.html', context)














