import tkinter 
window = tkinter.Tk()
window.title('tkinter')
window.geometry('300x300+200+400')

label1 = tkinter.Label(window, bd = 100, relief = 'solid', justify = tkinter.LEFT ,text = 'Spirit of Learning', font = 'sans')
label1.pack()

window.mainloop()