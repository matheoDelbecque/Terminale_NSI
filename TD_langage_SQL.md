#exercice 1

SELECT titre FROM livre;

SELECT nom FROM usager;

SELECT DISTINCT nom FROM usager;

SELECT titre FROM livre WHERE annee < 1980;

SELECT isbn FROM emprunt WHERE retour = '2020-01-01';

SELECT nom FROM auteur ORDER BY nom ASC;

SELECT nom FROM usager WHERE cp = '75012' OR cp = '75013';

SELECT nom, adresse FROM usager WHERE NOT adresse LIKE '%Rue%';

SELECT annee, titre FROM livre WHERE annee % 4 = 0 AND annee % 100 != 0;

#exercice 2

SELECT livre.titre FROM livre JOIN emprunt ON livre.isbn = emprunt.isbn;

SELECT livre.titre FROM livre JOIN emprunt ON livre.isbn = emprunt.isbn WHERE emprunt.retour < '2020-03-31';

SELECT auteur.nom, auteur.prenom FROM livre JOIN auteur_de ON livre.isbn = auteur_de.isbn JOIN auteur ON auteur_de.a_id = auteur.a_id WHERE livre.titre = '1984';

SELECT DISTINCT usager.nom, usager.prenom FROM usager JOIN emprunt ON usager.code_barre = emprunt.code_barre;

SELECT DISTINCT usager.nom, usager.prenom FROM usager JOIN emprunt ON usager.code_barre = emprunt.code_barre ORDER BY nom ASC;
