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


URLs pertinentes
================

Si le serveur django est exécuté sur la machine locale, les URLs suivantes sont
disponibles :

* administration : http://127.0.0.1:8000/admin/
* racine de l'API REST : http://127.0.0.1:8000/sensors/api/
* liste des capteurs définis : http://127.0.0.1:8000/sensors/api/sensors/
* liste des valeurs enregistrées : http://127.0.0.1:8000/sensors/api/readings/


Liens
=====

Utilisation de Postgresql avec Django sous Ubuntu :

https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
