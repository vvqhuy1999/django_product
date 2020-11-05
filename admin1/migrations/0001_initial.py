# Generated by Django 3.1.2 on 2020-11-03 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=200, verbose_name='Tên')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=200, verbose_name='Tên')),
                ('price', models.FloatField(verbose_name='Đơn giá')),
                ('image', models.ImageField(upload_to='static/images', verbose_name='Ảnh mẫu')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin1.category')),
            ],
        ),
    ]
