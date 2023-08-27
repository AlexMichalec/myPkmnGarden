# Generated by Django 4.2.4 on 2023-08-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0007_alter_pokemonspecies_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonspecies',
            name='if_genderless',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonmonster',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('UNKNOWN', 'Unknown')], default='MALE', max_length=7),
        ),
    ]
