from __future__ import annotations

import customtkinter

from customtkinter import *



class Calculator:

    def __init__(self):
        self.model = CalculatorModel()

    def run(self):
        self.model.root_window()


class CalculatorModel:

    def __init__(self):
        self.__view = self.CalculatorViewer(self)
        self.activate_second_value = False
        self.first_result = 0
        self.second_result = 0
        self.action = None

    def root_window(self):
        return self.__view.root_window.mainloop()


    def handler_data(self, value):

        result = int(self.__view.output_label.cget("text"))
        if not self.activate_second_value:
            try:
                self.first_result = result*10+int(value)
                self.__view.update_output(self.first_result)

            except:
                self.operation(value)
            return
        try:
            self.second_result = result * 10 + int(value)
            self.__view.update_output(self.second_result)
        except:
            self.operation(value)

    def operation(self, value):
                if value == "=":
                    if self.action == "*":
                        view_result = self.first_result * self.second_result
                    elif self.action == "+":
                        view_result = self.first_result + self.second_result
                    elif self.action == "-":
                        view_result = self.first_result - self.second_result
                    elif self.action == "/":
                        view_result = self.first_result / self.second_result
                    elif self.action == "C":
                        self.activate_second_value = False
                        self.second_result = 0
                        self.first_result = 0
                        self.action = None
                        view_result = self.first_result
                    self.__view.update_output(view_result)
                    self.first_result = view_result
                    self.activate_second_value = False
                    return

                self.action = value
                self.activate_second_value = True
                self.__view.update_output(0)
                return


    class CalculatorViewer:

        def __init__(self, CalculatorModel):
            self.handler_data = CalculatorModel.handler_data
            self.root_window = self.create_window()
            self.output_label = None
            self.btn = None
            self.button = []
            self.create_widgets()

        def update_output(self, memory):
            self.output_label.configure(text=memory)

        def create_window(self):
            window = CTk()
            window.geometry("400x200")

            return window

        def handler_on_click_btn(self, index):
            btn_value = self.button[index]
            self.handler_data(btn_value)



        def create_widgets(self,):
            vidgets = ["7","8","9","C","4","5","6","/","1","2","3","*","0","=","+","-",]
            index = 0

            for c in range(3): self.root_window.columnconfigure(index=c, weight=1)
            for r in range(4): self.root_window.rowconfigure(index=r, weight=1)

            self.output_label = CTkLabel(self.root_window, text="0")
            self.output_label.grid(row=0, column=0, columnspan=4)

            for i in range(1,5):
                for j in range(0,4):
                    self.btn = customtkinter.CTkButton(self.root_window, text=vidgets[index],
                                                       command=lambda index = index: self.handler_on_click_btn(index))
                    self.btn.grid(row=i, column=j)
                    self.button.append(self.btn.cget("text"))
                    index += 1