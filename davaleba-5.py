from tkinter import *
import json

def products_function():
    chosen_prod_list = []
    var = products.get()
    chosen_prod_list.append(var)

    print(chosen_prod_list)

    with open('info.txt') as json_file:
        data = json.load(json_file)
        print(data)
    new_list = [it for it in data["products"]]
    print(new_list)
    last_list = []
    for it in chosen_prod_list:
        if it in new_list:
            last_list.append(it)
    my_file = open("result.txt","w")
    written = my_file.writeline(str(last_list))
    my_file.close()

master = Tk()
Label(master, text="Enter products:").grid(row=0)
products = Entry(master)
products.grid(row=0, column=1)


Button(master, text='Exit',command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Save',command=products_function).grid(row=3, column=1, sticky=W, pady=4)

mainloop()

