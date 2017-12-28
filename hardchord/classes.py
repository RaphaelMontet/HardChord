#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Classe note, définie par son nom US et son nom français
class Note:

    def __init__(self, anName_n, laName_n):
        self.anName = anName_n
        self.laName = laName_n


#Classe note jouée, définie par un doigt et une frette
class NoteJouee(Note):

    def __init__(self, doigt_n, frette_n):
        self.doigt = doigt_n
        self.frette = frette_n


#Classe accord, défini par les notes le composant et la manière dont celles-ci sont jouées
class Accord:

    tabNotesJouees = []

    def __init__(self, nom_n, *notesJouees):
            self.nom = nom_n
            self.tabNotesJouees = notesJouees


#Classe table accords, permettant de stocker l'ensemble des accords
class TableAccords:

    tabAccords = []

    def __init__(self, *accords):
        self.tabAccords = accords


#Classe display, permettant d'afficher divers éléments
class Display:

    def __init__(self):
        pass
    #SFML ici


#Classe display accord, permettant d'afficher les informations relatives à un accord
class DisplayAccord(Display):

    def __init__(self):
        pass
    #SFML ici
