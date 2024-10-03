# Generated by Django 5.1.1 on 2024-10-02 23:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emprendimientos', '0002_delete_comentario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='emprendimientos.articulo')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
