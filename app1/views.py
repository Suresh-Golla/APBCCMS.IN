from django.shortcuts import render

# Create your views here.
from app1.models import Registration


def home(request):
    return render(request, '1.html')

def Register(request):

    if request.method == 'POST':
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        mobile = request.POST["mobile"]
        gender = request.POST["gender"]
        reg = Registration(firstname=firstname,
                           lastname=lastname,
                           email=email,
                           password=password,
                           mobile=mobile,
                           gender=gender)

        reg.register()
        return render(request, 'register.html')

    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')


def jobs(request):
    data = Registration.objects.all()
    return render(request, 'jobs.html', {'data':data})


def training(request):
    data = Registration.objects.all()
    return render(request, 'trainingskills.html', {'data': data})

    #return render(request, 'trainingskills.html')


def jobsmela(request):
    return render(request, 'jobmela.html')


def reports(request):
    return render(request, 'reports.html')


def helpdesk(request):
    return render(request, 'helpdesk.html')


def contacts(request):
    return render(request, 'contacts.html')

def updates(request):
    return render(request, 'updates.html')

