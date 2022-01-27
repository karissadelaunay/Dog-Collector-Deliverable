# Generated by Django 4.0.1 on 2022-01-26 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='dog',
            name='outfits',
            field=models.ManyToManyField(to='main_app.Outfit'),
        ),
    ]
