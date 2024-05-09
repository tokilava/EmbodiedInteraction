import tkinter as tk
import random

"-------Open and read all the Paragraphs-------"
with open("HairlossParagraph.txt", "r", encoding="utf-8") as file:
    hairloss_paragraph = file.read()
with open("Nausea.txt", "r", encoding="utf-8") as file:
    nausea_paragraph = file.read()
with open("LossAppetite.txt", "r", encoding="utf-8") as file:
    LossAppetite_paragraph = file.read()
with open("Fatigue.txt", "r", encoding="utf-8") as file:
    fatigue_paragraph = file.read()

pageCounter = 0     #Make sure which paragraph we are on
labelWidth = 750    #Widht of the window
fonts = ("Times New Roman", "Arial", "Georgia", "Calibri")

paragraph_List = [(hairloss_paragraph, "Hårtab:"), (nausea_paragraph, "Kvalme:"), (LossAppetite_paragraph, "Manglende appetit:"), (fatigue_paragraph, "Træthed (Fatigue):")]

"-------When the Next Page button is pressed we increment pageCounter to move to the next paragraph-------"
def on_button_press():
    global pageCounter
    pageCounter += 1
    "------Pop a random item from the paragraph_List------"
    if len(paragraph_List) != 0:
        random_index = random.randint(0, len(paragraph_List) - 1)
        pop_list_item = paragraph_List.pop(random_index)
        paragraph, current_label = pop_list_item
    # Removes the existing label before adding a new one, this is to avoid all the paragraphs getting ontop of each other
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    if pageCounter == 1:
        label = tk.Label(root, text=current_label, font=("Arial", 16), bg="#2b2b2b", fg="white")
        new_paragraph = tk.Label(root, text=paragraph, font=("Arial", 13), bg="#2b2b2b", fg="white", wraplength = labelWidth)
        label.pack()
        new_paragraph.pack()
    elif pageCounter == 2:
        label = tk.Label(root, text=current_label, font=("Arial", 16), bg="#2b2b2b", fg="white")
        new_paragraph = tk.Label(root, text=paragraph, font=("Arial", 13), bg="#2b2b2b", fg="white", wraplength=labelWidth)
        label.pack()
        new_paragraph.pack()
    elif pageCounter == 3:
        label = tk.Label(root, text=current_label, font=("Arial", 16), bg="#2b2b2b", fg="white")
        new_paragraph = tk.Label(root, text=paragraph, font=("Arial", 13), bg="#2b2b2b", fg="white",wraplength=labelWidth)
        label.pack()
        new_paragraph.pack()
    elif pageCounter == 4:
        label = tk.Label(root, text=current_label, font=("Arial", 16), bg="#2b2b2b", fg="white")
        new_paragraph = tk.Label(root, text=paragraph, font=("Arial", 13), bg="#2b2b2b", fg="white",wraplength=labelWidth)
        label.pack()
        new_paragraph.pack()
    else:
        label = tk.Label(root, text="Tak skal du have for din hjælp.", font=("Arial", 16), bg="#2b2b2b", fg="white")
        label.pack()


root = tk.Tk()
root.title("Side effects")
label = tk.Label(root, text="Hello and welcome. To start the reading, press the button below:", font=("Arial", 16), bg="#2b2b2b", fg="white")
label.pack()
button = tk.Button(root, text="Next Page", command=on_button_press)
button.pack()

root.configure(bg="#1e1e1e")  # Dark gray background color
root.mainloop()


