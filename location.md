Introduction:

2. PK de Agences = id
   PK de Locations = id
   PK de Vehicules = immatriculation

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
2. SELECT MIN(age) FROM Vehicules;

   SELECT MAX(age) FROM Vehicules;
3. SELECT nom FROM Vehicules WHERE age = 3;
4. 
