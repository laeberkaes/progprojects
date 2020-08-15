import secrets
import tkinter as tk

# Hier die Logik

dice = input("Welcher Würfel soll geworfen werden? ")
num = input("Wie oft soll er geworfen werden? ")
mod = input("Zusätzliche Modifikatoren? ")

secretsGenerator = secrets.SystemRandom()
diceVal = secretsGenerator.randint(1,int(dice[1:]))

# Hier das Design
window = tk.Tk()
frame = tk.Frame(master=window)
greeting = tk.Label(master=frame)

greeting.pack()
window.mainloop()