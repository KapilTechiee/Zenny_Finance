# from django.db import models

# CATEGORY_CHOICES = [
#     ('income', 'Income'),
#     ('expense', 'Expense'),
#     ('savings', 'Saving'),   
# ]
# STATUS_CHOICES = [
#     ('complete', 'Completed'),
#     ('pending', 'Pending'),
# ]
# class Transaction(models.Model):
#     date = models.DateField(auto_now_add=True)
#     description = models.CharField(max_length=255)
#     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
#     def __str__(self):
#         return f"{self.description} - {self.amount}"



from django.db import models

CATEGORY_CHOICES = [
    ('income', 'Income'),
    ('expense', 'Expense'),
]

STATUS_CHOICES = [
    ('complete', 'Completed'),
    ('pending', 'Pending'),
]

class Transaction(models.Model):
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='complete')

    def __str__(self):
        return f"{self.description} - {self.amount}"
