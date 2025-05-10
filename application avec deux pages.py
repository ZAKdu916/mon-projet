import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application avec deux pages")
        self.geometry("400x300")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.pages = {}

        for Page in (AccueilPage, Page1, Page2):
            page = Page(self.container, self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(AccueilPage)

    def show_page(self, page_class):
        page = self.pages[page_class]
        page.tkraise()

class AccueilPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Bienvenue sur l'Accueil", font=("Arial", 18))
        label.pack(pady=10)

        button1 = tk.Button(self, text="Aller à la Page 1", command=lambda: controller.show_page(Page1))
        button1.pack()

        button2 = tk.Button(self, text="Aller à la Page 2", command=lambda: controller.show_page(Page2))
        button2.pack()

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Ceci est la Page 1", font=("Arial", 18))
        label.pack(pady=10)

        button = tk.Button(self, text="Retour à l'Accueil", command=lambda: controller.show_page(AccueilPage))
        button.pack()

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Ceci est la Page 2", font=("Arial", 18))
        label.pack(pady=10)

        button = tk.Button(self, text="Retour à l'Accueil", command=lambda: controller.show_page(AccueilPage))
        button.pack()

if __name__ == "__main__":
    app = Application()
    app.mainloop()