# Generated by Django 2.2.9 on 2020-01-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympics', '0006_olympicevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olympicevent',
            name='medal',
            field=models.CharField(choices=[('G', 'Gold'), ('S', 'Silver'), ('B', 'Bronze')], max_length=1, null=True),
        ),
    ]
