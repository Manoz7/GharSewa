# Generated by Django 3.2 on 2021-08-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_delete_bookservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_man',
            name='cert',
            field=models.FileField(default='service_man/certificate.png', null=True, upload_to='service_man/'),
        ),
    ]
