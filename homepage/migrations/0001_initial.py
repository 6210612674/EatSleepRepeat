# Generated by Django 3.2.7 on 2021-10-30 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('active', models.BooleanField(default=True)),
                ('F_id', models.AutoField(primary_key=True, serialize=False)),
                ('F_name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('description', models.CharField(max_length=150)),
                ('category', models.IntegerField(choices=[(1, 'Maincourse'), (2, 'Appetizer'), (3, 'Dessert'), (4, 'Drink')])),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('O_id', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_id', models.CharField(max_length=30)),
                ('paymentOptions', models.IntegerField(choices=[(1, 'Cash'), (2, 'Ecommerce')])),
                ('pickup', models.IntegerField(choices=[(1, 'Pick Up'), (2, 'Delivery')])),
            ],
        ),
    ]
