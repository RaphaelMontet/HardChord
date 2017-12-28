#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes import *

#Fichier d'exécution principal, utilisé pour les menus et la gestion de partie

#Liste des notes
Ab = Note("Ab", "Lab")
A = Note("A", "La")
Ad = Note("A#", "La#")

Bb = Note("Bb", "Sib")
B = Note("B", "Si")
Bd = Note("B#", "Si#")

Cb = Note("Cb", "Dob")
C = Note("C", "Do")
Cd = Note("C#", "Do#")

Db = Note("Db", "Réb")
D = Note("D", "Ré")
Dd = Note("D#", "Ré#")

Eb = Note("Eb", "Mib")
E = Note("E", "Mi")
Ed = Note("E#", "Mi#")

Fb = Note("Fb", "Fab")
F = Note("F", "Fa")
Fd = Note("F#", "Fa#")

Gb = Note("Gb", "Solb")
G = Note("G", "Sol")
Gd = Note("G#", "Sol#")

#Liste des accords (doigt, frette)
    #Base A
A = Accord("A major", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(2, 2), NoteJouee(1, 2), NoteJouee(3, 2), NoteJouee(0, 0))
A5 = Accord("A5", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(1, 2), NoteJouee(2, 2), NoteJouee(-1, -1), NoteJouee(-1, -1))
A6 = Accord("A6", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(1, 2), NoteJouee(1, 2), NoteJouee(1, 2), NoteJouee(1, 2))
A7 = Accord("A7", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(2, 2), NoteJouee(0, 0), NoteJouee(3, 2), NoteJouee(0, 0))
Amaj7 = Accord("Amaj7", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(2, 2), NoteJouee(1, 1), NoteJouee(3, 2), NoteJouee(0, 0))
A9 = Accord("A9", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(1, 2), NoteJouee(3, 4), NoteJouee(1, 2), NoteJouee(2, 3))
Amaj9 = Accord("Amaj9", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(1, 2), NoteJouee(3, 4), NoteJouee(1, 2), NoteJouee(4, 5))
A11 = Accord("A11", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(0, 0), NoteJouee(0, 0), NoteJouee(1, 2), NoteJouee(0, 0))
A13 = Accord("A13", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(2, 2), NoteJouee(0, 0), NoteJouee(3, 2), NoteJouee(4, 2))
Amaj13 = Accord("Amaj13", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(2, 2), NoteJouee(1, 1), NoteJouee(3, 2), NoteJouee(4, 2))
Am = Accord("A minor", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(2, 2), NoteJouee(3, 2), NoteJouee(1, 1), NoteJouee(0, 0))
Am6 = Accord("Am6", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(2, 2), NoteJouee(3, 2), NoteJouee(1, 1), NoteJouee(4, 2))
Am7 = Accord("Am7", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(2, 2), NoteJouee(0, 0), NoteJouee(1, 1), NoteJouee(0, 0))
Am9 = Accord("Am9", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(2, 5), NoteJouee(3, 5), NoteJouee(0, 0), NoteJouee(0, 0))
Am11 = Accord("Am11", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(0, 0), NoteJouee(0, 0), NoteJouee(1, 1), NoteJouee(0, 0))
Am13 = Accord("Am13", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(2, 2), NoteJouee(0, 0), NoteJouee(1, 1), NoteJouee(3, 2))
Ammaj7 = Accord("Am(maj7)", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(2, 2), NoteJouee(3, 2), NoteJouee(1, 1), NoteJouee(4, 4))
Asus2 = Accord("Asus2", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(1, 2), NoteJouee(2, 2), NoteJouee(0, 0), NoteJouee(0, 0))
Asus4 = Accord("Asus4", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(1, 2), NoteJouee(2, 2), NoteJouee(3, 3), NoteJouee(0, 0))
Adim = Accord("Adim", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(1, 1), NoteJouee(3, 2), NoteJouee(2, 1), NoteJouee(4, 2))
Aaug = Accord("Aaug", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(4, 3), NoteJouee(2, 2), NoteJouee(3, 2), NoteJouee(1, 1))
A69 = Accord("A6/9", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(3, 4), NoteJouee(4, 4), NoteJouee(1, 2), NoteJouee(0, 0))
A7sus4 = Accord("A7sus4", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(1, 2), NoteJouee(0, 0), NoteJouee(2, 3), NoteJouee(0, 0))
A7b5 = Accord("A7b5", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(1, 1), NoteJouee(2, 2), NoteJouee(2, 2), NoteJouee(4, 3))
A7b9 = Accord("A7b9", NoteJouee(3, 3), NoteJouee(2, 2), NoteJouee(-1, -1), NoteJouee(1, 1), NoteJouee(4, 3), NoteJouee(1, 1))
A9sus4 = Accord("A9sus4", NoteJouee(3, 5), NoteJouee(-1, -1), NoteJouee(4, 5), NoteJouee(2, 4), NoteJouee(1, 3), NoteJouee(-1, -1))
Add9 = Accord("Add9", NoteJouee(-1, -1), NoteJouee(0, 0), NoteJouee(1, 2), NoteJouee(4, 4), NoteJouee(2, 2), NoteJouee(0, 0))
Aaug9 = Accord("Aaug9", NoteJouee(1, 1), NoteJouee(-1, -1), NoteJouee(2, 1), NoteJouee(3, 2), NoteJouee(3, 2), NoteJouee(4, 3))

    #Base B


print Am.nom