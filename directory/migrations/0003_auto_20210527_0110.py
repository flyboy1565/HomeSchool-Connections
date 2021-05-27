# Generated by Django 3.2.3 on 2021-05-27 01:10

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_auto_20210526_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentcontact',
            name='best_contact_option',
            field=models.CharField(choices=[('e', 'Email'), ('p', 'Phone'), ('t', 'Text')], max_length=5, verbose_name='best contact option'),
        ),
        migrations.AlterField(
            model_name='parentcontact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='parentcontact',
            name='participation_level',
            field=models.CharField(choices=[('a', 'All-In'), ('b', 'Email Me'), ('c', 'Usually Busy')], max_length=5, verbose_name='participation level'),
        ),
        migrations.AlterField(
            model_name='parentcontact',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='phone number'),
        ),
    ]