# Generated by Django 3.0.3 on 2020-02-24 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_favorite_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='PlotNo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Plot'),
        ),
    ]