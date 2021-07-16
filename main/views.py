from django.shortcuts import render

def main_login(request):
    return render(request, 'main/main_login.html')


def main_logout(request):
    return render(request, 'main/main_logout.html')
