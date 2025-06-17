from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms
from django.forms import inlineformset_factory

# Formulaire pour la catégorie
class CategorieProduitForm(ModelForm):
    class Meta:
        model = models.CategorieProduit
        fields = ['id_categorie_produit', 'nom', 'descriptif']
        labels = {
            'id_categorie_produit': _('ID catégorie'),
            'nom': _('Nom'),
            'descriptif': _('Descriptif'),
        }

# Formulaire pour les produits
class ProduitForm(ModelForm):
    class Meta:
        model = models.Produit
        fields = ['id_produits', 'nom', 'date_de_peremption', 'photo', 'marque', 'prix', 'id_categorie_produit']
        labels = {
            'id_produits': _('ID Produit'),
            'nom': _('Nom'),
            'date_de_peremption': _('Date de péremption'),
            'photo': _('Photo'),
            'marque': _('Marque'),
            'prix': _('Prix'),
            'id_categorie_produit': _('Catégorie'),
        }
        widgets = {
            'photo': forms.FileInput(attrs={'accept': 'image/*'}),
        }

# Formulaire pour les clients
class ClientForm(ModelForm):
    class Meta:
        model = models.Client
        fields = ['id_clients', 'nom', 'prenom', 'date_inscription', 'adresse']
        labels = {
            'id_clients': _('ID Client'),
            'nom': _('Nom'),
            'prenom': _('Prénom'),
            'date_inscription': _('Date d\'inscription'),
            'adresse': _('Adresse'),
        }

# Formulaire pour les commandes
class CommandeForm(ModelForm):
    class Meta:
        model = models.Commande
        fields = ['id_commandes', 'numero_commande', 'id_client', 'date']
        labels = {
            'id_commandes': _('ID Commande'),
            'numero_commande': _('Numéro'),
            'id_client': _('Client'),
            'date': _('Date'),
        }

# Formulaire pour les lignes de commande
class CommandeProduitForm(ModelForm):
    class Meta:
        model = models.CommandeProduit
        fields = ['id_produit', 'quantite']
        labels = {
            'id_produit': _('Produit'),
            'quantite': _('Quantité'),
        }

CommandeProduitFormSet = inlineformset_factory(
    parent_model=models.Commande,
    model=models.CommandeProduit,
    form=CommandeProduitForm,
    extra=3,  # Nombre de lignes de produits à afficher
    can_delete=True
)