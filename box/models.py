from django.db import models



class Box(models.Model):
    title = models.CharField(max_length=255)
    token = models.SlugField(unique=True)
    cash = models.PositiveIntegerField(default=0)
    on = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"


class Customer(models.Model):
    turniket_id = models.CharField(max_length=16)
    cash_back = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.turniket_id} {self.cash_back}"


class CashBack(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.amount}"


class Income(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField(default=0)
    box = models.ForeignKey(Box, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.amount}"


class TakenMoney(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at} {self.amount}"



