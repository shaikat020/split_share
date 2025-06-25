from django.db import models

# Create your models here.
from django.db import models

class ExpenseSession(models.Model):
    total_amount = models.FloatField()
    total_persons = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session {self.id} on {self.created_at.date()}"


class ExpenseEntry(models.Model):
    session = models.ForeignKey(ExpenseSession, on_delete=models.CASCADE, related_name='entries')
    name = models.CharField(max_length=100)
    paid = models.FloatField()
    debt = models.FloatField()

    def __str__(self):
        return f"{self.name} - Paid: {self.paid}, Debt: {self.debt}"

