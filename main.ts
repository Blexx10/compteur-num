input.onButtonPressed(Button.A, function () {
    Personne += 1
})
input.onButtonPressed(Button.AB, function () {
    Personne = 0
})
input.onButtonPressed(Button.B, function () {
    Personne += -1
})
let Personne = 0
Personne = 0
basic.forever(function () {
    basic.showNumber(Personne)
})
basic.forever(function () {
    if (Personne >= 10) {
        basic.showIcon(IconNames.No)
    }
})
