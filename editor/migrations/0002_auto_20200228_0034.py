# Generated by Django 3.0.3 on 2020-02-28 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderform',
            old_name='order_amount',
            new_name='amount',
        ),
        migrations.AddField(
            model_name='orderform',
            name='condo',
            field=models.CharField(choices=[('ccm', 'cruz con mar'), ('miranda', 'miranda'), ('marea34', 'marea34')], default='ccm', max_length=20),
        ),
        migrations.AddField(
            model_name='orderform',
            name='name',
            field=models.CharField(default='ccm', max_length=50),
            preserve_default=False,
        ),
    ]
