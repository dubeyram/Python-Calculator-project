import tkinter as tk

window = tk.Tk()
window.title("TK Calculator")
window.geometry("302x375")
window.configure(bg="black")
window.resizable(0, 0)
equal_button_pressed = False
calculator_is_on = False
calculator_is_off = True

# Existing numbers and some operators
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
operators = ["+", "-", "*", "/", "%"]


def sleep_time(message):
    my_entry.delete(0, tk.END)
    my_entry.insert(0, message)
    window.after(3000, clear)


def parse_string(content):
    concatenated_numbers = c = ""
    list_of_numbers_and_operators = list()
    for c in content:
        if c in numbers or c == ".":
            concatenated_numbers += c
        else:
            list_of_numbers_and_operators.append(concatenated_numbers)
            list_of_numbers_and_operators.append(c)
            concatenated_numbers = ""
    if c not in operators:
        list_of_numbers_and_operators.append(concatenated_numbers)
    return list_of_numbers_and_operators


def dot_in_numbers(a_string):
    if "." in a_string:
        return True
    return False


def addition():
    global equal_button_pressed
    if calculator_is_on:
        content = my_entry.get()
        nb_char = len(content)
        # if content == "":
        #     my_entry.insert(0, "0+")
        if content == "0+" or content == "0-" or content == "0" or content == "0.":
            my_entry.delete(0, tk.END)
            my_entry.insert(0, "0+")
        else:
            try:
                l_char = content[(nb_char - 1)]  # last char in content without new operator
                print("last character", l_char)
                # We should do and instead of or
                if l_char not in operators and l_char != ".":
                    my_entry.delete(0, tk.END)
                    my_entry.insert(0, str(eval(content)) + "+")
                if l_char in operators:
                    my_entry.delete(0, tk.END)
                    new_val = eval(content[0:-1])
                    my_entry.insert(0, str(new_val) + "+")
                if l_char == ".":
                    character_before_l_char = content[(nb_char - 2)]
                    if character_before_l_char in operators:
                        new_val = content[0:-2]
                        my_entry.delete(0, tk.END)
                        my_entry.insert(0, new_val + "+")
            except ZeroDivisionError:
                message = 'CAN NOT DIVIDE BY ZERO, RESETTING...'
                sleep_time(message)
            except SyntaxError:
                message = 'SYNTAX ERROR, RESETTING...'
                sleep_time(message)
        equal_button_pressed = False


def subtract():
    global equal_button_pressed
    if calculator_is_on:
        content = my_entry.get()
        nb_char = len(content)
        # if content == "":
        #     my_entry.insert(0, "0-")
        if content == "0+" or content == "0-" or content == "0" or content == "0.":
            my_entry.delete(0, tk.END)
            my_entry.insert(0, "0-")
        else:
            try:
                l_char = content[(nb_char - 1)]
                print("last character", l_char)
                if l_char not in operators and l_char != ".":
                    my_entry.delete(0, tk.END)
                    my_entry.insert(0, str(eval(content)) + "-")
                if l_char in operators:
                    my_entry.delete(0, tk.END)
                    new_val = eval(content[:-1])
                    print(" new value", new_val)
                    my_entry.insert(0, str(new_val) + "-")
                if l_char == ".":
                    character_before_l_char = content[(nb_char - 2)]
                    if character_before_l_char in operators:
                        new_val = content[0:-2]
                        my_entry.delete(0, tk.END)
                        my_entry.insert(0, new_val + "-")
            except ZeroDivisionError:
                message = 'CAN NOT DIVIDE BY ZERO, RESETTING...'
                sleep_time(message)
            except SyntaxError:
                message = 'SYNTAX ERROR, RESETTING...'
                sleep_time(message)
        equal_button_pressed = False


def multiplication():
    global equal_button_pressed
    if calculator_is_on:
        content = my_entry.get()
        nb_char = len(content)
        # if content == "":
        #     my_entry.insert(0, "0")
        if content == "0+" or content == "0-" or content == "0" or content == "0.":
            my_entry.delete(0, tk.END)
            my_entry.insert(0, "0")
        else:
            try:
                l_char = content[(nb_char - 1)]
                print("last character", l_char)
                if l_char not in operators and l_char != ".":
                    my_entry.delete(0, tk.END)
                    my_entry.insert(0, str(eval(content)) + "*")
                if l_char in operators:
                    my_entry.delete(0, tk.END)
                    new_val = eval(content[:-1])
                    print(" new value", str(new_val))
                    my_entry.insert(0, str(new_val) + "*")
                if l_char == ".":
                    character_before_l_char = content[(nb_char - 2)]
                    if character_before_l_char in operators:
                        new_val = content[0:-2]
                        my_entry.delete(0, tk.END)
                        my_entry.insert(0, new_val + "*")
            except ZeroDivisionError:
                message = 'CAN NOT DIVIDE BY ZERO, RESETTING...'
                sleep_time(message)
            except SyntaxError:
                message = 'SYNTAX ERROR, RESETTING...'
                sleep_time(message)
        equal_button_pressed = False


def division():
    global equal_button_pressed
    if calculator_is_on:
        content = my_entry.get()
        nb_char = len(content)
        # if content == "":   Do not need it anymore, because it resets to "0" not ""
        #     my_entry.insert(0, "0")
        if content == "0+" or content == "0-" or content == "0" or content == "0.":
            my_entry.delete(0, tk.END)
            my_entry.insert(0, "0")
        else:
            try:
                l_char = content[(nb_char - 1)]  # last char in content without new operator
                print("last character", l_char)
                if l_char not in operators and l_char != ".":
                    my_entry.delete(0, tk.END)
                    my_entry.insert(0, str(eval(content)) + "/")
                if l_char in operators:
                    my_entry.delete(0, tk.END)
                    new_val = eval(content[:-1])
                    print(" new value", new_val)
                    my_entry.insert(0, str(new_val) + "/")
                if l_char == ".":
                    character_before_l_char = content[(nb_char - 2)]
                    if character_before_l_char in operators:
                        new_val = content[0:-2]
                        my_entry.delete(0, tk.END)
                        my_entry.insert(0, new_val + "/")
            except ZeroDivisionError:
                message = 'CAN NOT DIVIDE BY ZERO, RESETTING...'
                sleep_time(message)
            except SyntaxError:
                message = 'SYNTAX ERROR, RESETTING...'
                sleep_time(message)
        equal_button_pressed = False


def modulo():
    global equal_button_pressed
    if calculator_is_on:
        content = my_entry.get()
        nb_char = len(content)
        # if content == "":   Do not need it anymore, because it resets to "0" not ""
        #     my_entry.insert(0, "0")
        if content == "0+" or content == "0-" or content == "0" or content == "0.":
            my_entry.delete(0, tk.END)
            my_entry.insert(0, "0")
        else:
            try:
                l_char = content[(nb_char - 1)]  # last char in content without new operator
                print("last character", l_char)
                if l_char not in operators and l_char != ".":
                    my_entry.delete(0, tk.END)
                    my_entry.insert(0, str(eval(content)) + "%")
                if l_char in operators:
                    my_entry.delete(0, tk.END)
                    new_val = eval(content[:-1])
                    print(" new value", new_val)
                    my_entry.insert(0, str(new_val) + "%")
                if l_char == ".":
                    character_before_l_char = content[(nb_char - 2)]
                    if character_before_l_char in operators:
                        new_val = content[0:-2]
                        my_entry.delete(0, tk.END)
                        my_entry.insert(0, new_val + "%")
            except ZeroDivisionError:
                message = 'CAN NOT DIVIDE BY ZERO, RESETTING...'
                sleep_time(message)
            except SyntaxError:
                message = 'SYNTAX ERROR, RESETTING...'
                sleep_time(message)
        equal_button_pressed = False


def dot():
    global equal_button_pressed
    if calculator_is_on:
        content = my_entry.get()
        # nb_char = len(content)
        # if content == "":
        #     my_entry.insert(0, "0.")
        if content == "0+" or content == "0-" or content == "0" or content == "0.":
            my_entry.delete(0, tk.END)
            my_entry.insert(0, "0.")
        else:
            # Get the last string from blocks, and check if we have a "." in there
            blocks = parse_string(content)
            a_string = blocks[len(blocks) - 1]
            if not dot_in_numbers(a_string):
                my_entry.delete(0, tk.END)
                my_entry.insert(0, content + ".")
        equal_button_pressed = False


def equal_button():
    global equal_button_pressed
    if calculator_is_on:
        content = my_entry.get()
        # if content == "" or content == "0+" or content == "0-" or content == "0":
        if content == "0+" or content == "0-" or content == "0":
            my_entry.delete(0, tk.END)
            my_entry.insert(0, "0")
        else:
            val = content[len(content) - 1]
            # looking to see if val is in operator
            if val in operators or val == ".":
                content = content[:-1]
            try:
                print(eval(content))
                my_entry.delete(0, tk.END)
                my_entry.insert(0, str(eval(content)))
            except ZeroDivisionError:
                message = 'CAN NOT DIVIDE BY ZERO, RESETTING...'
                sleep_time(message)
            except SyntaxError:
                message = 'SYNTAX ERROR, RESETTING...'
                sleep_time(message)
        equal_button_pressed = True


def clear():
    global equal_button_pressed
    if calculator_is_on:
        my_entry.delete(0, tk.END)
        my_entry.insert(0, "0")
        equal_button_pressed = False


def off_calculator():
    global equal_button_pressed, calculator_is_on, calculator_is_off
    my_entry.delete(0, tk.END)
    my_entry.insert(0, "")
    equal_button_pressed = False
    calculator_is_off = True
    calculator_is_on = False


def on_calculator():
    global equal_button_pressed, calculator_is_on, calculator_is_off
    my_entry.delete(0, tk.END)
    my_entry.insert(0, "0")
    equal_button_pressed = False
    calculator_is_on = True
    calculator_is_off = False


def click_number(number):
    global equal_button_pressed
    if calculator_is_on:
        content = my_entry.get()
        if not equal_button_pressed:
            # if content == "":
            #     my_entry.insert(0, number)
            if content == "0":
                my_entry.delete(0, tk.END)
                my_entry.insert(0, number)
            else:
                if len(content) == 1:
                    content = content + number
                    my_entry.delete(0, tk.END)
                    my_entry.insert(0, content)
                else:
                    op = content[len(content) - 2]
                    print("operator", op)
                    val = content[len(content) - 1]
                    print("val", val)
                    if op in operators and val == "0" and number in numbers:
                        content = content[:-1]
                    content = content + number
                    my_entry.delete(0, tk.END)
                    my_entry.insert(0, content)
        else:
            my_entry.delete(0, tk.END)
            my_entry.insert(0, number)
            equal_button_pressed = False


my_entry = tk.Entry(window, width=45, borderwidth=6, justify="right", bg="black", fg="white")
my_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

# Initialize empty by default the entry.
my_entry.insert(0, "")

# Define Buttons
on_button = tk.Button(window, text="ON", padx=18, pady=20, bg="green", fg="white", command=on_calculator)
off_button = tk.Button(window, text="OFF ", padx=15, pady=20, bg="red", fg="white", command=off_calculator)
modulo_button = tk.Button(window, text="%", padx=22, pady=20, bg="black", fg="white", command=modulo)
clear_button = tk.Button(window, text="AC", padx=19, pady=20, bg="black", fg="white", command=clear)
button_seven = tk.Button(window, text="7", padx=24, pady=20, bg="black", fg="white", command=lambda: click_number("7"))
button_eight = tk.Button(window, text="8", padx=24, pady=20, bg="black", fg="white", command=lambda: click_number("8"))
button_nine = tk.Button(window, text="9", padx=24, pady=20, bg="black", fg="white", command=lambda: click_number("9"))
button_four = tk.Button(window, text="4", padx=24, pady=20, bg="black", fg="white", command=lambda: click_number("4"))
button_five = tk.Button(window, text="5", padx=24, pady=20, bg="black", fg="white", command=lambda: click_number("5"))
button_six = tk.Button(window, text="6", padx=24, pady=20, bg="black", fg="white", command=lambda: click_number("6"))
button_one = tk.Button(window, text="1", padx=24, pady=20, bg="black", fg="white", command=lambda: click_number("1"))
button_two = tk.Button(window, text="2", padx=24, pady=20, bg="black", fg="white", command=lambda: click_number("2"))
button_three = tk.Button(window, text="3", padx=24, pady=20, bg="black", fg="white", command=lambda: click_number("3"))
button_zero = tk.Button(window, text="0", padx=24, pady=20, bg="black", fg="white", command=lambda: click_number("0"))
dot_button = tk.Button(window, text=" .", padx=24, pady=20, bg="black", fg="white", command=dot)
addition_button = tk.Button(window, text="+", padx=23, pady=20, bg="black", fg="white", command=addition)
equal_button = tk.Button(window, text="=", padx=23, pady=20, bg="black", fg="white", command=equal_button)
multiplication_button = tk.Button(window, text="x", padx=24, pady=20, bg="black", fg="white", command=multiplication)
subtract_button = tk.Button(window, text=" -", padx=23, pady=20, bg="black", fg="white", command=subtract)
division_button = tk.Button(window, text="÷", padx=23, pady=20, bg="black", fg="white", command=division)

# Put buttons on the screen
on_button.grid(row=1, column=0)
off_button.grid(row=1, column=1)
modulo_button.grid(row=1, column=2)
clear_button.grid(row=1, column=3)
button_seven.grid(row=2, column=0)
button_eight.grid(row=2, column=1)
button_nine.grid(row=2, column=2)
button_four.grid(row=3, column=0)
button_five.grid(row=3, column=1)
button_six.grid(row=3, column=2)
button_one.grid(row=4, column=0)
button_two.grid(row=4, column=1)
button_three.grid(row=4, column=2)
button_zero.grid(row=5, column=0)
dot_button.grid(row=5, column=1)
addition_button.grid(row=5, column=3)
equal_button.grid(row=5, column=2)
multiplication_button.grid(row=3, column=3)
subtract_button.grid(row=4, column=3)
division_button.grid(row=2, column=3)


window.mainloop()
