Introduction:

2. - PK de Agences = id
   - PK de Locations = id
   - PK de Vehicules = immatriculation

3. Les seuls clé étrangères seront juste dans la relation Locations : 
   - vehicule (FK) --> immatriculation (Vehicules)
   - départ (FK) --> id (Agences)
   - retour (FK) --> id (Agences)

La relation Agences:

1. SELECT * FROM Agences;
2. SELECT nom,ville FROM Agences;
3. SELECT nom FROM Agences WHERE ville = 'Lorient';
4. SELECT nom,code FROM Agences WHERE code LIKE '56%';
5. SELECT nom,code FROM Agences WHERE SUBSTR(code,1,2) = '56';
6. SELECT DISTINCT ville FROM Agences WHERE SUBSTR(code,1,2) = '56';
7. SELECT nom, code FROM Agences WHERE SUBSTR(code,1,2) IN ('56','29','35','22');
8. SELECT COUNT(*) FROM Agences WHERE pays = 'France';
9. SELECT COUNT(*) FROM Agences WHERE SUBSTR(code,1,2) IN ('56','29','35','22');

La relation Vehicules

1. SELECT COUNT(*) FROM Vehicules;
2. SELECT MIN(age) AS minimum,(SELECT MAX(age) FROM Vehicules) AS maximum FROM Vehicules;
3. SELECT nom FROM Vehicules WHERE age = 3;
4. SELECT MIN(age) FROM Vehicules WHERE nom LIKE 'Peugeot%';
5. SELECT MAX(kilometrage) FROM Vehicules;
6. SELECT AVG(kilometrage) FROM Vehicules;
7. SELECT * FROM Vehicules ORDER BY kilometrage DESC;
8. SELECT nom,immatriculation,kilometrage/age AS km_par_mois FROM Vehicules;
9. SELECT immatriculation,kilometrage/age AS km_par_mois FROM Vehicules WHERE km_par_mois = (SELECT MAX(kilometrage/age) FROM Vehicules);
10. SELECT nom,immatriculation,ROUND((kilometrage/age)*0.35) AS recette FROM Vehicules;
11. SELECT nom,immatriculation,ROUND((kilometrage/age)*0.35) AS recette FROM Vehicules ORDER BY recette DESC;

La relation Locations

1. SELECT * FROM Locations;
2. SELECT COUNT(*) FROM Locations;
3. SELECT COUNT(*) FROM Locations WHERE depart <> retour;
4. SELECT SUM(kilometrage) FROM Locations;
5. SELECT ROUND(AVG(kilometrage)) FROM Locations WHERE depart = retour;
6. SELECT * FROM Locations AS L JOIN Vehicules AS V ON V.immatriculation = L.vehicule;
7. SELECT V.nom,L.vehicule,L.date,L.kilometrage FROM Locations AS L JOIN Vehicules AS V ON V.immatriculation = L.vehicule;
8. SELECT L.* FROM Locations AS L WHERE L.vehicule = 'AB-224-BA' ORDER BY date ASC;
9. SELECT L.*,A.nom,A.ville FROM Locations AS L JOIN Agences AS A ON A.id = L.depart WHERE L.vehicule = 'AB-224-BA' ORDER BY date ASC;
10. SELECT DISTINCT A.nom,A.ville FROM Locations AS L JOIN Agences AS A ON A.id = L.depart WHERE L.vehicule = 'AB-224-BA';
11. SELECT L.date,depart.nom,depart.ville,retour.nom,retour.ville FROM Locations AS L JOIN Agences AS depart ON L.depart = depart.id JOIN Agences AS retour ON L.retour = retour.id WHERE L.vehicule = 'AB-224-BA' ORDER BY L.date;

Gestion du réseau

1. SELECT * FROM Locations WHERE vehicule = 'DF-269-EF' ORDER BY date DESC;
2. UPDATE Locations SET kilometrage = 247 WHERE id = 34;
3. SELECT kilometrage FROM Locations WHERE id = 34;
4. UPDATE Vehicules SET kilometrage = kilometrage + 247 WHERE immatriculation = 'DF-269-EF';
5. SELECT kilometrage FROM Vehicules WHERE immatriculation = 'DF-269-EF';
6. SELECT id FROM Agences WHERE nom = 'Sépamieuayeur';
7. SELECT MAX(id) FROM Locations;
8. INSERT INTO Locations(id,vehicule,depart,retour,kilometrage,date,duree) VALUES(41,'CC-259-FF',1,1,NULL,'2020-12-24',0);
9. SELECT V.nom,V.immatriculation FROM Vehicules AS V JOIN Locations AS L ON V.immatriculation = L.vehicule WHERE L.date = '2020-12-24';
10. SELECT V.nom,V.immatriculation FROM Vehicules AS V JOIN Locations AS L ON V.immatriculation = L.vehicule WHERE L.kilometrage IS NULL;
11. 
