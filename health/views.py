from django.shortcuts import render, get_object_or_404
from .models import Health
from datetime import datetime, timedelta
import datetime


def main(request, goal_id):
    goal = get_object_or_404(Health, pk=goal_id)
    status = get_status(goal)
    board = get_board(goal, status['start_days'])
    context = {
        'goal': goal,
        'start_days': status['start_days'],
        'success_days': status['success_days'],
        'continuity_days': status['continuity_days'],
        'dates': board['dates'],
        'achievements': board['achievements'],
    }
    return render(request, 'health/main.html', context)


def add_goal(request):
    return render(request, 'health/add_goal.html')


def get_status(goal):   # 시작, 성공, 연속 일수를 리턴하는 함수
    certifies = goal.certifies.all()
    start_days = (datetime.date.today() - goal.created).days + 1
    success_days = goal.certifies.filter(achievement=True).count()
    continuity_days = 0
    for i in range(certifies.count()):
        date = datetime.date.today() - timedelta(days=i)  # 오늘부터 거꾸로 가면서 성공했는지 확인
        certify = goal.certifies.filter(created=date)
        if certify.first().achievement:     # 성공했으면 연속 일수를 1씩 증가
            continuity_days += 1
            continue
        else:   # 실패했으면 종료
            break
    res = {
        'start_days': start_days,
        'success_days': success_days,
        'continuity_days': continuity_days,
    }
    return res


def get_board(goal, start_days):    # 도장판의 날짜와 성공 여부를 리턴하는 함수
    dates = []
    achievements = []
    if start_days <= 30:    # 시작한지 1달이 되지 않았으면
        for i in range(30):
            date = goal.created + timedelta(days=i)  # 시작한 날짜부터 오늘까지 날짜를 보여준다
            dates.append(date.strftime('%m/%d'))
            certify = goal.certifies.filter(created=date)
            if certify:  # 날짜에 해당하는 인증이 있으면
                achievements.append(certify.first().achievement)
            else:  # 인증 안 했으면
                if date < datetime.date.today():    # 과거라면
                    achievements.append(False)  # 실천 실패로 처리
                else:   # 미래라면
                    achievements.append(None)     # 아무것도 보여주지 않음
    else:  # 시작한지 1달이 넘었으면
        for i in range(30):
            date = datetime.date.today() - timedelta(days=i)  # 오늘 날짜 이전 30일을 보여준다
            dates.append(date.strftime('%m/%d'))
            certify = goal.certifies.filter(created=date)
            if certify:  # 날짜에 해당하는 인증이 있으면
                achievements.append(certify.first().achievement)
            else:  # 인증 안 했으면
                if date < datetime.date.today():  # 과거라면
                    achievements.append(False)  # 실천 실패로 처리
                else:  # 미래라면
                    achievements.append(None)  # 아무것도 보여주지 않음
    res = {
        'dates': dates,
        'achievements': achievements,
    }
    return res
