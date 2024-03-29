# Generated by Django 5.0.2 on 2024-02-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_saloon', '0013_image_delete_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
