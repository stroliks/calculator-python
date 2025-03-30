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
        self.__view = self.CalculatorViewer(self)
        self.__activate_second_value = False
        self.__first_result = 0
        self.__second_result = 0
        self.__action = None

    def get_view(self):
        return self.__view

    def get_first_result(self):
        return self.__first_result

    def get_second_result(self):
        return self.__second_result

    def get_action(self):
        return self.__action

    def set_action(self, value):
        self.__action = value

    def get_activate_second_value(self):
        return self.get_activate_second_value

    def root_window(self):
        return self.get_view().get_root_window()

    def set_handler_data(self, value):
        self.__handler_data(value)

    def __handler_data(self, value):

        result = int(self.get_view().get_output_label().cget("text"))
        if not self.get_activate_second_value:
            try:
                self.get_first_result = result * 10 + int(value)
                self.get_view().set_update_output(self.get_first_result)

            except:
                self.__operation(value)
            return
        try:
            self.get_second_result = result * 10 + int(value)
            self.get_view().set_update_output(self.get_second_result)
        except:
            self.__operation(value)

    def __operation(self, value):
                if value == "=":
                    if self.get_action == "*":
                        view_result = self.get_first_result * self.get_second_result
                    elif self.get_action == "+":
                        view_result = self.get_first_result + self.get_second_result
                    elif self.get_action == "-":
                        view_result = self.get_first_result - self.get_second_result
                    elif self.get_action == "/":
                        view_result = self.get_first_result / self.get_second_result
                    elif self.get_action == "C":
                        self.get_activate_second_value = False
                        self.get_second_result = 0
                        self.get_first_result = 0
                        self.set_action(None)
                        view_result = self.get_first_result
                    self.get_view().set_update_output(view_result)
                    self.get_first_result = view_result
                    self.get_activate_second_value = False
                    return

                self.set_action(value)
                self.get_activate_second_value = True
                self.get_view().set_update_output(0)
                return


    class CalculatorViewer:

        def __init__(self, CalculatorModel):
            self.handler_data = CalculatorModel.set_handler_data()
            self.__root_window = self.__create_window()
            self.__output_label = None
            self.btn = None
            self.button = []
            self.__create_widgets()

        def get_output_label(self):
            return self.__output_label

        def get_button(self):
            return self.__button

        def __update_output(self, memory):
            self.__output_label.configure(text=memory)

        def set_update_output(self, memory):
            return self.__output_label.configure(text=memory)

        def __create_window(self):
            window = CTk()
            window.geometry("400x200")

            return window

        def get_root_window(self):
            return self.__root_window.mainloop()


        def handler_on_click_btn(self, index):
            btn_value = self.button[index]

            self.handler_data(btn_value)

        # @staticmethod
        # def set_handler_data(value):
        #     CalculatorModel().set_handler_data(value)



        def __create_widgets(self,):
            vidgets = ["7","8","9","C","4","5","6","/","1","2","3","*","0","=","+","-",]
            index = 0

            for c in range(3): self.__root_window.columnconfigure(index=c, weight=1)
            for r in range(4): self.__root_window.rowconfigure(index=r, weight=1)

            self.__output_label = CTkLabel(self.__root_window, text="0")
            self.__output_label.grid(row=0, column=0, columnspan=4)

            for i in range(1,5):
                for j in range(0,4):
                    self.btn = customtkinter.CTkButton(self.__root_window, text=vidgets[index],
                                                       command=lambda index = index: self.handler_on_click_btn(index))
                    self.btn.grid(row=i, column=j)
                    self.button.append(self.btn.cget("text"))
                    index += 1