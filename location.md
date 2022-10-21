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
