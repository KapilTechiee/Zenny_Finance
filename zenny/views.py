from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Transaction
from .forms import TransactionForm

def index(request):
    # Simple home view (keeps the homepage carousel)
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')


def trans(request):
    # show last 15 transactions and aggregated totals
    transactions = Transaction.objects.order_by('-id')[:15]

    total_income = Transaction.objects.filter(category='income').aggregate(total=Sum('amount'))['total'] or 0
    total_expense = Transaction.objects.filter(category='expense').aggregate(total=Sum('amount'))['total'] or 0
    current_balance = total_income - total_expense
    # total_saving = Transaction.objects.filter(category='savings').aggregate(total=Sum('amount'))['total'] or 0

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'current_balance': current_balance,
        # 'total_saving': total_saving,
    }
    return render(request, "trans.html", context)


def add_transaction(request):
    # add transaction form (GET shows form, POST validates and saves)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transactions')   # redirect to transactions listing after save
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

