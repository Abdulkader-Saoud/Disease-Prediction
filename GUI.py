import customtkinter

class FunctionFrame(customtkinter.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.values = values
        self.textboxes = []

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        for i, value in enumerate(self.values):
            customtkinter.CTkLabel(self, text=value).grid(row=i, column=0, sticky="w")
            textbox = customtkinter.CTkTextbox(self, width=50, height=1)
            textbox.grid(row=i, column=1, sticky="w")
            self.textboxes.append(textbox)

    def get(self):
        return [value for value, textbox in zip(self.values, self.textboxes) if textbox.get()]


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("500x400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Left Frame
        self.left_frame = FunctionFrame(self,values=["Max depth", "Min Samples Split"])
        self.left_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew" )
        self.left_frame.grid_propagate(False)

        self.left_button = customtkinter.CTkButton(self, text="Left Button", command=self.left_button_callback)
        self.left_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.middle_frame = FunctionFrame(self, values=["Param1", "Param2"])
        self.middle_frame.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")
        self.middle_frame.grid_propagate(False)

        self.middle_button = customtkinter.CTkButton(self, text="Middle Button", command=self.middle_button_callback)
        self.middle_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.right_frame = FunctionFrame(self, values=["Option1", "Option2"])
        self.right_frame.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nsew")
        self.right_frame.grid_propagate(False)

        self.right_button = customtkinter.CTkButton(self, text="Right Button", command=self.right_button_callback)
        self.right_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        self.log_text = customtkinter.CTkTextbox(self, width=60, height=200)  # Increased height
        self.log_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    def left_button_callback(self):
        self.log_text.insert("end", "Left Button Clicked\n")

    def middle_button_callback(self):
        self.log_text.insert("end", "Middle Button Clicked\n")

    def right_button_callback(self):
        self.log_text.insert("end", "Right Button Clicked\n")


app = App()
app.mainloop()
