from tkinter import *
import ast

class Calculator():
    def __init__(self,r) -> None:
        self.r= r
        self.r.title("Calculator")
        self.r.geometry("325x225")

        # frame 1 for displaying user inputs and results
        self.f1 = Frame(self.r, relief="solid", bg="white", highlightbackground="lightgray", highlightcolor="lightgray", highlightthickness=1)
        self.f1.pack( fill="x", expand=True, padx=2)

        self.user_inputs_and_result = Entry(self.f1)
        self.user_inputs_and_result.configure(borderwidth=0)
        self.user_inputs_and_result.configure(highlightbackground="white", highlightcolor="white")
        self.user_inputs_and_result.pack(padx=5, pady=5)
        self.user_inputs_and_result.insert(0, "")

        # Frame 2 for displaying buttons
        self.f2 = Frame(self.r)
        self.f2.pack()

        self.i=0 # index of last element in the result display screen
        self.current_oprator = None # Selected operator such as "+" , "-"

        # Operations
        self.operations_dict: dict = {"+" : "+", 
                         "-": "-", 
                         "÷": "/", 
                         "×" : "*", 
                         "%": "/100*", 
                         "π": "*3.14", 
                         "(": "(",
                         ")": ")",
                         "xⁿ": "**",
                         "x²": "**2"}
        self.operations:list = list(self.operations_dict.keys())
        
        # Display
        self.display_number_btns()
        self.display_operators_btns()
        # Display other buttons such as "AC", "Delete", "="
        self.clear_btn = Button(self.f2, text="CE", height=2, width=2, foreground="red", command=self.back_space)
        self.clear_btn.grid(row=5, column=2)
        self.all_clear_btn = Button(self.f2, text="AC", height=2, width=2,  foreground="red", command=self.clear_user_inputs)
        self.all_clear_btn.grid(row=5, column=4)
        self.calculate_btn = Button(self.f2, text="=", height=2, width=2, foreground="red", command= self.calculate)
        self.calculate_btn.grid(row=5, column=5)

    # Func to display numbers btns
    def display_number_btns(self) -> None:
        numbers = [1,2,3,4,5,6,7,8,9]
        counter: int = 0
        for x in range(3):
            for y in range(3):
                btn_text = numbers[counter]
                btn = Button(self.f2, text=btn_text, width=2, height=2, command=lambda text=btn_text:self.capture_numerical_inputs(text))
                btn.grid(row=x+2, column=y)
                counter += 1
        # Zero and decimal
        button_0 = Button(self.f2, text="0", width=2, height=2, command=lambda:self.capture_numerical_inputs(0))
        button_0.grid(row=5,column=0) 
        button_decimal = Button(self.f2, text=".", width=2, height=2, command=lambda:self.capture_numerical_inputs("."))
        button_decimal.grid(row=5,column=1) 
        
    # Func to display operations btns
    def display_operators_btns(self) -> None:
        counter: int = 0
        for x in range(4):
            for y in range(3):
                if(counter < len(self.operations)):
                    btn_text = self.operations[counter]
                    btn = Button(self.f2, text= btn_text, width=2, height=2, command=lambda text=btn_text:self.capture_operation_input(text) )
                    counter += 1
                    btn.grid(row=x + 2, column=y + 3) 
    
    # Capture numerical inputs
    def capture_numerical_inputs(self, input) -> None:
        if(self.user_inputs_and_result.get() == "ERROR"):
            self.clear_user_inputs()
            self.user_inputs_and_result.insert(self.i, input)
            self.i= 1

        else:
            self.user_inputs_and_result.insert(self.i, input)
            self.i+=1

    # Capture operation inputs -> when buttons like "+", "-", "%" are clicked
    def capture_operation_input(self, input) -> None:
        if self.i == 0:
            pass
        else:
            self.user_inputs_and_result.insert(self.i, self.operations_dict[input])
            self.i+=len(self.operations_dict[input])


    # Function to erase the last input
    def back_space(self) -> None:
        self.user_inputs_and_result.delete(self.i -1, END)
        self.i = self.i - 1
    
    # All clear (AC) function
    def clear_user_inputs(self) -> None:
        self.i = 0
        self.user_inputs_and_result.delete(0, END)

    # Function to do the actual math
    def calculate(self) -> None:
        try:
            raw_equation = self.user_inputs_and_result.get()
            node = ast.parse(raw_equation, mode="eval")
            result = eval(compile(node, '<string>', 'eval'))
            print(f"Calculating ...  {raw_equation} = {result}")
            self.clear_user_inputs()
            self.user_inputs_and_result.insert(0, result)
            self.i = len(str(result))

        except Exception as e:
            self.clear_user_inputs()
            self.user_inputs_and_result.insert(0,"ERROR")
    
if __name__ == "__main__":
    root = Tk()
    my_calculator = Calculator(root)
    root.mainloop()