# Generated by Django 3.0.8 on 2020-09-04 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_auto_20200904_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('value', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
