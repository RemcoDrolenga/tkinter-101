import tkinter
window = tkinter.Tk()

AchtergrondList = ["white","yellow","orange", "red", "purple", "black" ]
window.title("My First Window")
window.geometry("50x50")
WithLength = 50
Aftellen = 6

for i in range(6):
    WithLength += 50
    WindowSize = (str(WithLength)+"x"+str(WithLength))
    print(Aftellen)
    Aftellen -= 1
    window.configure(bg=AchtergrondList[i])
    window.geometry(WindowSize)
    window.after(1000,window.update())
print("BOOOM!")
window.after(4000,window.update())
window.destroy()

window.mainloop()