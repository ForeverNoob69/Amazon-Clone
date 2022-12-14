# Generated by Django 4.0.3 on 2022-07-26 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_remove_orderitem_product_orderitem_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(blank=True, max_length=200, null=True)),
                ('product_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
