"""Das erste, was wir tun müssen, ist ein Paket namens pygame zu installieren,
 das ist die Module, die wir brauchen, um alle Grafiken zu erstellen"""
import pygame

"""Da wir einige Elemente brauchen, die in der Module 
'constant' gelagert sind, importieren wir sie wie folgt"""
from Bauernschach.Bilder.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from Bauernschach.board import Spiestand
from Bauernschach.game import Game

"""Ausführzeit"""
FPS = 60

"""Wir werden ein Pygame-Display einrichten, in das wir alles einzeichnen werden,
 dann werden wir eine grundlegende Ereignisschleife einrichten, die prüfen wird, 
 ob wir eine Maus drücken oder eine bestimmte Taste oder was auch immer wir tun """
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dame') #Name des Spiels

def get_row_col_form_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

"""Wir definieren eine Hauptfunktion, die wir ausführen werden müssen um ads Spiel anzuzeigen und auszuführen"""
def main():
    """wir werden eine so genannte Ereignisschleife erstellen, die alle x-mal pro Sekunde abläuft, sie prüft,
    ob wir auf etwas gedrückt haben, sie aktualisiert die Anzeige und so weiter"""
    run = True

    """in pygame, wenn wir wollen, dass unser Spiel mit einer konstanten Framerate läuft, können wir eine Uhr 
    definieren und die Uhr wird sicherstellen, dass unser Hauptereignisschleife nicht zu schnell oder zu langsam läuft"""
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_form_mouse(pos)
                if game.turn == RED:
                    game.select(row, col)

        game.update()

    pygame.quit()

main()