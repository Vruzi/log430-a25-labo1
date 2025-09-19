# Labo XX — Rapport

<img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Ets_quebec_logo.png" width="250"> \
[Prénom Nom de l’étudiant·e] \
Rapport de laboratoire \
LOG430 — Architecture logicielle \
[Lieu et date de dépôt] \
École de technologie supérieure

## Questions

> 💡 **Question 1** : Quelles commandes avez-vous utilisées pour effectuer les opérations UPDATE et DELETE dans MySQL ? Avez-vous uniquement utilisé Python ou également du SQL ? Veuillez inclure le code pour illustrer votre réponse.

J'ai regarder comment les fonction SELECT et INSERT était faite, et j'ai suivie la même structure, voici un example de code
```
def update(self, user):
   """ Update given user in MySQL """
   self.cursor.execute(
      "UPDATE users SET name=%s, email=%s WHERE id=%s",
      (user.name, user.email, user.id)
   )
   self.conn.commit()
   return self.cursor.rowcount
```
J'ai remarqué la strucuture la fonction execute avec le sting de la commande SQL à effectuer avec %s pour dire ou insérer les donnée par exemple user.name et ensuitre la liste des données les uns à la suite des autres. Finalement il fait initier la connection et finir avec le retour, par exemple ici le nombre de lignes affecté

> 💡 **Question 2** : Quelles commandes avez-vous utilisées pour effectuer les opérations dans MongoDB ? Avez-vous uniquement utilisé Python ou également du SQL ? Veuillez inclure le code pour illustrer votre réponse.

Pour faire les opérations dans MongoDB nous avons tous simplement fait du code python qui fait les actions demandés.
Extrait de mon code:
```
self.conn = pymongo.MongoClient(f"mongodb://{db_user}:{db_pass}@{db_host}:27017/") 
self.db = self.conn[db_name]

def select_all(self):
   """ Select all users from MongoDB """
   col = self.db["users"]
   return [User(*col) for col in col.find()]
```
MySQL fonctionne avec une base de donnée relationnelle, tandis que MongoDB (orientée documents) n’utilise pas SQL : on manipule des collections de documents JSON/BSON via le MQL. En Python, on passe par PyMongo et des méthodes comme find(), insert_one(), update_one() avec des dictionnaires. Pour MongoDB, nous avons utilisé uniquement Python/PyMongo, aucun SQL.


> 💡 **Question 3** : Comment avez-vous implémenté votre `product_view.py` ? Est-ce qu’il importe directement la `ProductDAO` ? Veuillez inclure le code pour illustrer votre réponse.

Pour faire le product_view.py j'ai suivie la même strucutre que dans user_vew.py. Mais j'ai modifier user_view afin d'avoir une navigation entre user et product.
Non il importe pas directement ProductDAO car nous somme dans un model MVC et donc il appelle le controller.
```
from models.product import Product
from controllers.product_controller import ProductController
```

> 💡 **Question 4** : Si nous devions créer une application permettant d’associer des achats d'articles aux utilisateurs (`Users` → `Products`), comment structurerions-nous les données dans MySQL par rapport à MongoDB ?

Si nous devions créer une application qui associe user et product. Nous utilisirions une base de donnée relationnel comme MySQL.
On peut lier Id_user avec Product_Id avec une table relationnel.

## Observations additionnelles

- Observations sur d’éventuels problèmes de setup ou de code rencontrés lors de l’exécution des activités (optionel).

- Particularités de votre configuration CI/CD (ex. : utilisation d’une VM, d’un service infonuagique comme Azure, etc.).

Pour le CI/CD j'ai configuer la VM de l'école afin d'avoir un self-hosted runner dessus afin de pouvoir faire le déploiement.