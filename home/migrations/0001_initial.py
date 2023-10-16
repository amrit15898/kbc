# Generated by Django 4.2.6 on 2023-10-13 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(max_length=200)),
                ('is_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Questiom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField()),
                ('answers', models.ManyToManyField(to='home.answers')),
            ],
        ),
    ]