input.onButtonPressed(Button.A, function () {
    alert = 1
    basic.showString("Armed")
})
input.onButtonPressed(Button.AB, function () {
    alert = 0
})
input.onButtonPressed(Button.B, function () {
    alert = 0
    basic.showString("Disarmed")
})
let pressure = 0
let alert = 0
alert = 1
basic.forever(function () {
    if (alert == 1) {
        if (input.magneticForce(Dimension.Strength) > 200) {
            basic.showIcon(IconNames.Happy)
        } else {
            basic.showIcon(IconNames.Sad)
            basic.pause(1200)
            music.startMelody(music.builtInMelody(Melodies.Chase), MelodyOptions.Once)
            basic.pause(8000)
        }
    }
})
basic.forever(function () {
    if (alert == 1) {
        if (input.pinIsPressed(TouchPin.P1)) {
            pressure = 1
        } else {
            pressure = 0
        }
        if (pressure == 1) {
            basic.showIcon(IconNames.Angry)
            basic.pause(1000)
            music.startMelody(music.builtInMelody(Melodies.Chase), MelodyOptions.Once)
        }
    }
})
