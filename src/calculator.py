from __future__ import annotations

import customtkinter

from customtkinter import *



class Calculator:

    def __init__(self):
        self.__model = CalculatorModel()

    def run(self):
        self.__model.root_window()


class CalculatorModel:

    def __init__(self):
        self.view = self.CalculatorViewer(self)
        self.__activate_second_value = False
        self.__first_result = 0
        self.__second_result = 0
        self.__action = None

    def root_window(self):
        return self.view.root_window.mainloop()


    def handler_data(self, value):

        result = int(self.view.get_output_label().cget("text"))
        if not self.__activate_second_value:
            try:
                self.__first_result = result * 10 + int(value)
                self.view.update_output(self.__first_result)

            except:
                self.operation(value)
            return
        try:
            self.__second_result = result * 10 + int(value)
            self.view.update_output(self.__second_result)
        except:
            self.operation(value)

    def operation(self, value):
                if value == "=":
                    if self.__action == "*":
                        view_result = self.__first_result * self.__second_result
                    elif self.__action == "+":
                        view_result = self.__first_result + self.__second_result
                    elif self.__action == "-":
                        view_result = self.__first_result - self.__second_result
                    elif self.__action == "/":
                        view_result = self.__first_result / self.__second_result
                    elif self.__action == "C":
                        self.__activate_second_value = False
                        self.__second_result = 0
                        self.__first_result = 0
                        self.__action = None
                        view_result = self.__first_result
                    self.view.update_output(view_result)
                    self.__first_result = view_result
                    self.__activate_second_value = False
                    return

                self.__action = value
                self.__activate_second_value = True
                self.view.update_output(0)
                return


    class CalculatorViewer:

        def __init__(self, CalculatorModel):
            self.handler_data = CalculatorModel.handler_data
            self.root_window = self.create_window()
            self.__output_label = None
            self.__btn = None
            self.__button = []
            self.create_widgets()

        def get_output_label(self):
            return self.__output_label
        def set_output_label(self, value):
            self.__output_label = value
        def update_output(self, memory):
            self.__output_label.configure(text=memory)

        def create_window(self):
            window = CTk()
            window.geometry("400x200")

            return window

        def handler_on_click_btn(self, index):
            btn_value = self.__button[index]
            self.handler_data(btn_value)



        def create_widgets(self, ):
            vidgets = ["7","8","9","C","4","5","6","/","1","2","3","*","0","=","+","-",]
            index = 0

            for c in range(3): self.root_window.columnconfigure(index=c, weight=1)
            for r in range(4): self.root_window.rowconfigure(index=r, weight=1)

            self.set_output_label(CTkLabel(self.root_window, text="0"))
            self.__output_label.grid(row=0, column=0, columnspan=4)

            for i in range(1,5):
                for j in range(0,4):
                    self.__btn = customtkinter.CTkButton(self.root_window, text=vidgets[index],
                                                         command=lambda index = index: self.handler_on_click_btn(index))
                    self.__btn.grid(row=i, column=j)
                    self.__button.append(self.__btn.cget("text"))
                    index += 1