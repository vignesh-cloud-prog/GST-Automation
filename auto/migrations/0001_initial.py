# Generated by Django 2.1 on 2021-10-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GST_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsn', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('cgst', models.CharField(max_length=100)),
                ('sgst', models.CharField(max_length=100)),
                ('igst', models.CharField(max_length=100)),
                ('cess', models.CharField(max_length=100)),
            ],
        ),
    ]
