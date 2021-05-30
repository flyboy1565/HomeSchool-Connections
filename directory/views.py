from directory.forms import FamilyForm
from django.shortcuts import render
from django.forms import inlineformset_factory, formset_factory
import random


from .models import *
from .forms import *

def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)


def index(request):
    return render(request, "directory/home.html", {})

def add_contact(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        parent_formset = ParentFormSet(request.POST, prefix='parent')
        child_formset = ChildrenFormSet(request.POST, prefix='child')
        family = Family()
        print("checking valid")
        if parent_formset.is_valid():
            family_name = ""
            id = str(random.randint(0,9999999))
            for f in parent_formset:
                parent = f.save()
                family_name += f.last_name
                if f.last_name != family_name:
                    family_name += ('-' + f.last_name)
                family.guardian.add(parent)
            for f in child_formset:
                child = f.save()
                family.children.add(child)
            family_name += ('#' + id)
            print('family name:', family_name)
            family.family_nickname = family_name
            family.save()
        else:
            print('Errors were made')
            print(parent_formset.errors)
    else:
        parent_formset = ParentFormSet(prefix='parent')
        child_formset = ChildrenFormSet(prefix='child')
        helper = MyFormSetHelper()
        context = {
            'parent_formset': parent_formset, 
            'parent_count': [i for i in range(0, len(parent_formset.forms))],
            'child_count': [i for i in range(0, len(child_formset.forms))],
            'child_formset': child_formset,
            'helper': helper
        }
        return render(request, 'directory/add_contact.html', context)
    