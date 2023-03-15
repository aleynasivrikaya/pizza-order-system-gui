import tkinter as tk
import tkinter.messagebox as messagebox

class PizzaSiparisUygulamasi(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Pizza Ordering Application")
        self.geometry("600x500+100+100")
        self.configure(bg='brown')


        baslik = tk.Label(text="Global Pizza Hub", fg='black',
                          bg='brown', font='Times 22 bold')
        baslik.pack()

        # Pizza size selection box
        boyut_label = tk.Label(self, text="Please Choose Pizza Size:",bg='brown', fg='white')
        boyut_label.pack()

        boyutlar = [("Small", 50), ("Medium", 85), ("Large", 115)]
        self.boyut = tk.StringVar()
        self.boyut.set("Small")  # Default size : Small

        for boyut, fiyat in boyutlar:
            boyut_radio = tk.Radiobutton(
                self, text=boyut, variable=self.boyut, value=boyut,bg='brown', fg='black')
            boyut_radio.pack()

        # Pizza type selection box
        tur_label = tk.Label(self, text="Please Choose a Pizza Base: :",bg='brown', fg='white')
        tur_label.pack()

        turler = [("Classic", 10), ("Margherita", 15), ("Turk", 20), ("Plain", 12)]
        self.tur = tk.StringVar()
        self.tur.set("Classic")  # Default type : Classic

        for tur, fiyat in turler:
            tur_radio = tk.Radiobutton(
                self, text=tur, variable=self.tur, value=tur,bg='brown', fg='black')
            tur_radio.pack()


        # Pizza ingredients selection box
        malzeme_label = tk.Label(self, text="and Sauce of Your Choice:",bg='brown', fg='white')
        malzeme_label.pack()

        self.malzemeler = {
            "Salami": tk.IntVar(),
            "Mushroom": tk.IntVar(),
            "Sausage": tk.IntVar(),
            "Olive": tk.IntVar(),
            "Corn": tk.IntVar()
        }

        for malzeme, var in self.malzemeler.items():
            malzeme_check = tk.Checkbutton(self, text=malzeme, variable=var,bg='brown', fg='black')
            malzeme_check.pack()

        # Order button
        siparis_button = tk.Button(
            self, text="ORDER", command=self.siparis_ver)
        siparis_button.pack()

        # Order information display
        self.siparis_bilgisi = tk.Label(self, text="",bg='brown', fg='black')
        self.siparis_bilgisi.pack()

    def siparis_ver(self):
        boyut = self.boyut.get()
        fiyat = None

        if boyut == "Small":
            fiyat = 50
        elif boyut == "Medium":
            fiyat = 85
        elif boyut == "Large":
            fiyat = 115


        malzemeler = [malzeme for malzeme,
            var in self.malzemeler.items() if var.get()]

        malzeme_metin = ", ".join(malzemeler)
        if malzeme_metin:
            malzeme_metin = " (" + malzeme_metin + ")"

        toplam_fiyat = fiyat + len(malzemeler)
        siparis_bilgisi = f"{boyut} Size {self.tur.get()} Pizza{malzeme_metin}: {toplam_fiyat} TL"

        self.siparis_bilgisi.config(text=siparis_bilgisi)
        messagebox.showinfo("Order Information", siparis_bilgisi)


uygulama = PizzaSiparisUygulamasi()
uygulama.mainloop()

