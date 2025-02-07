# Generated by Django 5.0.1 on 2025-01-11 15:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forms', '0003_remove_question_choices_remove_form_created_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('created_at', models.DateField(auto_now=True)),
                ('Updated_at', models.DateField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('choices', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
