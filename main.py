def on_button_pressed_a():
    basic.show_number(krok)
    basic.pause(200)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global krok
    krok = 0
    basic.show_number(krok)
    basic.pause(200)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    global krok
    krok += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

krok = 0
krok = 0

def on_forever():
    pass
basic.forever(on_forever)
