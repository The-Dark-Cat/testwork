# Generated by Django 3.1.5 on 2021-02-04 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversionrate',
            options={'verbose_name': 'Коэффециент конверсии', 'verbose_name_plural': 'Коэффециент конверсии'},
        ),
        migrations.AlterModelOptions(
            name='counterparty',
            options={'verbose_name': 'Контрагенты', 'verbose_name_plural': 'Контрагенты'},
        ),
        migrations.AlterModelOptions(
            name='nomenclature',
            options={'verbose_name': 'Номенклатура материалов и ГП', 'verbose_name_plural': 'Номенклатура материалов и ГП'},
        ),
        migrations.AlterModelOptions(
            name='production',
            options={'verbose_name': 'отчет производства', 'verbose_name_plural': 'отчет производства'},
        ),
        migrations.AlterModelOptions(
            name='productionconsumed',
            options={'verbose_name': 'Списанные материалы', 'verbose_name_plural': 'Списанные материалы'},
        ),
        migrations.AlterModelOptions(
            name='productionproduced',
            options={'verbose_name': 'Произведенная продукция', 'verbose_name_plural': 'Произведенная продукция'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Закупки', 'verbose_name_plural': 'Закупки'},
        ),
        migrations.AlterModelOptions(
            name='uom',
            options={'verbose_name': 'Еденицы измерения', 'verbose_name_plural': 'Еденицы измерения'},
        ),
        migrations.AddField(
            model_name='productionconsumed',
            name='consumed_uom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='myfirstapp.uom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productionproduced',
            name='produced_uom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='myfirstapp.uom'),
            preserve_default=False,
        ),
    ]