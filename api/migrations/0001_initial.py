# Generated by Django 5.0.3 on 2024-03-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('organizationName', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=20)),
                ('profits', models.DecimalField(decimal_places=2, max_digits=20)),
                ('assets', models.DecimalField(decimal_places=2, max_digits=20)),
                ('marketValue', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
