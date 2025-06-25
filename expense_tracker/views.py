# tracker/views.py
from django.shortcuts import render
from .models import ExpenseSession, ExpenseEntry
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'POST':
        total_amount = float(request.POST.get('total_amount'))
        total_persons = int(request.POST.get('total_persons'))

        session = ExpenseSession.objects.create(
            total_amount=total_amount,
            total_persons=total_persons
        )

        people = []
        for i in range(total_persons):
            name = request.POST.get(f'name_{i}')
            paid = float(request.POST.get(f'paid_{i}'))
            people.append({'name': name, 'paid': paid})

        share = total_amount / total_persons

        for p in people:
            debt = round(p['paid'] - share, 2)
            p['debt'] = debt
            ExpenseEntry.objects.create(
                session=session,
                name=p['name'],
                paid=p['paid'],
                debt=debt
            )

        return render(request, 'result.html', {'people': people})

    return render(request, 'index.html')
