#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import mcutils
import config as conf


def command_info(command_dict):
    if len(command_dict['args']) > 1:
        for element in command_dict['args'][1:]:
            if mcutils.get_map_info(element):
                mcutils.say_minecraft('Map %s : %s' % (element, mcutils.get_map_info(element)))
            else:
                mcutils.say_minecraft("la Map %s n'existe pas" % element)
    else:
        mcutils.say_minecraft('[Map %s chargée] Voici la liste des maps :' % mcutils.get_srv_param('level-name'))
        for name, desc in mcutils.get_map_info().items():
            mcutils.say_minecraft("Map %s: %s" % (name, desc))
        mcutils.say_minecraft('Utilisez !setinfo pour modifier les informations de la map actuellement chargée.')
    return


def command_update(command_dict):
    mcutils.say_minecraft("test")
    if len(command_dict['args']) == 2:
        if command_dict['args'][1] == mcutils.get_srv_param('level-name'):
            mcutils.say_minecraft('Mise à jour de la map ' + command_dict['args'][1] + '.')
            mcutils.stop_server()
            time.sleep(10)
            mcutils.update_map(command_dict['args'][1])
            mcutils.start_server()
        else:
            if command_dict['args'][1] in mcutils.get_map_info().items():
                mcutils.update_map(command_dict['args'][1])
                mcutils.say_minecraft('Mise à jour de la map %s lancée en tâche de fond.' % command_dict['args'][1])
            else:
                mcutils.say_minecraft("La map n'existe pas.")
        return
    else:
        mcutils.say_minecraft('Usage: ' + conf.SYMBOL_COMMAND + 'update <Map_ID>')


def command_swap(command_dict):
    if len(command_dict['args']) > 1:
        if command_dict['args'][1] == mcutils.get_srv_param('level-name'):
            mcutils.say_minecraft('La map %s est déja chargée.' % command_dict['args'][1])
        else:
            mcutils.say_minecraft('Changement de map programmé : Passage de la map %s vers la map %s' % (
                mcutils.get_srv_param('level-name'), command_dict['args'][1]))
            mcutils.stop_server()
            mcutils.set_srv_param('level-name', command_dict['args'][1])
            mcutils.start_server()
    else:
        mcutils.say_minecraft('Usage: ' + conf.SYMBOL_COMMAND + 'swap <Map_ID>')
    return


def command_set_info(command_dict):
    if len(command_dict) > 1:
        str = ' '.join(command_dict['args'][1:])
        print(str)
        mcutils.set_map_info(str)
    else:
        mcutils.say_minecraft('Usage: ' + conf.SYMBOL_COMMAND + 'Setinfo <Description>')
    return
