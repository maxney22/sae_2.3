# Generated by Django 5.2.3 on 2025-06-11 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieProduit',
            fields=[
                ('id_categorie_produit', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('descriptif', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_clients', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_inscription', models.DateField()),
                ('adresse', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id_commandes', models.AutoField(primary_key=True, serialize=False)),
                ('numero_commande', models.DecimalField(decimal_places=0, max_digits=10)),
                ('date', models.DateField()),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driveapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id_produits', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('date_de_peremption', models.DateField()),
                ('photo', models.ImageField(upload_to='produits_photos/')),
                ('marque', models.CharField(max_length=100)),
                ('prix', models.FloatField()),
                ('id_categorie_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driveapp.categorieproduit')),
            ],
        ),
        migrations.CreateModel(
            name='CommandeProduit',
            fields=[
                ('id_commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='driveapp.commande')),
                ('quantite', models.IntegerField()),
                ('id_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driveapp.produit')),
            ],
            options={
                'unique_together': {('id_commande', 'id_produit')},
            },
        ),
    ]
