from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .form import UserSignUpForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer

@api_view(['POST'])
def create_user(request):
    print("on line 11 -->", request.data)
    serializer = UserCreateSerializer(data=request.data)
    response_data = {
        "errors": None,
        "data": None
    }

    if serializer.is_valid():
        user = serializer.save()
        print("The serializer is saving but where is the question")
        response_data["data"] = {
            "success": True,
            "id": user.id
        }
        response_status = status.HTTP_201_CREATED
    else:
        response_data['errors'] = serializer.errors
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(response_data, status=response_status)



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














