from Tkinter import Frame, Tk, Label, YES, BOTH, Button, Entry, LEFT, RIGHT, END
from tkinter import ttk

app = Tk()
app.title("Tugas Besar 01")

list_data = []


def sorting_table(table, column, is_desc):
    sorting_list = [(table.set(k, column), k) for k in table.get_children()]
    if column == "Waktu Keluar":
        sorting_list.sort(key=lambda t: t[0].split(':'), reverse=is_desc)
    else:
        sorting_list.sort(key=lambda t: int(t[0]), reverse=is_desc)
    for index, (val, k) in enumerate(sorting_list):
        table.move(k, '', index)


def search_call_back():
    try:
        i = [x for x, y in enumerate(list_data) if y[0] == search_box.get()][0]
        display = "Rp. " + str(list_data[i][3])
    except IndexError:
        display = "Not Found"
    except "another error":
        display = "Another Error"
    label_biaya['text'] = display


def input_call_back():
    data = (input_1.get(), input_2.get(), input_3.get(), input_4.get())
    table_1.insert(parent="", index=END, iid=len(list_data), values=data)
    table_2.insert(parent="", index=END, iid=len(list_data), values=data)
    list_data.append(data)

    sorting_table(table_1, "Waktu Keluar", True)
    sorting_table(table_2, "Biaya", True)


def create_table_parking(frame):
    table = ttk.Treeview(frame)
    table["columns"] = ["No Plat Polisi", "Waktu Masuk", "Waktu Keluar", "Biaya"]
    table["show"] = "headings"

    table.column("No Plat Polisi", width=90, anchor='c')
    table.column("Waktu Masuk", width=90, anchor='c')
    table.column("Waktu Keluar", width=90, anchor='c')
    table.column("Biaya", width=90, anchor='c')

    table.heading("No Plat Polisi", text="No Plat Polisi")
    table.heading("Waktu Masuk", text="Waktu Masuk")
    table.heading("Waktu Keluar", text="Waktu Keluar")
    table.heading("Biaya", text="Biaya")
    return table


frame_1 = Frame(app)
Label(frame_1, text="Aplikasi Parkir Kelompok Algorithm01", fg="black").pack()
frame_1.pack(expand=YES, fill=BOTH)

frame_2 = Frame(app)
label_search = Label(frame_2, text="Cari NoPol", fg="black")
label_search.grid(row=0, column=0)
search_box = Entry(frame_2, fg="black")
search_box.grid(row=0, column=1)
search_button = Button(frame_2, text="Cari", fg="black", command=lambda: search_call_back())
search_button.grid(row=0, column=2)
frame_2.pack(expand=YES, fill=BOTH)

frame_3 = Frame(app)
label_1 = Label(frame_3, text="No Plat Polisi", fg="black")
label_1.grid(row=0, column=0)
input_1 = Entry(frame_3, fg="black")
input_1.grid(row=0, column=1)

label_2 = Label(frame_3, text="Waktu Masuk", fg="black")
label_2.grid(row=1, column=0)
input_2 = Entry(frame_3, fg="black")
input_2.grid(row=1, column=1)

label_3 = Label(frame_3, text="Waktu Keluar", fg="black")
label_3.grid(row=2, column=0)
input_3 = Entry(frame_3, fg="black")
input_3.grid(row=2, column=1)

label_4 = Label(frame_3, text="Biaya", fg="black")
label_4.grid(row=3, column=0)
input_4 = Entry(frame_3, fg="black")
input_4.grid(row=3, column=1)

input_button = Button(frame_3, text="Input", fg="black", command=lambda: input_call_back())
input_button.grid(row=3, column=2)
label_display = Label(frame_3, text="Biaya Per Jam", fg="black")
label_display.grid(row=0, column=3)
label_biaya = Label(frame_3, text="Biaya", fg="black")
label_biaya.grid(row=1, column=3, rowspan=2)
frame_3.pack(expand=YES, fill=BOTH)

frame_4 = Frame(app)
label_list_1 = Label(frame_4, text="List Pelanggan Terakhir Keluar", fg="black")
label_list_1.grid(row=0, column=0)
table_1 = create_table_parking(frame_4)
table_1.grid(row=1, column=0)
frame_4.pack(expand=YES, fill=BOTH, side=LEFT)

frame_5 = Frame(app)
label_list_2 = Label(frame_5, text="List Pelanggan Banyak Bayar", fg="black")
label_list_2.grid(row=0, column=0, columnspan=4)
table_2 = create_table_parking(frame_5)
table_2.grid(row=1, column=0)
frame_5.pack(expand=YES, fill=BOTH, side=RIGHT)

app.mainloop()
