# Generated by Django 5.0.7 on 2024-10-11 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_review_owner_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
