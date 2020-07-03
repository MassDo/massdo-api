# Generated by Django 3.0.7 on 2020-07-03 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('numero_siret', models.IntegerField()),
                ('adresse', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('unite', models.CharField(max_length=50)),
                ('codification_internationnale', models.CharField(max_length=50)),
                ('producteurs', models.ManyToManyField(to='api.Farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('biologique', 'biologique'), ('sans ogm', 'sans ogm'), ('origine', 'origine')], max_length=50)),
                ('farmer_certifie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Farmer')),
            ],
        ),
    ]
