# Generated by Django 2.2.19 on 2022-10-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_turi'),
    ]

    operations = [
        migrations.CreateModel(
            name='hoteles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageperfil', models.ImageField(upload_to='hotels/images')),
                ('slide', models.ImageField(upload_to='hotels/images')),
                ('slide1', models.ImageField(upload_to='hotels/images')),
                ('slide2', models.ImageField(upload_to='hotels/images')),
                ('namehotel', models.TextField()),
                ('numeroDeHabitaciones', models.CharField(max_length=30)),
                ('precio', models.CharField(max_length=30)),
                ('desayuno', models.BooleanField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
            ],
        ),
    ]
