def on_button_pressed_a():
    global Personne
    Personne += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Personne
    Personne = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Personne
    Personne += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

Personne = 0
Personne = 0

def on_forever():
    basic.show_number(Personne)
basic.forever(on_forever)

def on_forever2():
    if Personne >= 10:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever2)
