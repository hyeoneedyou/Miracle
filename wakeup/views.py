from django.shortcuts import render

def main(request):
    return render(request, 'wakeup/main.html')


def add_goal(request):
    return render(request, 'wakeup/add_goal.html')

def verify(request):
    return render(request, 'wakeup/verify.html')
