import tkinter
turn = 0
window = tkinter.Tk()
window.title("octopustacto")

button_widget = tkinter.Button(window, text="", command = tictacto(turn))
button_widget.pack()
window.mainloop()

