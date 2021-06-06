from django.shortcuts import render, redirect
from django.forms import inlineformset_factory, formset_factory
from django.db.models import Count
from django.utils.encoding import force_text

import random


from .models import *
from .forms import *
from .utils import get_vtypes

def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)


def index(request):
    parents = ParentContact.objects.all()
    children = Child.objects.all()
    vtypes = {i[0]:i[1] for i in ParentContact._meta.get_field('volunteering_type_1').choices }
    t1 = ParentContact.objects.values('volunteering_type_1').annotate(count=Count('volunteering_type_1'))
    t2 = ParentContact.objects.values('volunteering_type_2').annotate(count=Count('volunteering_type_2'))
    context = {
        'parents':parents,
        'volunteer_types': get_vtypes(vtypes,t1,t2),
        'children': children
    }
    return render(request, "directory/home.html", context)


def view_contact(request, obj_type, pk):
    if obj_type == 'parent':
        parent = ParentContact.objects.prefetch_related('children').get(pk=pk)
    else:
        parent = ParentContact.objects.prefetch_related('children').get(children__pk=pk)
    context = {
        'parent': parent
    }
    return render(request, 'directory/view_contact.html', context)    


def add_contact(request):
    if request.method == 'POST':
        parent_form = ParentContactForm(request.POST, prefix='parent')
        child_form = ChildForm(request.POST, prefix='child')
        if parent_form.is_valid() and child_form.is_valid:
            parent = parent_form.save()
            child = child_form.save(commit=False)
            child.parent = parent
            child.save()
            return redirect(index)
        else:
            print(parent_form.errors)
            print(child_form.errors)
    else:
        parent_form = ParentContactForm(prefix='parent')
        child_form = ChildForm(prefix='child')
        helper = MyFormSetHelper()
        context = {
            'parent_form': parent_form, 
            'child_form': child_form,
            'helper': helper
        }
        return render(request, 'directory/add_contact.html', context)
    