from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

from .forms import UserForm
from .models import App, Projects


def index(request):
    return render(request, 'main/main_page.html')


def projects(request):
    all_projects = Projects.objects.all().order_by('-name')
    page = request.GET.get('page', 1)

    paginator = Paginator(all_projects, 8)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'main/projects_page.html', {'projects': users})


def cooperation(request):
    return render(request, 'main/get_form.html')


def emp_form(request):
    form = UserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            body = {
                'name': form.cleaned_data['Name'],
                'email': form.cleaned_data['Email'],
                'message': form.cleaned_data['Message'],
            }
            message = f"Користувач {body['name']} надіслав(-ла) повідомлення: {body['message']}\n''." \
                      f"\n\nПошта для зв'язку: {body['email']} "
            form.save()
            send_mail('Замовлення проекту', message, 'buildcompany0@gmail.com', ['buildcompany0@gmail.com'])
            messages.success(request, f"Повідомлення надіслано. Відповідь очікуйте на email: {body['email']}")
        else:
            messages.error(request, "Повідомлення не надіслано. Неправильно вказане ім'я")
    form = UserForm()
    return render(request, 'main/get_form.html', {'form': form})


def one_project(request, name):
    info_project = get_object_or_404(App, name=name)
    return render(request, 'main/info_project_page.html', {'project': info_project})
