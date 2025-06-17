from django.shortcuts import render, redirect, get_object_or_404
import csv
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import CategorieProduit, Produit, Client, Commande, CommandeProduit
from .forms import CategorieProduitForm, ProduitForm, ClientForm, CommandeForm, CommandeProduitForm, CommandeProduitFormSet

def accueil(request):
    return render(request, 'driveapp/accueil.html')

def importer_produits(request):
    if request.method == 'POST':
        csv_file = request.FILES['fichier_csv']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être au format CSV.')
            return redirect('importer_produits')

        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                categorie, _ = CategorieProduit.objects.get_or_create(nom=row['categorie'])
                Produit.objects.create(
                    nom=row['nom'],
                    date_de_peremption=row['date_de_peremption'],
                    photo='',  # attention ici : à remplacer par défaut ou ignorer
                    marque=row['marque'],
                    prix=float(row['prix']),
                    id_categorie_produit=CategorieProduit.objects.get(nom=row['categorie'])
                )
            messages.success(request, 'Produits importés avec succès.')
            return redirect('liste_produits')
        except Exception as e:
            messages.error(request, f'Erreur lors de l\'import : {e}')
            return redirect('importer_produits')

    return render(request, 'driveapp/importer_produits.html')

# ==============================================
# CRUD pour CategorieProduit
# ==============================================

def liste_categories(request):
    categories = CategorieProduit.objects.all()
    return render(request, 'driveapp/categorie/liste.html', {'categories': categories})


def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieProduitForm()
    return render(request, 'driveapp/categorie/formulaire.html', {'form': form})


def detail_categorie(request, pk):
    categorie = get_object_or_404(CategorieProduit, pk=pk)
    produits = Produit.objects.filter(id_categorie_produit=categorie)
    return render(request, 'driveapp/categorie/detail.html', {
        'categorie': categorie,
        'produits': produits
    })


def modifier_categorie(request, pk):
    categorie = get_object_or_404(CategorieProduit, pk=pk)
    if request.method == 'POST':
        form = CategorieProduitForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('detail_categorie', pk=pk)
    else:
        form = CategorieProduitForm(instance=categorie)
    return render(request, 'driveapp/categorie/formulaire.html', {'form': form})


def supprimer_categorie(request, pk):
    categorie = get_object_or_404(CategorieProduit, pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('liste_categories')
    return render(request, 'driveapp/categorie/supprimer.html', {'categorie': categorie})


# ==============================================
# CRUD pour Produit
# ==============================================

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'driveapp/produit/liste.html', {'produits': produits})


def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'driveapp/produit/formulaire.html', {'form': form})


def detail_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    categorie = produit.id_categorie_produit
    return render(request, 'driveapp/produit/detail.html', {'produit': produit})


def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('detail_produit', pk=pk)
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'driveapp/produit/formulaire.html', {'form': form})


def supprimer_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'driveapp/produit/supprimer.html', {'produit': produit})


# ==============================================
# CRUD pour Client
# ==============================================

def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'driveapp/client/liste.html', {'clients': clients})


def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    else:
        form = ClientForm()
    return render(request, 'driveapp/client/formulaire.html', {'form': form})


def detail_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    commandes = Commande.objects.filter(id_client=client)
    return render(request, 'driveapp/client/detail.html', {
        'client': client,
        'commandes': commandes
    })


def modifier_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('detail_client', pk=pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'driveapp/client/formulaire.html', {'form': form})


def supprimer_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('liste_clients')
    return render(request, 'driveapp/client/supprimer.html', {'client': client})


# ==============================================
# CRUD pour Commande
# ==============================================

def liste_commandes(request):
    commandes = Commande.objects.all()
    return render(request, 'driveapp/commande/liste.html', {'commandes': commandes})


def ajouter_commande(request):
    if request.method == 'POST':
        commande_form = CommandeForm(request.POST)
        formset = CommandeProduitFormSet(request.POST)

        if commande_form.is_valid() and formset.is_valid():
            commande = commande_form.save()
            lignes = formset.save(commit=False)
            for ligne in lignes:
                ligne.id_commande = commande
                ligne.save()
            return redirect('detail_commande', pk=commande.pk)
    else:
        commande_form = CommandeForm()
        formset = CommandeProduitFormSet()

    return render(request, 'driveapp/commande/formulaire.html', {
        'form': commande_form,
        'formset': formset,
        'mode': 'creation'
    })


def detail_commande(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    lignes = CommandeProduit.objects.filter(id_commande=commande)
    total = sum(ligne.id_produit.prix * ligne.quantite for ligne in lignes)
    for ligne in lignes:
        ligne.sous_total = ligne.quantite * ligne.id_produit.prix
    return render(request, 'driveapp/commande/detail.html', {
        'commande': commande,
        'lignes': lignes,
        'total': total
    })


def modifier_commande(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        formset = CommandeProduitFormSet(request.POST, instance=commande)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('detail_commande', pk=pk)
    else:
        form = CommandeForm(instance=commande)
        formset = CommandeProduitFormSet(instance=commande)

    return render(request, 'driveapp/commande/formulaire.html', {
        'form': form,
        'formset': formset,
        'mode': 'modification'
    })


def supprimer_commande(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('liste_commandes')
    return render(request, 'driveapp/commande/supprimer.html', {'commande': commande})


# ==============================================
# CRUD pour CommandeProduit
# ==============================================

def ajouter_ligne_commande(request):
    if request.method == 'POST':
        form = CommandeProduitForm(request.POST)
        if form.is_valid():
            ligne = form.save()
            return redirect('detail_commande', pk=ligne.id_commande.pk)
    else:
        form = CommandeProduitForm()
    return render(request, 'driveapp/commandeproduit/formulaire.html', {'form': form})


def supprimer_ligne_commande(request, pk):
    ligne = get_object_or_404(CommandeProduit, pk=pk)
    commande_pk = ligne.id_commande.pk
    if request.method == 'POST':
        ligne.delete()
        return redirect('detail_commande', pk=commande_pk)
    return render(request, 'driveapp/commandeproduit/supprimer.html', {'ligne': ligne})


def exporter_commande_txt(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    lignes = CommandeProduit.objects.filter(id_commande=commande)

    # Création du contenu du fichier texte
    contenu = f"Commande n°{commande.numero_commande}\n"
    contenu += f"Client : {commande.id_client.nom} {commande.id_client.prenom}\n"
    contenu += f"Date : {commande.date.strftime('%d/%m/%Y')}\n\n"
    contenu += "Produits commandés :\n"

    total = 0
    for ligne in lignes:
        nom = ligne.id_produit.nom
        quantite = ligne.quantite
        prix = ligne.id_produit.prix
        sous_total = quantite * prix
        contenu += f" - {nom} | {quantite} x {prix:.2f} € = {sous_total:.2f} €\n"
        total += sous_total

    contenu += f"\nTotal : {total:.2f} €"

    # Réponse HTTP avec téléchargement
    response = HttpResponse(contenu, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename=commande_{commande.pk}.txt'
    return response