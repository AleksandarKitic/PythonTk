import tkinter as tk
import matplotlib.pyplot as plt
import random

root = tk.Tk()
root.title('User info')
root.geometry('600x480')


def show_label():
    print("First Name: %s\nLast Name: %s\nCode: %s\nMessage: %s" % (f.get(), ln.get(), c.get(), txbox.get()))
    print('-' * 30)


def input_text():
    result_f = f.get()
    result_ln = ln.get()
    result_c = c.get()
    result_txbox = txbox.get()
    results = result_f, result_ln, result_c, result_txbox

    results_box.delete(1.0, 'end-1c')
    results_box.insert('end-1c', results)


tk.Label(root, text='First name:').grid(row=0)
tk.Label(root, text='Last name:').grid(row=1)
tk.Label(root, text='Code:').grid(row=2)
tk.Label(root, text='Message:').grid(row=3)

f = tk.Entry(root)
ln = tk.Entry(root)
c = tk.Entry(root)
txbox = tk.Entry(root)

f.grid(row=0, column=1)
ln.grid(row=1, column=1)
c.grid(row=2, column=1)
txbox.grid(row=3, column=1)


tk.Button(root, text='Quit', fg='red', command=root.quit).grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(root, text='Print', fg='green', command=show_label).grid(row=4, column=1, sticky=tk.W, pady=4)
txt_btn = tk.Button(root, text='Input', fg='blue', command=input_text).grid(row=4, column=2, sticky=tk.W, pady=4)

results_box = tk.Text(root, width=50, height=10)
results_box.grid(row=6, column=0, columnspan=2)
results_box.insert('end-1c', 'Result')

# --------------------------CLASS DIAGRAM ------------------------------------
number_x = []
number_y = []

class Diagraminfo(object):
    def open_tk(self):
        master = tk.Tk()
        master.geometry("600x480")
        master.title('Diagram')

        tk.Label(master, text='Number lower:').grid(row=0)
        tk.Label(master, text='Number upper:').grid(row=1)
        tk.Label(master, text='Diagram(line,bar):').grid(row=2)

        upper_number = tk.Entry(master)
        lower_number = tk.Entry(master)
        diagram = tk.Entry(master)

        upper_number.grid(row=0, column=1)
        lower_number.grid(row=1, column=1)
        diagram.grid(row=2, column=1)

        def checkmath():
            number1 = upper_number.getint(s=15)
            number2 = lower_number.getint(s=0)
            result_text = diagram.get()

            for number in range(0, 15):
                n = random.randrange(number2, number1)
                number_x.append(number)
                number_y.append(n)

            if result_text == 'line':
                now = diagramspec()
                now.linediag()
            elif result_text == 'bar':
                now1 = diagramspec()
                now1.bardiag()
            else:
                print('Diagram is incorrect. Try again!')

        tk.Button(master, text='Quit', fg='red', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
        tk.Button(master, text='Show Diagram', fg='green', command=checkmath).grid(row=3, column=1, sticky=tk.W,
                                                                                       pady=4)

class diagramspec(Diagraminfo):
    def linediag(self):
        plt.plot(number_x, number_y, label='Price', linestyle='-.', linewidth='1', marker='o', markersize='4',
                 color='red')
        plt.rc('grid', color='#bbb', linestyle='--')
        plt.title('Diagram line statistics.', fontdict={'fontname': 'Courier New', 'fontsize': 20})
        plt.xlabel('Days', fontdict={'fontname': 'Courier New', 'fontsize': 20})
        plt.ylabel('Statistics', fontdict={'fontname': 'Courier New', 'fontsize': 20})
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        plt.legend()
        plt.grid()
        plt.show()

    def bardiag(self):
        plt.bar(number_x, number_y, label='Price', align='center', color='green')
        plt.title('Diagram bar statistics.', fontdict={'fontname': 'Courier New', 'fontsize': 20})
        plt.xlabel('Days', fontdict={'fontname': 'Courier New', 'fontsize': 20})
        plt.ylabel('Statistics', fontdict={'fontname': 'Courier New', 'fontsize': 20})
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        plt.legend()
        plt.show()


tk.Button(root, text='Diagram', fg='black', command=Diagraminfo().open_tk,).grid(row=4, column=3, sticky=tk.W,
                                                                                      pady=4)

root.mainloop()
