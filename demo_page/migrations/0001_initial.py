# Generated by Django 4.2.2 on 2023-06-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.CharField(max_length=16)),
                ('visits', models.IntegerField(default=0)),
                ('last_visit', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
