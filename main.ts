let WordToBeCheckedPosition = 0
let userIn = ""
bluetooth.startUartService()
basic.showIcon(IconNames.Square)
let Translation = ["a", "b", "c"]
let wordToBeChecked = ["a", "b", "c"]
basic.forever(function () {
    userIn = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
    for (let index = 0; index < wordToBeChecked.length - 1; index++) {
        if (userIn == wordToBeChecked[WordToBeCheckedPosition]) {
            Kitronik_VIEWTEXT32.showString("" + (Translation[WordToBeCheckedPosition]))
        } else {
            WordToBeCheckedPosition += 1
        }
    }
})
