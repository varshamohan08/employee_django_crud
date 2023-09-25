# Generated by Django 4.2.5 on 2023-09-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('photo', models.ImageField(blank=True, help_text='Max 5 MB file size', null=True, upload_to='user_photos/', verbose_name='User Photo')),
            ],
        ),
    ]
