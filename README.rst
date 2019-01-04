=============================
Installation et configuration
=============================

Paquets prérequis
=================

::

   sudo apt-get update
   sudo apt-get install python-pip python-dev python-virtualenv
   sudo apt-get install libpq-dev postgresql postgresql-contrib


Installation
============

Le logiciel peut être installé sur toute machine sur laquelle Python 2.7 est
accessible. Les dépendances sont listées dans le fichier `requirements.txt`.

Plusieurs méthodes pour télécharger les sources :

* repository git : `git clone https://github.com/poroussel/displaysensors.git`
* archive zip : `https://github.com/poroussel/displaysensors/archive/master.zip`

Afin de simplifier l'installation des paquets dans les versions souhaitées il
est préférable d'utiliser un environnement Python spécifique à l'aide de l'outil
`virtualenv`.

Si les sources de l'application sont installées dans le répertoire `/home/toto/displaysensors`, on
peut créer l'environnement Python comme ceci ::

  cd /home/toto
  virtualenv --system-site-packages displaysensors

On doit ensuite activer l'environnement ::

  cd /home/toto/displaysensors
  source bin/activate

Les dépendances Python du projet sont alors installées dans l'environnement avec
la commande ::

  pip install -r requirements.txt

Configuration
=============

La configuration de l'application se trouve dans le fichier ::

  /home/toto/displaysensors/displaysensors/settings.py

Par défaut l'application utilise une base de données SQLite locale. Une fois les premiers tests
réalisés il est possible d'utiliser un serveur de base de données en modifiant le fichier
`settings.py`

L'initialisation d'une nouvelle base de données est réalisée à l'aide de commandes `Django` ::

  cd /home/toto/displaysensors
  source bin/activate
  python manage.py migrate
  python manage.py createsuperuser

Le serveur peut alors être lancé pour toutes les interfaces réseaux sur le port 8000 à l'aide de la commande ::

  python manage.py runserver 0.0.0.0:8000
  
Une fois le serveur actif la page d'administration sera disponible à l'adresse ::

  http://127.0.0.1:8000/admin


URLs pertinentes
================

Si le serveur django est exécuté sur la machine locale, les URLs suivantes sont
disponibles :

* administration : http://127.0.0.1:8000/admin/
* racine de l'API REST : http://127.0.0.1:8000/sensors/api/
* liste des capteurs définis : http://127.0.0.1:8000/sensors/api/sensors/
* liste des valeurs enregistrées : http://127.0.0.1:8000/sensors/api/readings/


Exemple d'envoi d'une donnée
============================

À l'aide de `curl` nous pouvons aisément envoyer une valeur pour le capteur d'id 1 ::

  curl -d '{"sensor":1, "value":33.7}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/sensors/api/readings/

  
Liens
=====

Utilisation de Postgresql avec Django sous Ubuntu :

https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
