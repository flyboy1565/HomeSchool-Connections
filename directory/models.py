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

class Family(models.Model):
    family_nickname = models.CharField(max_length=50, unique=True)
    guardian = models.ForeignKey("ParentContact", related_name="parents", on_delete=models.CASCADE)
    children = models.ForeignKey("Child", related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.family_nickname

    class Meta:
        verbose_name_plural = 'Familes'
    

class ParentContact(models.Model):
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=60)
    phone_number = PhoneNumberField(_("phone number"),null=True, blank=True)
    email = models.EmailField(_("email"), max_length=254,null=True, blank=True)
    participation_level = models.CharField(_("participation level"), choices=participation_level_choices(), max_length=5)
    volunteering_type = models.ManyToManyField("VolunteerType", related_name='volunteering_types')
    best_contact_option = models.CharField(_('best contact option'), choices=contact_choices(), max_length=5)
    skills = models.ManyToManyField("SkillSet", related_name='skills')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Child(models.Model):
    child_name = models.CharField(_("child name"), max_length=50)
    birth_date = models.DateField()
    allergies = models.TextField(null=True, blank=True)
    medical_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.child_name
    
    class Meta:
        verbose_name_plural = 'Children'
    

class SkillSet(models.Model):
    skill = models.CharField(_("skill"), max_length=50)

    def __str__(self):
        return self.skill
    

class VolunteerType(models.Model):
    vtype = models.CharField(_("volunteer type"), max_length=50)

    def __str__(self):
        return self.vtype
    
