# Generated by Django 3.0.1 on 2020-04-01 19:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('stats', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayir')], default='', max_length=40)),
                ('keyword', models.CharField(default='', max_length=40)),
                ('description', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('slug', models.SlugField()),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
                ('parant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='forSale.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Forslar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('stats', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayir')], default='', max_length=40)),
                ('category', models.CharField(default='', max_length=40)),
                ('pric', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default='')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('size', models.CharField(default='', max_length=40)),
                ('picurl', models.TextField(default='', max_length=50)),
                ('picname', models.TextField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=200)),
                ('slug', models.SlugField()),
                ('createAt', models.DateField(default=datetime.datetime(2020, 4, 1, 19, 33, 1, 681951, tzinfo=utc))),
                ('updateAt', models.DateField(default=datetime.datetime(2020, 4, 1, 19, 33, 1, 681951, tzinfo=utc))),
                ('categoryadmin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forSale.Category')),
                ('parant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='forSale.Forslar')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=22)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forSale.Forslar')),
            ],
        ),
    ]
