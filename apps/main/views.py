from django.shortcuts import render
from .models import Header



def index(request):
    header = Header.objects.all()
    return render(request, 'pages/index.html', {'header': header})


from django.contrib.auth.models import User


def create_admin_user(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "sifre123")
        return HttpResponse("Admin user created.")
    return HttpResponse("User already exists.")



from django.http import HttpResponse
from django.core.management import call_command

def run_migrate(request):
    call_command('migrate')
    return HttpResponse("Migrasyon tamamlandı.")
