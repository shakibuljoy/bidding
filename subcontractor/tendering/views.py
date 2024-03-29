from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ItemFormSet, ComparetiveStatementForm
from .models import ComparetiveStatement, Item

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
            return redirect('tendering:show-comparison', pk=comparetive_statement.id)
    else:
        item_formset = ItemFormSet(prefix='item')
        comparetive_statement_form = ComparetiveStatementForm(prefix='cs')
    
    return render(request, 'comparison_form.html', {
        'item_formset': item_formset,
        'comparetive_statement_form': comparetive_statement_form
    })


def show_comparison(request, pk):
    cs = ComparetiveStatement.objects.get(pk=pk)
    items = Item.objects.filter(cs=cs)
    app_c = 0

    for item in items:
        if item.apprx_qty is not None:
            if int(item.apprx_qty) > 0:
                app_c += 1

    context = {
        'cs':cs,
        'items':items,
        'app_c': app_c
    }
    return render(request, "show_comparison.html", context)

def show_list(request):
    comparetive_statement = ComparetiveStatement.objects.all()
    context = {
        'comparetive_statement':comparetive_statement
    }
    return render(request, 'index.html', context)