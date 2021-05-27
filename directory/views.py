from directory.forms import FamilyForm
from django.shortcuts import render
from django.forms import inlineformset_factory, formset_factory

from .models import *
from .forms import *

def index(request):
    return render(request, "directory/home.html", {})

def add_contact(request):
    parent_formset = ParentFormSet(prefix='parent')
    child_formset = ChildrenFormSet(prefix='child')
    helper = MyFormSetHelper()
    context = {
        'parent_formset': parent_formset, 
        'child_formset': child_formset,
        'helper': helper
    }
    return render(request, 'directory/add_contact.html', context)
    """
    if request.method == 'POST':
        pass
    else:
        family_form = FamilyForm(prefix='family')
        parent_formset = ParentContactFormSet(prefix='parent')
        children_formset = ChildFormSet(prefix='children')
        return render(request, 'directory/add_contact.html', {
            'family_form': family_form,
            'parent_formset': parent_formset,
            'children_formset': children_formset
        })        
    return render()
    """