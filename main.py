userIn = ""
bluetooth.start_uart_service()
basic.show_icon(IconNames.SQUARE)
Translation = ["a", "b", "c"]
wordToBeChecked = ["a", "b", "c"]
WordToBeCheckedPosition = 0

def on_forever():
    for i in range (len(wordToBeChecked) - 1):    
        global userIn, WordToBeCheckedPosition
        userIn = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
        if userIn == wordToBeChecked[WordToBeCheckedPosition]:
            Kitronik_VIEWTEXT32.show_string("" + (Translation[WordToBeCheckedPosition]))
        else:
            WordToBeCheckedPosition += 1
basic.forever(on_forever)
