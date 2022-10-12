from django.shortcuts import render

from contest_app.models import ContestParticipant, ContestTeam

# Create your views here.


def index(request):
    return render(request, 'contest_app/home.html')


def about(request):
    return render(request, 'contest_app/about.html')


def register(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name', '')
        team_course = request.POST.get('team_course', '')
        if team_name == '' or team_course == '' or team_course == 'Choose...':
            message = 'Please fill all fields'
            return render(request, 'contest_app/register.html', {'message': message})
        if ContestTeam.objects.filter(name=team_name).exists():
            message = 'Team name already exists'
            return render(request, 'contest_app/register.html', {'message': message})
        ContestTeam.objects.create(name=team_name, course=team_course)
        first_fullname = request.POST.get('first_fullname', '')
        first_phone = request.POST.get('first_phone', '')
        if first_fullname == '' or first_phone == '':
            message = 'Team Leader name and phone number are required!'
            return render(request, 'contest_app/register.html', {'message': message})
        if ContestParticipant.objects.filter(phone=first_phone).exists():
            message = 'Team Leader with this phone number already exists'
            return render(request, 'contest_app/register.html', {'message': message})
        ContestParticipant.objects.create(
            name=first_fullname, team=ContestTeam.objects.get(name=team_name), phone=first_phone, is_leader=True)
        second_fullname = request.POST.get('second_fullname', '')
        second_phone = request.POST.get('second_phone', '')
        if second_fullname != '' and second_phone != '':
            if ContestParticipant.objects.filter(phone=second_phone).exists():
                message = 'Team Co-founder with this phone number already exists'
                return render(request, 'contest_app/register.html', {'message': message})
            ContestParticipant.objects.create(
                name=second_fullname, team=ContestTeam.objects.get(name=team_name), phone=second_phone, is_leader=False)
        return render(request, 'contest_app/timer.html', context={'team_name': team_name})
    return render(request, 'contest_app/register.html')


def timer(request):
    return render(request, 'contest_app/timer.html')


def certificate(request):
    return render(request, 'contest_app/certificate.html')


def task_1(request):
    return render(request, 'contest_app/task_1.html')


def task_2(request):
    return render(request, 'contest_app/task_2.html')
