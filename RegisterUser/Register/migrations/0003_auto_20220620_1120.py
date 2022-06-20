# Generated by Django 3.2.13 on 2022-06-20 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0002_auto_20220620_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='UserAccounts',
        ),
    ]
