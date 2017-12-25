#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Classe note, définie par son nom US et son nom français
class Note:

    def __init__(self, usName_n, frName_n):
        self.usName = usName_n
        self.frName = frName_n

A = Note("A", "La")
B = Note("B", "Si")
C = Note("C", "Do")
D = Note("D", "Ré")
E = Note("E", "Mi")
F = Note("F", "Fa")
G = Note("G", "Sol")


#Classe note jouée, définie par une note, un doigt et une frette
class NoteJouee(Note):

    note = Note("0", "0")

    def __init__(self, note_n, doigt_n, frette_n, corde_n):
        self.note = Note.__init__(note_n, note_n.usName, note_n.frName)
        self.doigt = doigt_n
        self.frette = frette_n
        self.corde = corde_n


#Classe accord, défini par les notes le composant et la manière dont celles-ci sont jouées
class Accord:

    tabNotesJouees = []

    def __init__(self, image, *note):
        self.tabNotesJouees.append(note)

Am = Accord(NoteJouee(E, 0, 0, 1), NoteJouee(C, 1, 1, 2), NoteJouee(A, 2, 2, 3), NoteJouee(E, 3, 2, 4), NoteJouee(A, 0, 5, 0))