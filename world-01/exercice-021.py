# Exercício 021
# Faça um programa e Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.mixer.init()
pygame.mixer.music.load('exercice-021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
