# Generated by Django 3.1.4 on 2021-03-23 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_auto_20201221_1510'),
        ('projects', '0002_auto_20210101_2218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectimageurl',
            options={'verbose_name': 'Project Image'},
        ),
        migrations.AlterField(
            model_name='project',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='departments.department'),
        ),
    ]
