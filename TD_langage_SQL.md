SELECT titre FROM livre;

SELECT nom FROM usager;

SELECT DISTINCT nom FROM usager;

SELECT titre FROM livre WHERE annee < 1980;

SELECT isbn FROM emprunt WHERE retour = '2020-01-01';

SELECT nom FROM auteur ORDER BY nom ASC;

SELECT nom FROM usager WHERE cp = '75012' OR cp = '75013';

SELECT nom, adresse FROM usager WHERE NOT adresse LIKE '%Rue%';

SELECT annee, titre FROM livre WHERE annee % 4 = 0 AND annee % 100 != 0;
