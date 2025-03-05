from __future__ import annotations

import customtkinter
from customtkinter import *

class Calculator:

    def __init__(self):
        self.viewer = CalculatorViewer()
        self.model = CalculatorModel(self.viewer)

    def run(self):
        self.viewer.root_window.mainloop()


class CalculatorModel:

    def __init__(self, view: CalculatorViewer):
        self.__view = view

    def handler_data(self, value):
        result = int(self.__view.output_label.cget("text"))
        try:
            first_result = result*10+int(value)
            self.__view.update_output(first_result)
        except:
            if value == "=":
                if pre_value == "*":
                    view_result = first_result * result
                elif pre_value == "+":
                    view_result = first_result + result
                elif pre_value == "-":
                    view_result = first_result - result
                elif pre_value == "/":
                    view_result = first_result / result
                else:
                    view_result = result
                self.__view.update_output(view_result)
                activate = False
            pre_value = value
            activate = True
            view_result = result
            self.__view.update_output(view_result)


class CalculatorViewer:

    def __init__(self):
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

        btn_value = self.button[index].cget("text")
        model = CalculatorModel(self)
        model.handler_data(btn_value)


    def create_widgets(self,):
        vidgets = ["7","8","9","C","4","5","6","%","1","2","3","*","0","=","+","-",]
        index = 0

        for c in range(3): self.root_window.columnconfigure(index=c, weight=1)
        for r in range(4): self.root_window.rowconfigure(index=r, weight=1)

        self.output_label = CTkLabel(self.root_window, text="0")
        self.output_label.grid(row=0, column=0, columnspan=4)

        for i in range(1,5):
            for j in range(0,4):
                self.btn = customtkinter.CTkButton(self.root_window, text=vidgets[index], command=lambda index=index: self.handler_on_click_btn(index))
                self.btn.grid(row=i, column=j)
                self.button.append(self.btn)
                index += 1