input.onButtonPressed(Button.A, function () {
    basic.showNumber(krok)
    basic.pause(200)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    krok = 0
    basic.showNumber(krok)
    basic.pause(200)
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
    krok += 1
})
let krok = 0
krok = 0
basic.forever(function () {
	
})
