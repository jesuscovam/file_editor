# Generated by Django 3.0.3 on 2020-02-28 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_amount', models.CharField(choices=[('0', 'zero'), ('1', 'one'), ('2', 'two'), ('3', 'three')], max_length=1)),
            ],
        ),
    ]
