import tkinter as tk
import random
from PIL import ImageTk, Image



class App:
    def __init__(self, master):
        self.master = master
        self.frames()

    def frames(self):
#mainframe
        self.main=tk.Frame(self.master)
        self.main.config(bg="#F0F0F0")
        self.title = tk.Label(self.main, text="DICE 'n' FLIP", font=("Footlight MT Light", 45, "bold"), bg="#F0F0F0", fg="#1976D2", justify="center")
        self.title.pack(pady=10)
        self.flipcoin = tk.Button(self.main, text="FLIP COIN", font=("Garamond",15), width=30, height=1, bg="#1976D2", fg="#000000", command=self.show_fcframe)
        self.flipcoin.pack(pady=25, padx=25, anchor='center', expand=True)
        self.rolldice = tk.Button(self.main, text="ROLL DICE", font=("Garamond",15), width=30, height=1, bg="#1976D2", fg="#000000", command = self.show_drframe)
        self.rolldice.pack(pady=25, padx=25, anchor='center', expand=True)
        self.exit_button = tk.Button(self.main, text="EXIT", font=("Garamond",15), width=30, height=1, bg="#1976D2", fg="#000000", command=self.exit)
        self.exit_button.pack(pady=25, padx=25, anchor='center', expand=True)
        self.main.pack()
#flipcoinframe
        self.fcframe=tk.Frame(self.master)
        self.fcframe.config(bg="#F0F0F0")
        self.title = tk.Label(self.fcframe, text="FLIP COIN", font=("Footlight MT Light", 45, "bold"), bg="#F0F0F0", fg="#1976D2", justify="center")
        self.title.pack(pady=10)
        self.flipcoin = tk.Button(self.fcframe, text="FLIP COIN", font=("Garamond",15), width=30, height=1, bg="#1976D2", fg="#000000", command=self.display_coin)
        self.flipcoin.pack(pady=25, padx=25, anchor='center', expand=True)
        self.goback=tk.Button(self.fcframe, text="BACK", font=("Garamond",15), width=10, height=1, bg="#FFFDD0", fg="#000000", command=self.two_functions_coin)
        self.goback.pack(side=tk.LEFT, pady=20, padx=20, anchor='center', expand=True)
        self.exit_button = tk.Button(self.fcframe, text="EXIT", font=("Garamond",15), width=10, height=1, bg="#FFFDD0", fg="#000000", command=self.exit)
        self.exit_button.pack(side=tk.RIGHT, pady=20, padx=20, anchor='center', expand=True)
        self.fcframe.pack_forget()
#dicerollframe
        self.drframe=tk.Frame(self.master)
        self.drframe.config(bg="#F0F0F0")
        self.title = tk.Label(self.drframe, text="ROLL DICE", font=("Footlight MT Light", 45, "bold"), bg="#F0F0F0", fg="#1976D2", justify="center")
        self.title.pack(pady=10)
        self.rolldice = tk.Button(self.drframe, text="ROLL DICE", font=("Garamond",15), width=30, height=1, bg="#1976D2", fg="#000000", command=self.display_dice)
        self.rolldice.pack(pady=25, padx=25, anchor='center', expand=True)
        self.goback=tk.Button(self.drframe, text="BACK", font=("Garamond",15), width=10, height=1, bg="#FFFDD0", fg="#000000", command=self.two_functions_dice)
        self.goback.pack(side=tk.LEFT, pady=5, padx=5, anchor='center', expand=True)
        self.exit_button = tk.Button(self.drframe, text="EXIT", font=("Garamond",15), width=10, height=1, bg="#FFFDD0", fg="#000000", command=self.exit)
        self.exit_button.pack(side=tk.RIGHT, pady=5, padx=5, anchor='center', expand=True)
        self.drframe.pack_forget()

    @staticmethod
    def random_coin_num():
        coin_list = ["Head.png", "Tail.png"]
        return random.choice(coin_list)
    
    def display_coin(self):
        if hasattr(self, 'coin_display_label'):
            self.coin_display_label.destroy()
        random_coin = App.random_coin_num()
        self.coin = ImageTk.PhotoImage(Image.open("C:\\Users\\jaya2\\Visual Code\\InternPE\\{}".format(random_coin)))
        self.coin_display_label = tk.Label(self.fcframe, image= self.coin)
        self.coin_display_label.pack(pady=5)
        
    def two_functions_coin(self):
        self.destroy_coin()
        self.show_main()

    def destroy_coin(self):
        self.coin_display_label.destroy()

    @staticmethod
    def random_dice_num():
        dice_list = ["One.jpg", "Two.jpg", "Three.jpg", "Four.jpg", "Five.jpg", "Six.jpg"]
        return random.choice(dice_list)
    
    def display_dice(self):
        if hasattr(self, 'dice_display_label'):
            self.dice_display_label.destroy()
        random_dice = App.random_dice_num()
        self.dice = ImageTk.PhotoImage(Image.open("C:\\Users\\jaya2\\Visual Code\\InternPE\\{}".format(random_dice)))
        self.dice_display_label = tk.Label(self.drframe, image= self.dice)
        self.dice_display_label.pack(pady=5)

    def two_functions_dice(self):
        self.destroy_dice()
        self.show_main()

    def destroy_dice(self):
        self.dice_display_label.destroy()

    def exit(self):
        root.destroy()
        
    def show_main(self):
        self.fcframe.pack_forget()
        self.drframe.pack_forget()
        self.main.pack()

    def show_fcframe(self):
        self.main.pack_forget()
        self.fcframe.pack()
    
    def show_drframe(self):
        self.main.pack_forget()
        self.drframe.pack()



root = tk.Tk()
app = App(root)
root.title("DICE 'n' FLIP")
root.geometry("650x650")
root.configure(bg="#F0F0F0")
root.resizable(False, False)
root.mainloop()
