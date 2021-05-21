from django.db import models

# Create your models here.
EXPENSE = 'EXP'
INCOME = 'INC'

# TODO: add internalization
TRANSACTION_AVAILABLE_TYPES = [
    (EXPENSE, 'Dépense')
    (INCOME, 'Revenu')
]
# examples fo rubric values: factures, alimentation, dimes, offrandes, salaire, habillement, coiffure, don 
class TransactionRubric(models.Model):
    name = models.CharField(max_length=250)

class Transaction(models.Models):
    title = models.CharField(max_length=250)
    description = models.TextField()
    amount = models.money 
    # TODO: what does auto_now_add means ?, the other options
    created_date = models.DateTimeField(auto_now_add=True)
    rubric = models.ForeignKey(TransactionRubric, on_delete=models.SET_NULL, related_name='transactions')
    transaction_type = models.CharField(
        max_length=3,
        choices=TRANSACTION_AVAILABLE_TYPES,
        default=EXPENSE,
    )

