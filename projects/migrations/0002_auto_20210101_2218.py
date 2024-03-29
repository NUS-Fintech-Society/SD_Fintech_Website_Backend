# Generated by Django 3.1.4 on 2021-01-01 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimageurl',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='projectimageurl',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imageUrls', to='projects.project'),
        ),
    ]
