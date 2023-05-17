# Generated by Django 4.2.1 on 2023-05-15 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=35)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('H', 'High'), ('N', 'Normal'), ('L', 'Low')], default='N', max_length=1)),
                ('done', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
