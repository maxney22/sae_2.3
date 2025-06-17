from django.db import models
import bleach
# Create your models here.

class CategorieProduit(models.Model):
    id_categorie_produit = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)  # Augmenté à 255 pour correspondre au SQL
    descriptif = models.CharField(max_length=500)

    def __str__(self):
        return self.nom

    def make_dico(self):
        return {
            "id_categorie_produit": self.id_categorie_produit,
            "nom": self.nom,
            "descriptif": self.descriptif
        }

class Produit(models.Model):
    id_produits = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    date_de_peremption = models.DateField()
    photo = models.ImageField(
        upload_to='produits_photos/',
        blank=True,
        null=True
    )  # BinaryField() si vous stockez en BLOB
    marque = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)  # Meilleur que FloatField pour les prix
    id_categorie_produit = models.ForeignKey(CategorieProduit, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Client(models.Model):
    id_clients = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_inscription = models.DateField()
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Commande(models.Model):
    id_commandes = models.AutoField(primary_key=True)
    numero_commande = models.DecimalField(max_digits=10, decimal_places=0)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='id_client')
    date = models.DateField()

    def __str__(self):
        return f"Commande #{self.numero_commande} - {self.id_client.prenom} {self.id_client.nom}"

class CommandeProduit(models.Model):
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE, db_column='id_commande')
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE, db_column='id_produit')
    quantite = models.IntegerField()

    class Meta:
        db_table = 'commande_produits'
        unique_together = (('id_commande', 'id_produit'),)  # Corrigé le nom du champ

    def __str__(self):
        return f"{self.id_produit.nom} - {self.quantite} unité(s)"