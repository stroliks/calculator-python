from __future__ import annotations

import tkinter

from customtkinter import *


class Calculator:

    def __init__(self):
        self.__viewer = CalculatorViewer()
        self.__model = CalculatorModel(self.__viewer)

    def run(self):
        self.registration_events_buttons()

        self.__viewer.root_window.mainloop()

    def registration_events_buttons(self):
        self.__viewer.add_handler_on_click_btn_1(self.__handler_on_click_btn_1)
        self.__viewer.add_handler_on_click_btn_2(self.__handler_on_click_btn_2)
        self.__viewer.add_handler_on_click_btn_3(self.__handler_on_click_btn_3)
        self.__viewer.add_handler_on_click_btn_4(self.__handler_on_click_btn_4)
        self.__viewer.add_handler_on_click_btn_5(self.__handler_on_click_btn_5)
        self.__viewer.add_handler_on_click_btn_6(self.__handler_on_click_btn_6)
        self.__viewer.add_handler_on_click_btn_7(self.__handler_on_click_btn_7)
        self.__viewer.add_handler_on_click_btn_8(self.__handler_on_click_btn_8)
        self.__viewer.add_handler_on_click_btn_9(self.__handler_on_click_btn_9)
        self.__viewer.add_handler_on_click_btn_0(self.__handler_on_click_btn_0)
        self.__viewer.add_handler_on_click_btn_add_operation(self.__handler_on_click_btn_add)
        self.__viewer.add_handler_on_click_btn_sub_operation(self.__handler_on_click_btn_sub)
        self.__viewer.add_handler_on_click_btn_multi_operation(self.__handler_on_click_btn_multi)
        self.__viewer.add_handler_on_click_btn_eq(self.__handler_on_click_btn_eq)
        self.__viewer.add_handler_on_click_btn_cancel(self.__handler_on_click_btn_cancel)

    def __handler_on_click_btn_1(self):
        self.__model.update_memory(1)

    def __handler_on_click_btn_2(self):
        self.__model.update_memory(2)

    def __handler_on_click_btn_3(self):
        self.__model.update_memory(3)

    def __handler_on_click_btn_4(self):
        self.__model.update_memory(4)

    def __handler_on_click_btn_5(self):
        self.__model.update_memory(5)

    def __handler_on_click_btn_6(self):
        self.__model.update_memory(6)

    def __handler_on_click_btn_7(self):
        self.__model.update_memory(7)

    def __handler_on_click_btn_8(self):
        self.__model.update_memory(8)

    def __handler_on_click_btn_9(self):
        self.__model.update_memory(9)

    def __handler_on_click_btn_0(self):
        self.__model.update_memory(0)

    def __handler_on_click_btn_add(self):
        self.__model.update_memory_operation(CalculatorModel.ADD)

    def __handler_on_click_btn_sub(self):
        self.__model.update_memory_operation(CalculatorModel.SUB)

    def __handler_on_click_btn_multi(self):
        self.__model.update_memory_operation(CalculatorModel.MULTI)

    def __handler_on_click_btn_div(self):
        self.__model.update_memory(0)

    def __handler_on_click_btn_eq(self):
        self.__model.solver()

    def __handler_on_click_btn_cancel(self):
        self.__model.clear_memory()

class CalculatorModel:

    NOT_OPERATION = ""

    ADD = "+"
    SUB = "-"
    DIV = "/"
    MULTI = "*"

    def __init__(self, view: CalculatorViewer):
        self.__view = view

        self.__left_memory = 0
        self.__right_memory = 0

        self._operation_memory = CalculatorModel.NOT_OPERATION

    def update_memory(self, param):

        if self._operation_memory is CalculatorModel.NOT_OPERATION:
            self.__left_memory *= 10
            self.__left_memory += param
        else:
            self.__right_memory *= 10
            self.__right_memory += param

        memory_view = self.presenter_memory()
        self.__view.update_output(memory_view)

    def update_memory_operation(self, operation):

        if self.__right_memory != 0 and not (self._operation_memory is CalculatorModel.NOT_OPERATION):

            if CalculatorModel.ADD in self._operation_memory:
                self.add()
                self._operation_memory = operation
                memory_view = self.presenter_memory()
                self.__view.update_output(memory_view)
                return

            elif CalculatorModel.SUB in self._operation_memory:
                self.sub()
                self._operation_memory = operation
                memory_view = self.presenter_memory()
                self.__view.update_output(memory_view)
                return

            elif CalculatorModel.MULTI in self._operation_memory:
                self.multi()
                self._operation_memory = operation
                memory_view = self.presenter_memory()
                self.__view.update_output(memory_view)
                return

        if self.__left_memory != 0:
            self._operation_memory = operation

        memory_view = self.presenter_memory()
        self.__view.update_output(memory_view)


    def clear_memory(self):
        self.__left_memory = 0
        self.__right_memory = 0
        self._operation_memory = CalculatorModel.NOT_OPERATION

        memory_view = self.presenter_memory()
        self.__view.update_output(memory_view)

    def presenter_memory(self):
        result = str(self.__left_memory) + self._operation_memory

        if self.__right_memory != 0 and self._operation_memory != CalculatorModel.NOT_OPERATION:
            result = str(self.__right_memory)

        return result

    def add(self):
        self.__left_memory += self.__right_memory
        self.__right_memory = 0

        memory_view = self.presenter_memory()
        self.__view.update_output(memory_view)

    def sub(self):
        self.__left_memory -= self.__right_memory
        self.__right_memory = 0

        memory_view = self.presenter_memory()
        self.__view.update_output(memory_view)

    def multi(self):
        self.__left_memory *= self.__right_memory
        self.__right_memory = 0

        memory_view = self.presenter_memory()
        self.__view.update_output(memory_view)


    def solver(self):
        flag = False

        if CalculatorModel.ADD in self._operation_memory:
            flag = True
            self.add()

        elif CalculatorModel.SUB in self._operation_memory:
            flag = True
            self.sub()

        elif CalculatorModel.DIV in self._operation_memory:
            flag = True


        elif CalculatorModel.MULTI in self._operation_memory:
            flag = True
            self.multi()

        self._operation_memory = CalculatorModel.NOT_OPERATION
        memory_view = self.presenter_memory()
        self.__view.update_output(memory_view)
        self.__left_memory = 0
        self.__right_memory = 0

        if not flag:
            return


class CalculatorViewer:

    def __init__(self):
        self.root_window = self.__create_window()

        self.output_label = None
        self.btn_1 = None
        self.btn_2 = None
        self.btn_add_operation = None

        self.__create_widgets()

    def update_output(self, memory):
        self.output_label.configure(text=memory)

    def add_handler_on_click_btn_1(self, handler):
        self.btn_1.configure(command=handler)

    def add_handler_on_click_btn_2(self, handler):
        self.btn_2.configure(command=handler)

    def add_handler_on_click_btn_3(self, handler):
        self.btn_3.configure(command=handler)

    def add_handler_on_click_btn_4(self, handler):
        self.btn_4.configure(command=handler)

    def add_handler_on_click_btn_5(self, handler):
        self.btn_5.configure(command=handler)

    def add_handler_on_click_btn_6(self, handler):
        self.btn_6.configure(command=handler)

    def add_handler_on_click_btn_7(self, handler):
        self.btn_7.configure(command=handler)

    def add_handler_on_click_btn_8(self, handler):
        self.btn_8.configure(command=handler)

    def add_handler_on_click_btn_9(self, handler):
        self.btn_9.configure(command=handler)

    def add_handler_on_click_btn_0(self, handler):
        self.btn_0.configure(command=handler)

    def add_handler_on_click_btn_add_operation(self, handler):
        self.btn_add_operation.configure(command=handler)

    def add_handler_on_click_btn_sub_operation(self, handler):
        self.btn_sub_operation.configure(command=handler)

    def add_handler_on_click_btn_multi_operation(self, handler):
        self.btn_multi_operation.configure(command=handler)

    def add_handler_on_click_btn_eq(self, handler):
        self.btn_eq.configure(command=handler)

    def add_handler_on_click_btn_cancel(self, handler):
        self.btn_cancel.configure(command=handler)

    def __create_window(self):
        window = CTk()
        window.geometry("387x300")
        window.title("Калькулятор")

        return window

    def __create_widgets(self):
        self.output_label = CTkLabel(self.root_window, font=(None, 20), width=380, text="0")
        self.output_label.grid(row=0, columnspan=4)

        self.btn_0 = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" 0 ")
        self.btn_0.grid(row=4, column=0, padx=3, pady=3)

        self.btn_1 = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" 1 ")
        self.btn_1.grid(row=3, column=0, padx=3, pady=3)

        self.btn_4 = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" 4 ")
        self.btn_4.grid(row=2, column=0, padx=3, pady=3)

        self.btn_7 = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" 7 ")
        self.btn_7.grid(row=1, column=0, padx=3, pady=3)

        self.btn_8 = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" 8 ")
        self.btn_8.grid(row=1, column=1, padx=3, pady=3)

        self.btn_5 = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" 5 ")
        self.btn_5.grid(row=2, column=1, padx=3, pady=3)

        self.btn_2 = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" 2 ")
        self.btn_2.grid(row=3, column=1, padx=3, pady=3)

        self.btn_cancel = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" C ")
        self.btn_cancel.grid(row=4, column=1, padx=3, pady=3)

        self.btn_9 = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" 9 ")
        self.btn_9.grid(row=1, column=2, padx=3, pady=3)

        self.btn_6 = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" 6 ")
        self.btn_6.grid(row=2, column=2, padx=3, pady=3)

        self.btn_3 = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" 3 ")
        self.btn_3.grid(row=3, column=2, padx=3, pady=3)

        self.btn_eq = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" = ")
        self.btn_eq.grid(row=4, column=2, padx=3, pady=3)

        self.btn_div = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" / ")
        self.btn_div.grid(row=1, column=3, padx=3, pady=3)

        self.btn_multi_operation = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" * ")
        self.btn_multi_operation.grid(row=2, column=3, padx=3, pady=3)

        self.btn_sub_operation = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" - ")
        self.btn_sub_operation.grid(row=3, column=3, padx=3, pady=3)

        self.btn_add_operation = CTkButton(self.root_window, font=(None, 20), width=90, height=60, text=" + ")
        self.btn_add_operation.grid(row=4, column=3, padx=3, pady=3)