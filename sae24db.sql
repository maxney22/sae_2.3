
-- Base de données
CREATE DATABASE IF NOT EXISTS sae24db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE sae24db;

-- Table : Catégorie de produit
CREATE TABLE CategorieProduit (
    id_categorie_produit INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    descriptif TEXT
);

-- Table : Produit
CREATE TABLE Produit (
    id_produits INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    date_de_peremption DATE,
    photo VARCHAR(255),
    marque VARCHAR(100),
    prix DECIMAL(10, 2),
    id_categorie_produit INT,
    FOREIGN KEY (id_categorie_produit) REFERENCES CategorieProduit(id_categorie_produit)
        ON DELETE SET NULL ON UPDATE CASCADE
);

-- Table : Client
CREATE TABLE Client (
    id_clients INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_inscription DATE,
    adresse TEXT
);

-- Table : Commande
CREATE TABLE Commande (
    id_commandes INT PRIMARY KEY AUTO_INCREMENT,
    numero_commande VARCHAR(50) NOT NULL,
    id_client INT,
    date DATE,
    FOREIGN KEY (id_client) REFERENCES Client(id_clients)
        ON DELETE SET NULL ON UPDATE CASCADE
);

-- Table : Ligne de commande (CommandeProduit)
CREATE TABLE CommandeProduit (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_commande INT,
    id_produit INT,
    quantite INT,
    FOREIGN KEY (id_commande) REFERENCES Commande(id_commandes)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_produit) REFERENCES Produit(id_produits)
        ON DELETE CASCADE ON UPDATE CASCADE
);
