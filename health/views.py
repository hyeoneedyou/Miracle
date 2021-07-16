from django.shortcuts import render

def main(request):
    return render(request, 'health/main.html')


def add_goal(request):
    return render(request, 'health/add_goal.html')
