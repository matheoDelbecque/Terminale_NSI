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
9. SELECT immatriculation FROM Vehicules WHERE kilometrage/age = (SELECT MAX(kilometrage/age) FROM Vehicules);
10. SELECT nom,immatriculation,ROUND((kilometrage/age)*0.35) AS recette FROM Vehicules;
11. SELECT nom,immatriculation,ROUND((kilometrage/age)*0.35) AS recette FROM Vehicules ORDER BY recette DESC;
