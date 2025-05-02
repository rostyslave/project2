from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .models import Service, Device, RepairOrder, ContactInfo
from .forms import UserRegistrationForm, DeviceForm, RepairOrderForm



def home(request):
    """Головна сторінка"""
    services = Service.objects.all()[:3]  # Показати 3 послуги на головній
    return render(request, 'repair_app/home.html', {'services': services})


def services(request):
    """Сторінка з послугами"""
    services = Service.objects.all()
    return render(request, 'repair_app/services.html', {'services': services})


def contacts(request):
    """Сторінка з контактною інформацією"""
    contacts = ContactInfo.objects.all()
    return render(request, 'repair_app/contacts.html', {'contacts': contacts})


def register(request):
    """Реєстрація нового користувача"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Реєстрація успішна!")
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'repair_app/register.html', {'form': form})



@login_required
def device_list(request):
    """Список пристроїв користувача"""
    devices = Device.objects.filter(user=request.user)
    return render(request, 'repair_app/device_list.html', {'devices': devices})


@login_required
def device_create(request):
    """Створення нового пристрою"""
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.user = request.user
            device.save()
            messages.success(request, "Пристрій успішно додано!")
            return redirect('device_list')
    else:
        form = DeviceForm()
    return render(request, 'repair_app/device_form.html', {'form': form})


@login_required
def device_edit(request, device_id):
    """Редагування пристрою"""
    device = get_object_or_404(Device, id=device_id, user=request.user)

    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            messages.success(request, "Пристрій успішно оновлено!")
            return redirect('device_list')
    else:
        form = DeviceForm(instance=device)

    return render(request, 'repair_app/device_form.html', {
        'form': form,
        'edit_mode': True,
        'device': device
    })


@login_required
def repair_list(request):
    """Список замовлень ремонту користувача"""
    repairs = RepairOrder.objects.filter(user=request.user)
    return render(request, 'repair_app/repair_list.html', {'repairs': repairs})


@login_required
def repair_create(request):
    """Створення замовлення ремонту"""
    if request.method == 'POST':
        form = RepairOrderForm(request.user, request.POST)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.user = request.user
            repair.save()
            messages.success(request, "Замовлення ремонту успішно створено!")
            return redirect('repair_list')
    else:
        form = RepairOrderForm(request.user)

    return render(request, 'repair_app/repair_form.html', {'form': form})


@login_required
def repair_detail(request, repair_id):
    """Деталі замовлення ремонту"""
    repair = get_object_or_404(RepairOrder, id=repair_id, user=request.user)
    return render(request, 'repair_app/repair_detail.html', {'repair': repair})