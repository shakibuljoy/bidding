from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, CustomUserLoginForm

def signup(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in!")
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Get the unsaved user object
            user.mode = 'bidder'
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)  # Set the password
            user.save()  # Save the user object to the database

            user = authenticate(request, username=username, password=password)
            login(request, user)

            # Now you can access the company_name attribute
            return redirect('tendering:list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def testuser(request):
    if request.user.is_authenticated:
        if request.user.is_bidder():
            request.user.mode = 'poster'
            request.user.save()
            return HttpResponse(f"{request.user.company_name} is Bidder")
        elif request.user.is_poster():
            request.user.mode = 'bidder'
            request.user.save()
            return HttpResponse(f"{request.user.company_name} is Poster")
    else:
        return HttpResponse("User not authenticated!")
    
def login_view(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in!")
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/account/test')  # Redirect to your desired page after successful login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomUserLoginForm()

    context = {'form': form}
    return render(request, 'login.html', context)


@login_required  
def logout_view(request):
    logout(request)
    return redirect('usermodel:login')
