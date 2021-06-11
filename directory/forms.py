from django.forms import ModelForm
from django.forms import modelformset_factory
from django.forms.models import modelform_factory

from crispy_forms.helper import FormHelper, Layout

from .models import *

# class FamilyForm(ModelForm):
#     class Meta:
#         model = Family
#         fields = '__all__'


class ParentContactForm(ModelForm):
    class Meta:
        model = ParentContact
        fields = '__all__'


class ChildForm(ModelForm):
    class Meta:
        model = Child
        fields = ('first_name', 'last_name', 'birth_date', 'allergies', 'medical_notes')


class MyFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(MyFormSetHelper, self).__init__(*args, **kwargs)
        self.template = 'bootstrap/table_inline_formset.html'

