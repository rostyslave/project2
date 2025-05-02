from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    """Модель для послуг ремонту"""
    name = models.CharField(max_length=100, verbose_name="Назва послуги")
    description = models.TextField(verbose_name="Опис послуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"


class Device(models.Model):
    """Модель для пристроїв користувачів"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Власник")
    name = models.CharField(max_length=100, verbose_name="Назва пристрою")
    model = models.CharField(max_length=100, verbose_name="Модель")
    serial_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Серійний номер")
    purchase_date = models.DateField(blank=True, null=True, verbose_name="Дата придбання")
    description = models.TextField(blank=True, null=True, verbose_name="Додаткова інформація")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def __str__(self):
        return f"{self.name} - {self.model}"

    class Meta:
        verbose_name = "Пристрій"
        verbose_name_plural = "Пристрої"


class RepairOrder(models.Model):
    """Модель для замовлень ремонту (техніка у ремонті)"""
    STATUS_CHOICES = [
        ('pending', 'Очікує обробки'),
        ('diagnosed', 'Діагностовано'),
        ('in_progress', 'В роботі'),
        ('completed', 'Завершено'),
        ('cancelled', 'Скасовано'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Замовник")
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name="Пристрій")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Послуга")
    issue_description = models.TextField(verbose_name="Опис проблеми")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    notes = models.TextField(blank=True, null=True, verbose_name="Примітки")

    def __str__(self):
        return f"Ремонт #{self.id} - {self.device}"

    class Meta:
        verbose_name = "Замовлення ремонту"
        verbose_name_plural = "Замовлення ремонту"


class ContactInfo(models.Model):
    """Модель для контактної інформації сервісних центрів"""
    name = models.CharField(max_length=100, verbose_name="Назва сервісного центру")
    address = models.CharField(max_length=200, verbose_name="Адреса")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    working_hours = models.CharField(max_length=200, verbose_name="Робочі години")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контактна інформація"
        verbose_name_plural = "Контактна інформація"
