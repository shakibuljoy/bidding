from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemFormSet, ComparetiveStatementForm

def create_comparison(request):
    if request.method == 'POST':
        item_formset = ItemFormSet(request.POST, prefix='item')
        comparetive_statement_form = ComparetiveStatementForm(request.POST, prefix='cs')
        
        if item_formset.is_valid() and comparetive_statement_form.is_valid():
            comparetive_statement = comparetive_statement_form.save()
            
            for form in item_formset:
                item = form.save(commit=False)
                item.cs = comparetive_statement
                item.save()
            
            # Handle successful submission (e.g., redirect to a success page)
            return HttpResponse('Succes')
    else:
        item_formset = ItemFormSet(prefix='item')
        comparetive_statement_form = ComparetiveStatementForm(prefix='cs')
    
    return render(request, 'comparison_form.html', {
        'item_formset': item_formset,
        'comparetive_statement_form': comparetive_statement_form
    })
