# -*- coding: utf-8 -*-

import sys
import requests

if __name__ == "__main__":
    """
    Script de test de l'enregistrement de nouvelles valeurs
    par l'api rest

    Par defaut on envoie la valeur 18.4 sur le capteur 1, ces
    valeurs pouvant être modifiées par les paramètres en ligne
    de commande
    """

    payload = {
        'sensor': 1,
        'value': 18.4,
    }

    if len(sys.argv) > 1:
        payload['sensor'] = int(sys.argv[1])
    if len(sys.argv) > 2:
        payload['value'] = float(sys.argv[2])

    print requests.post("http://127.0.0.1:8000/sensors/api/readings/", data=payload)
