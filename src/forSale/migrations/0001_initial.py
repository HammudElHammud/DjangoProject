# Generated by Django 3.0.3 on 2020-03-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forslar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('stats', models.CharField(default='', max_length=40)),
                ('category', models.CharField(default='', max_length=40)),
                ('pric', models.IntegerField(default='')),
                ('size', models.CharField(default='', max_length=40)),
                ('picurl', models.TextField(default='', max_length=50)),
                ('picname', models.TextField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
