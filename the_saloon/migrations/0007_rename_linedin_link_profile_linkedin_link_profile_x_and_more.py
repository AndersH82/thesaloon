# Generated by Django 5.0.2 on 2024-02-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_saloon', '0006_profile_facebook_link_profile_instagram_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='linedin_link',
            new_name='linkedin_link',
        ),
        migrations.AddField(
            model_name='profile',
            name='x',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]