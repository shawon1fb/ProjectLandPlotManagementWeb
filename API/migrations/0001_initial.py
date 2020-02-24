# Generated by Django 3.0.3 on 2020-02-24 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plotNo', models.TextField()),
                ('plotId', models.TextField()),
                ('plotName', models.TextField()),
                ('plotSize', models.TextField()),
                ('plot_RsLine', models.TextField()),
                ('plotOwner', models.TextField()),
                ('plotStatus', models.TextField()),
                ('plotPic', models.ImageField(upload_to='')),
            ],
        ),
    ]