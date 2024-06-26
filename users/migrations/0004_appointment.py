# Generated by Django 4.1.5 on 2024-05-10 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_blog_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_speciality', models.CharField(choices=[('Cardiology', 'Cardiology'), ('Dermatology', 'Dermatology'), ('Endocrinology', 'Endocrinology'), ('Gastroenterology', 'Gastroenterology'), ('Hematology', 'Hematology')], max_length=50)),
                ('date_of_appointment', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
