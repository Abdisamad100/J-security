# Generated by Django 3.0.5 on 2021-11-19 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juba', '0009_auto_20211108_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='police',
            name='blood_group',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='police',
            name='district',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='police',
            name='gun_patch_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='police',
            name='number_of_magazine',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='police',
            name='unique_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
