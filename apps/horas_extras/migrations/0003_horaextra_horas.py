# Generated by Django 4.1.3 on 2022-11-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas_extras', '0002_horaextra_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='horaextra',
            name='horas',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
