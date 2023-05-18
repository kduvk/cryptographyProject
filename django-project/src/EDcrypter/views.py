from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .algorithms import *

def home(request):
    if request.method == 'POST':
        cipher_type = request.POST.get('cipher_type')
        if cipher_type == 'caesar':
            return HttpResponseRedirect(reverse('caesar_cipher_url'))
        elif cipher_type == 'atBash':
            return HttpResponseRedirect(reverse('atBash_cipher_url'))
        elif cipher_type == 'vigenere':
            return HttpResponseRedirect(reverse('vigenere_cipher_url'))
        elif cipher_type == 'beaufort':
            return HttpResponseRedirect(reverse('beaufort_cipher_url'))
        elif cipher_type == 'railFence':
            return HttpResponseRedirect(reverse('railFence_cipher_url'))
        elif cipher_type == 'gronsfeld':
            return HttpResponseRedirect(reverse('gronsfeld_cipher_url'))
    return render(request, 'EDcrypter/home.html')


def caesar_cipher(request):
    if request.method == 'POST':
        input_text = request.POST.get('input-text')
        input_number = int(request.POST.get('input-number'))
        action = request.POST.get('action')
        output = ''
        if action == 'encrypt':
            output = caesarCipherE(input_text, input_number)
        elif action == 'decrypt':
            output = caesarCipherD(input_text, input_number)
        ## Render the output in a context dictionary
        context = {'output': output}
        return render(request, 'EDcrypter/caesarCipher.html', context)
    
    # If the request method is not POST, render the form with no output
    return render(request, 'EDcrypter/caesarCipher.html')

def atBash_cipher(request):
    if request.method == 'POST':
        input_text = request.POST.get('input-text')
        action = request.POST.get('action')
        output = ''
        if action == 'encrypt':
            output = atBashE(input_text)
        elif action == 'decrypt':
            output = atBashD(input_text)
        # Render the output in a context dictionary
        context = {'output': output}
        return render(request, 'EDcrypter/atBashCipher.html', context)

    # If the request method is not POST, render the form with no output
    return render(request, 'EDcrypter/atBashCipher.html')

def vigenere_cipher(request):
    if request.method == 'POST':
        input_text = request.POST.get('input-text')
        input_key = request.POST.get('input-key')
        action = request.POST.get('action')
        output = ''
        if action == 'encrypt':
            output = vigenereE(input_text, input_key)
        elif action == 'decrypt':
            output = vigenereD(input_text, input_key)
        # Render the output in a context dictionary
        context = {'output': output}
        return render(request, 'EDcrypter/vigenereCipher.html', context)

    # If the request method is not POST, render the form with no output
    return render(request, 'EDcrypter/vigenereCipher.html')

def beaufort_cipher(request):
    if request.method == 'POST':
        input_text = request.POST.get('input-text')
        input_key = request.POST.get('input-key')
        action = request.POST.get('action')
        output = ''
        if action == "encrypt":
            output = beaufortE(input_text, input_key)
        elif action == "decrypt":
            output = beaufortD(input_text, input_key)
        context = {'output': output}
        return render(request, 'EDcrypter/beaufortCipher.html', context)
    return render(request, 'EDcrypter/beaufortCipher.html')

def railFence_cipher(request):
    if request.method == 'POST':
        input_text = request.POST.get('input-text')
        input_number = int(request.POST.get('input-number'))
        action = request.POST.get('action')
        output = ''
        if action == 'encrypt':
            output = railFenceE(input_text, input_number)
        elif action == 'decrypt':
            output = railFenceD(input_text, input_number)
        context = {'output': output}
        return render(request, 'EDcrypter/railFenceCipher.html', context)

    return render(request, 'EDcrypter/railFenceCipher.html')

def gronsfeld_cipher(request):
    if request.method == 'POST':
        input_text = request.POST.get('input-text')
        input_number = str((request.POST.get('input-number')))
        action = request.POST.get('action')
        output = ''
        if action == 'encrypt':
            output = gronsfeldE(input_text, input_number)
        elif action == 'decrypt':
            output = gronsfeldD(input_text, input_number)
        context = {'output': output}
        return render(request, 'EDcrypter/gronsfeldCipher.html', context)
    return render(request, 'EDcrypter/gronsfeldCipher.html')
