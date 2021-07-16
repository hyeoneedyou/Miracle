from django.shortcuts import render

def main(request):
    return render(request, 'free/main.html')


def add_goal(request):
    return render(request, 'free/add_goal.html')
