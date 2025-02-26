# Generated by Django 4.1.10 on 2023-08-29 11:59

from django.db import migrations
from django.db.models import F, Value, Count
from django.db.models.functions import Concat
from django_scopes import scopes_disabled


def migrate_icons(apps, schema_editor):
    with scopes_disabled():
        MealType = apps.get_model('cookbook', 'MealType')
        Keyword = apps.get_model('cookbook', 'Keyword')
        PropertyType = apps.get_model('cookbook', 'PropertyType')
        RecipeBook = apps.get_model('cookbook', 'RecipeBook')

        duplicate_meal_types = MealType.objects.values('name').annotate(name_count=Count('name')).exclude(name_count=1).all()
        if len(duplicate_meal_types) > 0:
            raise RuntimeError(f'Duplicate MealTypes found, please remove/rename them and run migrations again/restart the container. {duplicate_meal_types}')
        MealType.objects.update(name=Concat(F('icon'), Value(' '), F('name')))

        duplicate_meal_types = Keyword.objects.values('name').annotate(name_count=Count('name')).exclude(name_count=1).all()
        if len(duplicate_meal_types) > 0:
            raise RuntimeError(f'Duplicate Keyword found, please remove/rename them and run migrations again/restart the container. {duplicate_meal_types}')
        Keyword.objects.update(name=Concat(F('icon'), Value(' '), F('name')))

        duplicate_meal_types = PropertyType.objects.values('name').annotate(name_count=Count('name')).exclude(name_count=1).all()
        if len(duplicate_meal_types) > 0:
            raise RuntimeError(f'Duplicate PropertyType found, please remove/rename them and run migrations again/restart the container. {duplicate_meal_types}')
        PropertyType.objects.update(name=Concat(F('icon'), Value(' '), F('name')))

        duplicate_meal_types = RecipeBook.objects.values('name').annotate(name_count=Count('name')).exclude(name_count=1).all()
        if len(duplicate_meal_types) > 0:
            raise RuntimeError(f'Duplicate RecipeBook found, please remove/rename them and run migrations again/restart the container. {duplicate_meal_types}')
        RecipeBook.objects.update(name=Concat(F('icon'), Value(' '), F('name')))


class Migration(migrations.Migration):
    dependencies = [
        ('cookbook', '0199_alter_propertytype_options_alter_automation_type_and_more'),
    ]

    operations = [
        migrations.RunPython( migrate_icons),
        migrations.AlterModelOptions(
            name='propertytype',
            options={'ordering': ('order',)},
        ),
        migrations.RemoveField(
            model_name='keyword',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='mealtype',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='propertytype',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='recipebook',
            name='icon',
        ),
    ]
