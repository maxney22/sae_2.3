from django.urls import path, include
from . import views
from django.shortcuts import redirect

urlpatterns = [

    path('produit/importer/', views.importer_produits, name='importer_produits'),

    path('commande/<int:pk>/exporter/', views.exporter_commande_txt, name='exporter_commande_txt'),

    path('', views.accueil, name='accueil'),
    path('categorie/', views.liste_categories, name='liste_categories'),

     # URLs pour CategorieProduit
    path('categorie/', views.liste_categories, name='liste_categories'),
    path('categorie/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('categorie/<int:pk>/', views.detail_categorie, name='detail_categorie'),
    path('categorie/<int:pk>/modifier/', views.modifier_categorie, name='modifier_categorie'),
    path('categorie/<int:pk>/supprimer/', views.supprimer_categorie, name='supprimer_categorie'),

    # URLs pour Produit
    path('produit/', views.liste_produits, name='liste_produits'),
    path('produit/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('produit/<int:pk>/', views.detail_produit, name='detail_produit'),
    path('produit/<int:pk>/modifier/', views.modifier_produit, name='modifier_produit'),
    path('produit/<int:pk>/supprimer/', views.supprimer_produit, name='supprimer_produit'),

    # URLs pour Client
    path('client/', views.liste_clients, name='liste_clients'),
    path('client/ajouter/', views.ajouter_client, name='ajouter_client'),
    path('client/<int:pk>/', views.detail_client, name='detail_client'),
    path('client/<int:pk>/modifier/', views.modifier_client, name='modifier_client'),
    path('client/<int:pk>/supprimer/', views.supprimer_client, name='supprimer_client'),

    # URLs pour Commande
    path('commande/', views.liste_commandes, name='liste_commandes'),
    path('commande/ajouter/', views.ajouter_commande, name='ajouter_commande'),
    path('commande/<int:pk>/', views.detail_commande, name='detail_commande'),
    path('commande/<int:pk>/modifier/', views.modifier_commande, name='modifier_commande'),
    path('commande/<int:pk>/supprimer/', views.supprimer_commande, name='supprimer_commande'),

    # URLs pour CommandeProduit
    path('ligne-commande/ajouter/', views.ajouter_ligne_commande, name='ajouter_ligne_commande'),
    path('ligne-commande/<int:pk>/supprimer/', views.supprimer_ligne_commande, name='supprimer_ligne_commande'),
]