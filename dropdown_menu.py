from tkinter import *

class UserChoices():

    def __init__(self, master, room, original_cards, cards_shown):

        self.room = room
        self.orginal_cards = original_cards
        self.cards_shown = cards_shown
        self.people = ["Mustard", "Trump", "Farage", "Peacock"]
        self.weapons = ["rope", "dagger", "revolver", "candlestick"]

        self.var_person = StringVar(master)
        self.var_person.set("Person") # default value
        self.var_weapon = StringVar(master)
        self.var_weapon.set("Weapon") # default value

        self.L = Label(master, bg = "red")
        self.L.config(text = "You have been brought to the: " + self.room)
        self.L.pack(fill = X)

        self.L1 = Label(master, bg = "green")
        self.L1.config(text = "You were dealt \n" + (", ".join(self.orginal_cards)))
        self.L1.pack(fill = X)

        self.L2 = Label(master, bg = "yellow")
        self.L2.config(text = "Comp has shown you \n" + (", ".join(self.cards_shown)))
        self.L2.pack(fill = X)

        self.p = OptionMenu(master, self.var_person, *self.people)
        self.p.pack()
        self.w = OptionMenu(master, self.var_weapon, *self.weapons)
        self.w.pack()

        self.button = Button(master, text="submit", command=self.person)
        self.button.pack()
        self.button = Button(master, text="Quit", command=master.destroy)
        self.button.pack()


    def person(self):
        return self.var_person.get(), self.var_weapon.get()
