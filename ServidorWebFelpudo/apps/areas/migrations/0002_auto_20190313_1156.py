# Generated by Django 2.0.4 on 2019-03-13 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datos', '0001_initial'),
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion_orden',
            name='sesion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.SESION'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areas.AREA'),
        ),
    ]
