# Generated by Django 5.0.2 on 2024-02-17 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_saloon', '0007_rename_linedin_link_profile_linkedin_link_profile_x_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='x',
            new_name='x_link',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='youtube',
            new_name='youtube_link',
        ),
    ]