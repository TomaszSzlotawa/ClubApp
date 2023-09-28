# Generated by Django 4.2.5 on 2023-09-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_players_delete_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=40)),
                ('weight', models.DecimalField(decimal_places=1, max_digits=4)),
                ('height', models.PositiveSmallIntegerField()),
                ('date_of_birth', models.DateField()),
                ('position', models.PositiveSmallIntegerField(choices=[(2, 'Pomocnik'), (1, 'Obrońca'), (0, 'Bramkarz'), (3, 'Napastnik')], default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Players',
        ),
    ]
