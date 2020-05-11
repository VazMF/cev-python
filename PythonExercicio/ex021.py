#faça um programa que abra e reproduza um arquivo mp3
#aula 08, utilizando módulos
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
input()
pygame.mixer.play()
pygame.event.wait()

