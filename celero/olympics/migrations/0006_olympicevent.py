# Generated by Django 2.2.9 on 2020-01-13 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olympics', '0005_athlete'),
    ]

    operations = [
        migrations.CreateModel(
            name='OlympicEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medal', models.CharField(choices=[('G', 'Gold'), ('S', 'Silver'), ('B', 'Bronze')], max_length=1)),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympics.Athlete')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympics.Event')),
                ('olympic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympics.Olympic')),
            ],
        ),
    ]
