import csv
import random
import linecache as lc
import tkinter as tk

#Other-----------------------------
number_vocab = 0
lines = 0

global correct_ger
global correct_en

get_en_input = ''
get_ger_input = ''
ad_clicked = ''
correct_ger = ''
correct_en = ''
ger_en_clicked = ''

#Opening-File----------------------
with open('vocab_list.csv', 'a', newline='', encoding='utf-8') as vocab_file_create:
    writer = csv.writer(vocab_file_create, delimiter=';')
    vocab_file_create.close()

#Methods---------------------------
def add_vocab(row_vocab):
    with open('vocab_list.csv', 'a', newline='', encoding='utf-8') as vocab_file_add:
        writing = csv.writer(vocab_file_add, delimiter=';')
        writing.writerow(row_vocab)
        vocab_file_add.close()


def generate_vocab():
    global vocab_split

    with open('vocab_list.csv', 'r', newline='', encoding='utf-8') as vocab_file_learn:
        lines = len(list(csv.reader(vocab_file_learn)))

        number_vocab = random.randint(1, lines)

        particular_line = lc.getline('vocab_list.csv', number_vocab)
        vocab_split = particular_line.split(';')

    if ger_en_clicked == 'ger':
        textfield_en.configure(state='normal')
        textfield_en.delete(0, tk.END)
        insert_vocab(vocab_split)
        textfield_en.configure(state='disabled')
    elif ger_en_clicked == 'en':
        textfield_ger.configure(state='normal')
        textfield_ger.delete(0, tk.END)
        insert_vocab(vocab_split)
        textfield_ger.configure(state='disabled')


def check_vocab(label_instruction):
    if ger_en_clicked == 'ger':
        #0: Number, 1: English, 2: German
        #Display English
        correct_ger = textfield_ger.get()
        if correct_ger == vocab_split[2]:
            label_instruction.configure(foreground='green', text='Great job! Your answer was correct!')
        elif correct_ger == '':
            label_instruction.configure(foreground='red', text='Empty input!')
        else:
            label_instruction.configure(foreground='red', text=f'Your answer was wrong. Here is the correct answer: {vocab_split[2]}')

    elif ger_en_clicked == 'en':
        # Display German
        correct_en = textfield_en.get()
        if correct_en == vocab_split[1]:
            label_instruction.configure(foreground='green', text='Great job! Your answer was correct!')
        elif correct_en == '':
            label_instruction.configure(foreground='red', text='Empty input!')
        else:
            label_instruction.configure(foreground='red', text=f'Your answer was wrong. Here is the correct answer: {vocab_split[1]}\n')


def insert_vocab(vocab_split):
    if ger_en_clicked == 'ger':
        textfield_en.insert(0, vocab_split[1])
    elif ger_en_clicked == 'en':
        textfield_ger.insert(0, vocab_split[2])


def enter_vocab(ad_clicked, input_ger, input_en):
    if (ad_clicked == True and input_en != '' and input_ger != ''):
        with open('vocab_list.csv', 'r+', encoding='utf-8') as vocab_file_read:
            lines = len(list(csv.reader(vocab_file_read))) + 1
            vocab_file_read.close()

        row_vocab = [lines, input_en, input_ger, '']
        add_vocab(row_vocab)

        label_instruction.configure(foreground='green', text=f'Vocabulary added successfully.\nYou have {str(lines)} vocabulary in your list.')


def press_enter(get_en_input, get_ger_input, ad_clicked, label_instruction):
    input_ger = textfield_ger.get()
    input_en = textfield_en.get()
    
    if get_ger_input == True:
        if (input_ger != '' and input_en != ''):
            label_instruction.configure(foreground='black', text='Enter the translation:')
            check_vocab(label_instruction)
            with open('vocab_list.csv', 'r', newline='', encoding='utf-8') as vocab_file_learn:
                islines0 = len(list(csv.reader(vocab_file_learn)))
            if islines0 != 0:
                generate_vocab()
        else:
            label_instruction.configure(foreground='red', text='Empty input!')

    if get_en_input == True:
        if (input_en != '' and input_ger != ''):
            label_instruction.configure(foreground='black', text='Enter the translation:')
            check_vocab(label_instruction)
            with open('vocab_list.csv', 'r', newline='', encoding='utf-8') as vocab_file_learn:
                islines0 = len(list(csv.reader(vocab_file_learn)))
            if islines0 != 0:
                generate_vocab()
        else:
            label_instruction.configure(foreground='red', text='Empty input!')

    enter_vocab(ad_clicked, input_ger, input_en)

    textfield_en.delete(0, tk.END)
    textfield_ger.delete(0, tk.END)


def press_clear():
    textfield_en.delete(0, tk.END)
    textfield_ger.delete(0, tk.END)


def press_main():
    label_instruction.configure(foreground='black', text='Press the "Add/Learn" button to start!')

    textfield_en.configure(state='normal')
    textfield_en.delete(0, tk.END)
    textfield_en.insert(0, 'Disabled')
    textfield_en.configure(foreground='grey', background='lightgrey', state='disabled')

    textfield_ger.configure(state='normal')
    textfield_ger.delete(0, tk.END)
    textfield_ger.insert(0, 'Disabled')
    textfield_ger.configure(foreground='grey', background='lightgrey', state='disabled')

    button_main.configure(state='disabled')
    button_ad.configure(state='normal')
    button_ger.configure(state='disabled')
    button_en.configure(state='disabled')
    button_enter.configure(state='disabled')
    button_clear.configure(state='disabled')

    global get_en_input
    global get_ger_input
    global ad_clicked
    global ger_en_clicked

    get_en_input = False
    get_ger_input = False
    ad_clicked = False
    ger_en_clicked = ''


def press_ad():
    textfield_en.configure(foreground='black', background='white', state='normal')
    textfield_en.delete(0, tk.END)

    textfield_ger.configure(foreground='black', background='white', state='normal')
    textfield_ger.delete(0, tk.END)

    label_instruction.configure(foreground='black', text='Enter the vocabulary you want to add or\n- press the "German" button to learn the German translations\n- press the "English" button to learn the English translations')

    button_ad.configure(state='disabled')
    button_main.configure(state='normal')
    button_ger.configure(state='normal')
    button_en.configure(state='normal')
    button_enter.configure(state='normal')
    button_clear.configure(state='normal')

    global get_en_input
    global get_ger_input
    global ad_clicked
    global ger_en_clicked

    get_en_input = True
    get_ger_input = True
    ad_clicked = True
    ger_en_clicked = ''

    
def press_ger():
    label_instruction.configure(foreground='black', text='Enter the translation:')

    textfield_en.configure(state='normal')
    textfield_en.delete(0, tk.END)
    textfield_en.insert(0, vocab_split[1])
    textfield_en.configure(foreground='black', state='disabled')

    textfield_ger.configure(state='normal')
    textfield_ger.delete(0, tk.END)
    textfield_ger.configure(foreground='black', background='white')

    button_ger.configure(state='disabled')
    button_en.configure(state='normal')
    button_ad.configure(state='normal')
    button_main.configure(state='normal')
    button_enter.configure(state='normal')
    button_clear.configure(state='normal')

    global get_en_input
    global get_ger_input
    global ad_clicked
    global ger_en_clicked

    get_en_input = False
    get_ger_input = True
    ad_clicked = False
    ger_en_clicked = 'ger'


def press_en():
    label_instruction.configure(foreground='black', text='Enter the translation:')

    textfield_ger.configure(state='normal')
    textfield_ger.delete(0, tk.END)
    textfield_ger.insert(0, vocab_split[2])
    textfield_ger.configure(foreground='black', state='disabled')

    textfield_en.configure(state='normal')
    textfield_en.delete(0, tk.END)
    textfield_en.configure(foreground='black', background='white')

    button_en.configure(state='disabled')
    button_ger.configure(state='normal')
    button_ad.configure(state='normal')
    button_main.configure(state='normal')
    button_enter.configure(state='normal')
    button_clear.configure(state='normal')

    global get_en_input
    global get_ger_input
    global ad_clicked
    global ger_en_clicked

    get_en_input = True
    get_ger_input = False
    ad_clicked = False
    ger_en_clicked = 'en'


def hover(e):
    e.widget.configure(foreground='white')

def unhover(e):
    e.widget.configure(foreground='black')


#GUI-------------------------------
window = tk.Tk()
window.resizable(False, False)

label_instruction = tk.Label(window)
label_ger = tk.Label(window)
label_en = tk.Label(window)

textfield_en = tk.Entry(window)
textfield_ger = tk.Entry(window)

button_quit = tk.Button(window)
button_enter = tk.Button(window)
button_clear = tk.Button(window)
button_main = tk.Button(window)
button_ad = tk.Button(window)
button_ger = tk.Button(window)
button_en = tk.Button(window)

window.geometry('700x220')
window.title('Vocabulary Learner')

label_instruction.configure(justify=tk.LEFT, text='Press the "Add" or "Learn" button to start!')
label_instruction.place(x=100, y=10)

label_en.configure(justify=tk.LEFT, text='Textfield English:')
label_en.place(x=60, y=105)

label_ger.configure(justify=tk.LEFT, text='Textfield German:')
label_ger.place(x=60, y=75)

textfield_en.insert(1, 'Disabled')
textfield_en.configure(width=46, foreground='grey', background='lightgrey', state='disabled')
textfield_en.place(x=160, y=105)

textfield_ger.insert(1, 'Disabled')
textfield_ger.configure(width=46, foreground='grey', background='lightgrey', state='disabled')
textfield_ger.place(x=160, y=75)

button_quit.configure(background='red', text='Quit', width=10, command=window.destroy)
button_quit.place(x=560, y=180)
button_quit.bind('<Enter>', hover)
button_quit.bind('<Leave>', unhover)

button_enter.configure(background='limegreen', text='Enter', width=10, state='disabled', command=lambda: press_enter(get_en_input, get_ger_input, ad_clicked, label_instruction))
button_enter.place(x=460, y=100)
button_enter.bind('<Enter>', hover)
button_enter.bind('<Leave>', unhover)

button_clear.configure(background='limegreen', text='Clear', width=10, state='disabled', command=lambda: press_clear())
button_clear.place(x=460, y=70)
button_clear.bind('<Enter>', hover)
button_clear.bind('<Leave>', unhover)

button_main.configure(background='#45cdff', text='Main Menu', width=10, state='disabled', command=lambda: press_main())
button_main.place(x=60, y=140)
button_main.bind('<Enter>', hover)
button_main.bind('<Leave>', unhover)

button_ad.configure(background='#45cdff', text='Add/Learn', width=10, command=lambda: press_ad())
button_ad.place(x=160, y=140)
button_ad.bind('<Enter>', hover)
button_ad.bind('<Leave>', unhover)

button_ger.configure(background='#45cdff', text='German', width=10, state='disabled', command=lambda: [generate_vocab(), press_ger()])
button_ger.place(x=360, y=140)
button_ger.bind('<Enter>', hover)
button_ger.bind('<Leave>', unhover)

button_en.configure(background='#45cdff', text='English', width=10, state='disabled', command=lambda: [generate_vocab(), press_en()])
button_en.place(x=260, y=140)
button_en.bind('<Enter>', hover)
button_en.bind('<Leave>', unhover)


window.mainloop()
