from django.shortcuts import render

def main(request):
    return render(request, 'study/main.html')


def add_goal(request):
    return render(request, 'study/add_goal.html')
