# Generated by Django 4.0.2 on 2022-02-10 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommercialTeam',
        ),
        migrations.DeleteModel(
            name='ManagementTeam',
        ),
        migrations.DeleteModel(
            name='SupportTeam',
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
