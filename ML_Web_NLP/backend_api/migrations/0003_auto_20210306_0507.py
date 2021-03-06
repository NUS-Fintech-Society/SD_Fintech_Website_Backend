# Generated by Django 3.1.4 on 2021-03-06 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0002_auto_20210306_0442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='id',
        ),
        migrations.RemoveField(
            model_name='headlines',
            name='company_id',
        ),
        migrations.AddField(
            model_name='headlines',
            name='company_name',
            field=models.ForeignKey(default='temp', on_delete=django.db.models.deletion.CASCADE, to='backend_api.companies'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='headlines',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companies',
            name='company_name',
            field=models.CharField(max_length=500, primary_key=True, serialize=False, unique=True),
        ),
    ]
