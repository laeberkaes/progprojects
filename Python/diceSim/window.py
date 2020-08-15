import tkinter as tk

def calcDice():
    dice = ent_dice.get()
    num = ent_num.get()
    mod = ent_mod.get()
    res = int(dice[1:]) * int(num) + int(mod)
    return res

# Set-up the window
window = tk.Tk()
window.title("DiceSim")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_dice = tk.Entry(master=frm_entry, width=10)
lbl_dice = tk.Label(master=frm_entry, text="Würfel")
ent_num = tk.Entry(master=frm_entry,width=10)
lbl_num = tk.Label(master=frm_entry, text="Anzahl")
ent_mod = tk.Entry(master=frm_entry,width=10)
lbl_mod = tk.Label(master=frm_entry, text="Modifikatoren")

ent_dice.grid(row=0, column=0, sticky="e")
lbl_dice.grid(row=0, column=1, sticky="w")
ent_num.grid(row=1, column=0, sticky="e")
lbl_num.grid(row=1, column=1, sticky="w")
ent_mod.grid(row=2, column=0, sticky="e")
lbl_mod.grid(row=2, column=1, sticky="w")

btn_convert = tk.Button(
    master=window,
    text="ROLL",
    command=calcDice()
)
lbl_result = tk.Label(master=window, text="Ergebnis")

# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()

# def calcDice():
#     dice = ent_dice.get()
#     num = ent_num.get()
#     mod = ent_mod.get()
#     lbl_result = int(dice[1:])*int(num)+int(mod)
#
# # Set-up the window
# window = tk.Tk()
# window.title("DiceSim")
# window.resizable(width=True, height=False)
#
# # Create the Fahrenheit entry frame with an Entry
# # widget and label in it
# frm_entry = tk.Frame(master=window)
# ent_dice = tk.Entry(master=frm_entry, width=10)
# ent_num = tk.Entry(master=frm_entry,width=10)
# ent_mod = tk.Entry(master=frm_entry,width=10)
# lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
#
# # Layout the temperature Entry and Label in frm_entry
# # using the .grid() geometry manager
# ent_dice.grid(row=0, column=0, sticky="e")
# ent_num.grid(row=0, column=1, sticky="w")
# ent_mod.grid(row=0, column=2, sticky="w")
# lbl_temp.grid(row=0, column=3, sticky="w")
#
# # Create the conversion Button and result display Label
# btn_convert = tk.Button(
#     master=window,
#     text="ROLL",
#     command=calcDice()
# )
# lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
#
# # Set-up the layout using the .grid() geometry manager
# frm_entry.grid(row=0, column=0, padx=10)
# btn_convert.grid(row=0, column=1, pady=10)
# lbl_result.grid(row=0, column=2, padx=10)

# Run the application
# window.mainloop()


# import tkinter as tk
#
# def fahrenheit_to_celsius():
#     """Convert the value for Fahrenheit to Celsius and insert the
#     result into lbl_result.
#     """
#     fahrenheit = ent_temperature.get()
#     celsius = (5/9) * (float(fahrenheit) - 32)
#     lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
#
# # Set-up the window
# window = tk.Tk()
# window.title("Temperature Converter")
# window.resizable(width=False, height=False)
#
# # Create the Fahrenheit entry frame with an Entry
# # widget and label in it
# frm_entry = tk.Frame(master=window)
# ent_temperature = tk.Entry(master=frm_entry, width=10)
# lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
#
# # Layout the temperature Entry and Label in frm_entry
# # using the .grid() geometry manager
# ent_temperature.grid(row=0, column=0, sticky="e")
# lbl_temp.grid(row=0, column=1, sticky="w")
#
# # Create the conversion Button and result display Label
# btn_convert = tk.Button(
#     master=window,
#     text="\N{RIGHTWARDS BLACK ARROW}",
#     command=fahrenheit_to_celsius
# )
# lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
#
# # Set-up the layout using the .grid() geometry manager
# frm_entry.grid(row=0, column=0, padx=10)
# btn_convert.grid(row=0, column=1, pady=10)
# lbl_result.grid(row=0, column=2, padx=10)
#
# # Run the application
# window.mainloop()

