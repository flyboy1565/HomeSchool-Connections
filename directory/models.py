from datetime import date
from django.db import models
from django.db.models.enums import Choices
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

def participation_level_choices():
    return (
        ('a', 'All-In'),
        ('b', 'Email Me'),
        ('c', 'Usually Busy'),
    )

def contact_choices():
    return(
        ('e', 'Email'),
        ('p', 'Phone'),
        ('t', 'Text'),
        # ('s', 'Social Media Account'),
    )

def volunteering_types():
    return (
        ('Ft', 'Field Trips'),
        ('T', 'Tutoring'),
        ('S', 'Small Snack'),
        ('SG', 'Study Groups'),
    )

class ParentContact(models.Model):
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    phone_number = PhoneNumberField(_("phone number"),null=True, blank=True)
    email = models.EmailField(_("email"), max_length=254,null=True, blank=True)
    participation_level = models.CharField(_("participation level"), choices=participation_level_choices(), max_length=5)
    volunteering_type_1 = models.CharField(_("Volunteer Type 1"), max_length=5, choices=volunteering_types())
    volunteering_type_2 = models.CharField(_("Volunteer Type 2"), max_length=5, choices=volunteering_types())
    best_contact_option = models.CharField(_('best contact option'), choices=contact_choices(), max_length=5)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Child(models.Model):
    child_name = models.CharField(_("child name"), max_length=50)
    birth_date = models.DateField()
    parent = models.ForeignKey("ParentContact", related_name="children", on_delete=models.CASCADE)
    allergies = models.TextField(null=True, blank=True)
    medical_notes = models.TextField(null=True, blank=True)

    @property
    def age(self):
        today = date.today()
        try: 
            birthday = self.birth_date.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday =  self.birth_date.replace(year=today.year, month= self.birth_date.month+1, day=1)
        if birthday > today:
            return today.year -  self.birth_date.year - 1
        else:
            return today.year -  self.birth_date.year

    def __str__(self):
        return self.child_name
    
    class Meta:
        verbose_name_plural = 'Children'
    

# class SkillSet(models.Model):
#     skill = models.CharField(_("skill"), max_length=50)

#     def __str__(self):
#         return self.skill
    

# class VolunteerType(models.Model):
#     vtype = models.CharField(_("volunteer type"), max_length=50)

#     def __str__(self):
#         return self.vtype
    
