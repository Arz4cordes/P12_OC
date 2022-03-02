API construite avec Django REST Framework, permettant de gérer un fichier client, des contrats associés aux clients, et des événements organisés après la signature des contrats.

Lien github du projet:
    https://github.com/Arz4cordes/P12_OC


##### SOMMAIRE ####
1) Objectifs
2) Installation
3) Utilisation de l'application
4) Détail des endpoints
5) Tests des endpoints avec Postman


##### 1. Objectifs de l'application #####
* Les utilisateurs de l'application sont répartis en 3 groupes:

    Management:
        Les managers sont les seuls utilisateurs qui ont accès à l'interface personnalisée d'administration de Django.
        Ils peuvent réaliser les actions Create, Read, Update, Delete sur chacun des modèles User, Client, Contract, Event (voir ci-dessous)
        de l'application.

    Commercial:
        Les commerciaux ont accès en lecture aux modèles Client, Contract, Event (voir ci-dessous).
        Ils peuvent créer des clients et mettre à jour les clients dont ils sont responsables.
        Ils peuvent créer et mettre à jour des contrats et des évenements pour les clients dont ils sont responsables.

    Support:
    Les membres de l'équipe support peuvent voir et mettre à jour les événements qui leur sont attribués.
    Il peuvent afficher les clients liés aux événements dont ils ont été nommés responsables.

* Modèles:
    Avec le modèle utilisateur, les modèles suivants ont été crée:

        Client
            Les clients ont un responsable du groupe commercial

        Contrat
            Les contrats sont liés à un client

        Event
            Les événements sont liés à un contrat signé
            Les événements se voient attribuer un responsable du groupe support

* Les différents endpoints sont détaillés au point 4 plus loin, avec les permissions correspondantes.


##### 2. Installation de l'application #####
I) Installer d'abord un environnement virtuel Python, par exemple avec la commande python -m venv envp10 sous windows.

II) Le fichier requirements.txt contient les bibliothèques à installer: utiliser par exemple la commande python -m pip install -r requirements.txt pour installer les bibliothèques utilisées dans l'application.

III) L'application utilise une base de données PostgreSQL: vous pouvez télécharger PostgreSQL via cette adresse:

        https://www.postgresql.org/download/

La documentation complète de PostgreSQL est par ailleurs disponible, pour information, à cette adresse (version 14.2):
    https://docs.postgresql.fr/14/pg14.pdf

IV) Après l'installation de PostgreSQL, vous devrez choisir un nom d'utilisateur et un mot de passe pour accèder aux bases de données localement.

ATTENTION: l'application a été configurée avec les paramètres suivants (voir DATABASES dans le fichier settings.py):
'NAME': 'Epic_Events', 
'USER': 'epic_events_admin', 
'PASSWORD': 'OC_P12'
        
Vous pouvez bien sûr utiliser un autre utilisateur avec un autre mot de passe, et changer le nom de la base de données,
mais veillez dans ce cas à changer les paramètres listés ci-dessus dans le fichier settings.py


##### 3. Utilisation de l'application #####
I) Utilisez tout d'abord la commande suivante pour créer un premier superutilisateur de l'application:
        python manage.py createsuperuser
    Vous aurez à définir un nom d'utilisateur, entrer un email et définir un mot de passe (avec confirmation du mot de passe)

II) Pour utilser ensuite l'application, vous devez ensuite lancer le serveur avec la commande suivante:
        python manage.py runserver

III) Avec les paramètres du superutilisateur crée, puis plus tard avec les paramètres de n'importe quel utilisateur de l'application du groupe Management,
    vous pouvez vous connecter à l'interface d'administration de Django avec l'URL suivante dans un navigateur web:
         http://127.0.0.1:8000/admin/

    Dans cette interface d'administration, vous avez accès aux modèles suivants:

    * User: pour gérer les utilisateurs de l'application (créer, mettre à jour, voir ou supprimer un utilisateur)
        Vous pouvez filtrer les utilisateurs par groupe (commercial, support ou management),
        et trier les utilisateurs par rôle, par nom ou par email

    * Client: pour gérer le fichier client (créer, mettre à jour, voir ou supprimer).
        Vous pouvez trier les clients par email, numéro de téléphone ou nom d'entreprise.

    * Contract: pour gérer les contrats (créer, mettre à jour, voir ou supprimer).
        Vous pouvez trier les contrats par date de création, par statut (signé ou non),
        par date de signature, par montant ou par client.

    * Event: pour gérer les événements (créer, mettre à jour, voir ou supprimer).
        Vous pouvez trier les événements par date, par statut (à venir ou terminé), par responsable et par contrat.

IV) Pour les utilisateurs qui ne sont pas managers, rendez vous tout d'abord sur l'endpoint http://127.0.0.1:8000/login/

Vous aurez à rentrer les informations nom d'utilisateur et mot de passe pour un utilisateur valide (enregistré dans la base de donnée préalablement).

Une fois authentifié avec des informations correctes, une page dont l'URL est http://127.0.0.1:8000/home/ est affichée:
cette page donne les informations concernant l'utilisateur authentifié et connecté (nom, email, son rôle parmi Commercial, Support ou Management ...). 
Cet endpoint est accesible à tout moment tant que l'utilisateur reste connecté et authentifié.

V) Les différents endpoints accessibles une fois qu'un utilisateur est connecté et authentifié sont détaillés dans la section 4. suivante.

VI) Pour se déconnecter de l'application, sélectionner Log Out en cliquant sur le numéro d'utilisateur en haut à droite de la page.


##### 4. Liste des différents endpoints #####

I) http://127.0.0.1:8000/client/

Permissions: accessible pour tous les managers et commerciaux, mais pas avec le rôle support.

On peut utiliser les méthodes GET et POST pour cet endpoint:

        GET: Affichage de tous les clients, avec 5 clients par page
        Pour chaque client affiché, un lien est disponible pour voir le détail de ce client (endpoint II)

        POST: Le responsable du client sera automatiquement l'utilisateur connecté qui lance la requête POST.

II) http://127.0.0.1:8000/client/{numéro_du_client}

Permissions: accessible pour pour tous les managers et commerciaux, mais seulement avec la méthode GET avec le rôle support
si le client demandé est lié à un événement dont le membre support est responsable.

On peut utiliser les méthodes GET et PUT pour cet endpoint:

        GET: Affichage de toutes les informations relatives à un client donné.
        La liste des contrats associés à ce client est affichée, elle contient les liens vers ces contrats (endpoint  IV)

        PUT: Accessible seulement pour un manager ou pour un commercial qui est responsable de ce client.
        Le responsable du client sera automatiquement l'utilisateur connecté qui lance la requête PUT.

III) http://127.0.0.1:8000/contract/

Permissions: accessible pour tous les managers et commerciaux, mais pas avec le rôle support.

On peut utiliser les méthodes  GET et POST pour cet endpoint:

    GET: Affichage de tous les contrats, avec 5 contrats par page.
    Pour chaque contrat affiché, des liens sont disponibles pour voir le détail d'un contrat (endpoint IV)
    ou bien pour voir le détail du client associé au contrat (endpoint II).

    POST: Le client associé au contrat doit forcément être un client dont l'utilisateur connecté est responsable
    pour que la requête POST soit valide.

IV) http://127.0.0.1:8000/contract/{numéro_du_contrat}

Permissions: accessible pour pour tous les managers et commerciaux, mais pas avec le rôle support.

On peut utiliser les méthodes GET et PUT pour cet endpoint:

        GET: Affichage de toutes les informations concernant le contrat sélectionné.
        Un lien est disponible pour voir les informations du client associé au contrat (endpoint II)

        PUT: Accessible seulement pour un manager ou pour un commercial qui est responsable de ce client associé au contrat.
        Le client associé au contrat doit forcément être un client dont l'utilisateur connecté est responsable
        pour que la requête PUT soit valide.

V) http://127.0.0.1:8000/event/

Permissions: accessible pour tous les managers et commerciaux, mais pas avec le rôle support.

On peut utiliser les méthodes GET et POST pour cet endpoint:

        GET: Affichage de tous les événements, avec 5 événements par page.

        POST: Le contrat associé à l'événement doit forcément être lié à un client dont l'utilisateur connecté est responsable
        pour que la requête POST soit valide.

VI) http://127.0.0.1:8000/event/{numéro_de_l_evenement}

Permissions: accessible pour pour tous les managers, accessible uniquement en GET pour tous les commerciaux,
mais un membre de l'équipe support doit être responsable de l'événement pour accèder à cet endpoint.

On peut utiliser les méthodes GET et PUT pour cet endpoint:

        GET: Affichage de toutes les informations concernant l'événement.
        Un lien est disponible pour voir les informations du client lié à cet événement.
        
        PUT: accessible pour les managers ou pour les membres de l'équipe support qui sont responsables de l'événement.

VII) http://127.0.0.1:8000/admin/

Pour se connecter à l'interface d'administration (voir partie 3. ci-dessus)

VIII) http://127.0.0.1:8000/login/

Pour se connecter à l'application (voir partie 3. ci-dessus)

IX) http://127.0.0.1:8000/home/

Pour voir toutes les informations de l'utilisateur connecté, si il est connecté et authentifié
(voir partie 3. ci-dessus)

X) http://127.0.0.1:8000/logout/

Pour se déconnecter de l'application (voir partie 3. ci-dessus)


##### 5. Test des différents endpoints avec le logiciel Postman #####

La documentation Postman de ce projet a été publié à l'adresse suivante:

        https://documenter.getpostman.com/view/14708629/UVkpMahM

ATTENTION: Pour toutes les requêtes avec la méthode POST ou PUT dans Postman,
il faudra d'abord aller sur l'endpoint voulu en méthode GET pour récupérer le cookie csrftoken,
afin de le coller dans le header de la requête en POST sur le même endpoint ensuite.
(cette démarche est détaillée pour chaque endpoint dans la documentation publiée)
