# Generated by Django 4.1.3 on 2022-11-12 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_alter_funcionario_empresa'),
        ('documentos', '0002_documento_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
        ),
    ]
