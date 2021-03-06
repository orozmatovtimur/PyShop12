# Generated by Django 3.1 on 2021-07-21 09:50

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
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('in stock', 'В наличии'), ('out of stock', 'нет в наличии'), ('awaiting', 'Ожидается')], max_length=20)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category')),
            ],
        ),
    ]
