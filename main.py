from harness import Harness
import subprocess
import json

with open('settings.json') as json_file:
    settings = json.load(json_file)

game = Harness(zoom=3, title="allstars-python")
game.resource_path = "."
font = game.load_bitmap_font("font.png", width=6, height=10)

if game.has_controllers:
    controller = game.controllers[0]
    controller.set_mapping()

a = 1

@game.draw
def draw(renderer):
    global a
    renderer.draw_text(font, 20, 60, "Super Mario 64")
    renderer.draw_text(font, 20, 80, "Super Mario Sunshine")
    renderer.draw_text(font, 20, 100, "Super Mario Galaxy")
    if a == 1:
        renderer.draw_text(font, 10, 60, "/")
    elif a == 2:
        renderer.draw_text(font, 10, 80, "/")
    elif a == 3:
        renderer.draw_text(font, 10, 100, "/")


@game.update
def update(dt):
    global a
    if game.keys[game.KEY_UP]:
        print("up")
        if a == 2:
            a = 1
        elif a == 3:
            a = 2
        game.keys[game.KEY_UP] = False
    elif game.keys[game.KEY_DOWN]:
        print("down")
        if a == 1:
            a = 2
        elif a == 2:
            a = 3
        game.keys[game.KEY_DOWN] = False
    elif game.keys[game.KEY_C]:
        print("selected", a)
        if a == 1:
            subprocess.run(settings["Super Mario 64"])
        elif a == 2:
            subprocess.run([settings["Dolphin"], settings["Super Mario Sunshine"]])
        elif a == 3:
            subprocess.run([settings["Dolphin"], settings["Super Mario Galaxy"]])
        game.keys[game.KEY_C] = False

game.loop()