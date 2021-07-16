from django.shortcuts import render

def main(request):
    return render(request, 'book/main.html')


def add_goal(request):
    return render(request, 'book/add_goal.html')
