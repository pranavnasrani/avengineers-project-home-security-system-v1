def on_button_pressed_a():
    if alert == 0:
        basic.show_string("Disarmed")
    else:
        basic.show_string("Armed")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global alert
    alert = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    control.reset()
input.on_button_pressed(Button.B, on_button_pressed_b)

pressure = 0
door = 0
alert = 0
alert = 1

def on_forever():
    global door
    if alert == 1:
        if input.magnetic_force(Dimension.STRENGTH) > 200:
            door = 1
        else:
            door = 0
        if door == 1:
            basic.show_icon(IconNames.HAPPY)
        else:
            basic.show_icon(IconNames.SAD)
            basic.pause(1000)
            music.start_melody(music.built_in_melody(Melodies.CHASE), MelodyOptions.ONCE)
basic.forever(on_forever)

def on_forever2():
    global pressure
    if alert == 1:
        if input.pin_is_pressed(TouchPin.P1):
            pressure = 1
        else:
            pressure = 0
        if pressure == 1:
            basic.show_icon(IconNames.ANGRY)
            basic.pause(1000)
            music.start_melody(music.built_in_melody(Melodies.CHASE), MelodyOptions.ONCE)
basic.forever(on_forever2)
