from django.shortcuts import render,redirect,get_object_or_404
import openai
import os
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import datetime

# Create your views here.
def index(request):
    return render (request, 'general/index.html')

openai.api_key = ""

# def chatbot(request):
#     response_text = ""
    
#     if request.method == 'POST':
#         prompt = request.POST.get('prompt')
        
#         if prompt == 'exit':
#             return render(request, 'chatbot.html', {'response_text': 'Chatbot exited.'})
        
#         messages = [{"role": "system", "content": "You are a Intelligent assistant."}]
#         messages.append({"role": "user", "content": prompt})
        
#         chat = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo", messages=messages, temperature=0.5
#         )
        
#         response_text = chat.choices[0].message.content

#     context = {'response_text': response_text}
#     return render(request, 'general/chatbot.html', context)


from django.shortcuts import render, redirect
from .models import Chats
from django.contrib.auth.decorators import login_required
import openai

@login_required
def chatbot(request):
    response_text = ""
    previous_chats = Chats.objects.filter(user=request.user).order_by('-date')
    
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        
        if prompt == 'exit':
            return render(request, 'chatbot.html', {'response_text': 'Chatbot exited.', 'previous_chats': previous_chats})
        
        messages = [{"role": "system", "content": "You are an intelligent assistant."}]
        messages.append({"role": "user", "content": prompt})
        
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, temperature=0.5
        )
        
        response_text = chat.choices[0].message.content

        # Save the new chat in the database
        new_chat = Chats(user=request.user, question=prompt, response=response_text)
        new_chat.save()

    return render(request, 'general/chatbot.html', {'response_text': response_text, 'previous_chats': previous_chats})



def user_register(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'user/user_register.html')
        else:
            user = User.objects.create_user(
                username=uname,
                password=passw,
            )
            # Add a success message
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('user_register')
    else:
        return render(request, "user/user_register.html")
    


def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw):
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'user/user_login.html')


def SignOut2(request):
     logout(request)
     return redirect('index')



def user_profile(request):
    # Retrieve the current user
    user = request.user
    
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        new_profile_picture = request.FILES.get('profile_picture')
        
        # Update user's profile fields
        user.name = name
        user.mobile_number = mobile_number
        user.email = email
        
        # Check if a new profile picture is uploaded
        if new_profile_picture:
            user.profile_picture = new_profile_picture
        
        # Save the updated profile
        user.save()
        
        # Redirect to profile page or any other page you want
        return redirect('user_profile')  # Replace 'profile-page' with the name of your profile page URL
    else:
        # Render the template with the current user's profile details
        return render(request, 'user/user_profile.html', {'user': user})
    


def user_history(request):
    previous_chats = Chats.objects.filter(user=request.user).order_by('-date')
    context = {'previous_chats':previous_chats}
    return render(request, 'user/user_history.html', context)



def delete_chat(request,pk):
    chats = get_object_or_404(Chats, pk=pk)
    chats.delete()
    return redirect('user_history')