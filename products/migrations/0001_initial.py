# Generated by Django 2.1 on 2021-11-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('price', models.CharField(max_length=10)),
                ('hsn', models.CharField(max_length=100)),
                ('cgst', models.CharField(max_length=100)),
                ('sgst', models.CharField(max_length=100)),
                ('igst', models.CharField(max_length=100)),
                ('cess', models.CharField(max_length=100)),
            ],
        ),
    ]
