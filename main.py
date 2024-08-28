import customtkinter
from forex_python.converter import CurrencyRates

currencies = ["USD", 'EUR', 'GBP', 'JYP', 'CAD', 'NGN', 'AUD', 'CHF', 'NZD']


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Currency Converter.")
        # self.geometry(f"{1100}x{580}")
        self.geometry(f"{900}x{500}")
        # self.wm_iconbitmap("logo.png")

        self.frame = customtkinter.CTkFrame(self)

        self.text = customtkinter.CTkLabel(self, text_color="green", font=customtkinter.CTkFont(family="consolas", size=24, slant="roman", underline=True), text="Currency Converter.")
        self.text.pack(pady=1)

        self.empty = customtkinter.CTkLabel(self, text="")
        self.empty.pack(pady=1)


        self.from_var = customtkinter.StringVar(self)
        self.from_var.set('USD')
        self.from_menu = customtkinter.CTkOptionMenu(self, variable=self.from_var, values=currencies)
        self.from_menu.pack(pady=1)

        self.to_var = customtkinter.StringVar(self)
        self.to_var.set('EUR')
        self.to_menu = customtkinter.CTkOptionMenu(self, variable=self.to_var, values=currencies)
        self.to_menu.pack(pady=1)

        self.amount_label = customtkinter.CTkLabel(self, text='Amount:', font=customtkinter.CTkFont(family="consolas"))
        self.amount_label.pack(pady=1)

        self.amount_entry = customtkinter.CTkEntry(self)
        self.amount_entry.pack(pady=1)

        self.convert_button = customtkinter.CTkButton(self, text='Convert', command=self.convert_currency, font=customtkinter.CTkFont(family="consolas"))
        self.convert_button.pack(pady=1)

        self.result_label = customtkinter.CTkLabel(self, text="", font=customtkinter.CTkFont(family="consolas"))
        self.result_label.pack(pady=1)


    def convert_currency(self):
        try:
            from_currency = self.from_var.get()
            to_currency = self.to_var.get()
            amount = float(self.amount_entry.get())

            c_rates = CurrencyRates()

            rate = c_rates.get_rate(from_currency, to_currency)
            converted_amount = amount * rate

            self.result_label.configure(text=f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')
        except ValueError:
            self.result_label.configure(text="Please enter a valid number.")
        except Exception:
            self.result_label.configure(text="Error Occurred")



if __name__ == "__main__":
    app = App()
    app.mainloop()