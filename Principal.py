import fun
from collections import Counter
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os


# fun_gui.show_gui()


class MainWindow:
    def __init__(self, master):
        self.master = master
        list_flowers = ['Cosmos', 'Hyacinth', 'Lily', 'Mum', 'Pansy', 'Rose', 'Tulip', 'Windflower']

        self.frame_flower = tk.Frame(master, bg="green")
        self.frame_flower.pack(side=tk.LEFT, padx=5)

        self.frame_select = tk.Frame(master, bg="red")
        self.frame_select.pack(side=tk.LEFT, padx=5, fill=tk.Y)
        self.frame_search = tk.Frame(self.frame_select, bg="bisque", pady=10, height=200)
        self.frame_search.pack(fill=tk.Y)
        self.frame_p1 = tk.Frame(self.frame_select, bg="brown", pady=0)
        self.frame_p1.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.frame_p2 = tk.Frame(self.frame_select, bg="blue", pady=0)
        self.frame_p2.pack(expand=tk.TRUE, fill=tk.BOTH)

        self.frame_results = tk.Frame(master, bg="cyan")
        self.frame_results.pack(side=tk.LEFT, padx=5, fill=tk.Y)
        # self.frame_resume = tk.Frame(self.frame_results, bg="orange", pady=0)
        # self.frame_resume.pack(expand=tk.TRUE, fill=tk.Y)
        # self.frame_table = tk.Frame(self.frame_results, bg="coral", pady=0)
        # self.frame_table.pack(expand=tk.TRUE, fill=tk.Y)
        i = 0
        self.photo = []
        self.v_flower = tk.StringVar(master, 'Cosmos')
        for flower in list_flowers:
            filename = 'img\gray_' + flower.lower() + '.png'
            flower_img = Image.open(filename)
            self.photo.append(ImageTk.PhotoImage(flower_img))
            self.rb = tk.Radiobutton(self.frame_flower,
                                     image=self.photo[i],
                                     indicatoron=0,
                                     pady=0,
                                     width=50,
                                     variable=self.v_flower,
                                     value=flower)
            self.rb.pack(fill=tk.BOTH, pady=5)
            i += 1

        rose_gens = {
            'all': ['0000', '0001', '0002', '0010', '0011', '0012', '0020', '0021', '0022', '0100', '0101', '0102',
                    '0110', '0111', '0112', '0120', '0121', '0122', '0200', '0201', '0202', '0210', '0211', '0212',
                    '0220', '0221', '0222', '1000', '1001', '1002', '1010', '1011', '1012', '1020', '1021', '1022',
                    '1100', '1101', '1102', '1110', '1111', '1112', '1120', '1121', '1122', '1200', '1201', '1202',
                    '1210', '1211', '1212', '1220', '1221', '1222', '2000', '2001', '2002', '2010', '2011', '2012',
                    '2020', '2021', '2022', '2100', '2101', '2102', '2110', '2111', '2112', '2120', '2121', '2122',
                    '2200', '2201', '2202', '2210', '2211', '2212', '2220', '2221', '2222'],
            'native': ['0010', '0100', '2001'],
            'hybrid': ['2022', '2211']
        }
        tulip_gens = {
            'all': ['000', '001', '002', '010', '011', '012', '020', '021', '022', '100', '101', '102', '110', '111',
                    '112', '120', '121', '122', '200', '201', '202', '210', '211', '212', '220', '221', '222'],
            'native': ['001', '020', '201'],
            'hybrid': ['101', '120', '210']
        }
        pansy_gens = {
            'all': ['000', '001', '002', '010', '011', '012', '020', '021', '022', '100', '101', '102', '110', '111',
                    '112', '120', '121', '122', '200', '201', '202', '210', '211', '212', '220', '221', '222'],
            'native': ['001', '020', '200'],
            'hybrid': ['102', '221']
        }
        cosmo_gens = {
            'all': ['000', '001', '002', '010', '011', '012', '020', '021', '022', '100', '101', '102', '110', '111',
                    '112', '120', '121', '122', '200', '201', '202', '210', '211', '212', '220', '221', '222'],
            'native': ['001', '021', '200'],
            'hybrid': ['112', '211']
        }
        lily_gens = {
            'all': ['000', '001', '002', '010', '011', '012', '020', '021', '022', '100', '101', '102', '110', '111',
                    '112', '120', '121', '122', '200', '201', '202', '210', '211', '212', '220', '221', '222'],
            'native': ['002', '020', '201'],
            'hybrid': ['210', '212', '221']
        }
        hyacinth_gens = {
            'all': ['000', '001', '002', '010', '011', '012', '020', '021', '022', '100', '101', '102', '110',
                    '111', '112', '120', '121', '122', '200', '201', '202', '210', '211', '212', '220', '221',
                    '222'],
            'native': ['001', '020', '201'],
            'hybrid': ['101', '120', '210']
        }
        windflower_gens = {
            'all': ['000', '001', '002', '010', '011', '012', '020', '021', '022', '100', '101', '102', '110',
                    '111', '112', '120', '121', '122', '200', '201', '202', '210', '211', '212', '220', '221',
                    '222'],
            'native': ['001', '020', '200'],
            'hybrid': ['102', '221']
        }
        mum_gens = {
            'all': ['000', '001', '002', '010', '011', '012', '020', '021', '022', '100', '101', '102', '110', '111',
                    '112', '120', '121', '122', '200', '201', '202', '210', '211', '212', '220', '221', '222'],
            'native': ['001', '020', '200'],
            'hybrid': ['112', '211']
        }
        self.flower_gens = {'Rose': rose_gens,
                            'Tulip': tulip_gens,
                            'Pansy': pansy_gens,
                            'Cosmos': cosmo_gens,
                            'Lily': lily_gens,
                            'Hyacinth': hyacinth_gens,
                            'Windflower': windflower_gens,
                            'Mum': mum_gens}

        flower_cat = ['native', 'hybrid', 'all']
        cosmo_clr = ['White', 'Yellow', 'Red']

        # ==========Search gen============
        tk.Label(self.frame_search, text='Search gen').pack()

        self.v_cat = tk.StringVar(master, 'native')
        for cat in flower_cat:
            self.rb_cat1 = tk.Radiobutton(self.frame_search,
                                          text=cat,
                                          pady=0,
                                          width=10,
                                          variable=self.v_cat,
                                          command=self.change_cat,
                                          value=cat)
            self.rb_cat1.pack(fill=tk.BOTH, pady=5)
            i += 1

        self.v_clr = tk.StringVar(master, cosmo_clr[0])
        self.cb_clr = ttk.Combobox(self.frame_search,
                                   values=cosmo_clr,
                                   textvariable=self.v_clr)
        self.cb_clr.bind('<<ComboboxSelected>>', self.change_clr)
        self.cb_clr.pack()

        self.v_gen = tk.StringVar(master, 'rryyWw')
        self.cb_gen = ttk.Combobox(self.frame_search,
                                   values=['rryyWw'],
                                   textvariable=self.v_gen)
        self.cb_gen.pack()

        self.btn_p1 = tk.Button(self.frame_search,
                                text='Parent 1',
                                command=lambda: self.v_entry1.set(self.v_gen.get()))
        self.btn_p1.pack(side=tk.LEFT, expand=tk.TRUE)
        self.btn_p2 = tk.Button(self.frame_search,
                                text='Parent 2',
                                command=lambda: self.v_entry2.set(self.v_gen.get()))
        self.btn_p2.pack(side=tk.LEFT, expand=tk.TRUE)

        self.img_base = tk.PhotoImage(width=50, height=50)
        # ==========Parent 1============
        tk.Label(self.frame_p1, text='Parent 1').pack(pady=5)

        self.v_entry1 = tk.StringVar(master, 'rryyWw')
        self.v_entry1.trace_add("write", self.change_img1)
        self.entry_p1 = tk.Entry(self.frame_p1, textvariable=self.v_entry1)
        self.entry_p1.pack(pady=5)

        self.img_p1 = tk.Label(self.frame_p1, image=self.img_base, bg = 'light blue')
        self.img_p1.pack(pady=5)

        # ==========Parent 2============
        tk.Label(self.frame_p2, text='Parent 2').pack(pady=5)

        self.v_entry2 = tk.StringVar(master, 'rrYYWw')
        self.v_entry2.trace_add("write", self.change_img2)
        self.entry_p2 = tk.Entry(self.frame_p2, textvariable=self.v_entry2)
        self.entry_p2.pack(pady=5)

        self.img_p2 = tk.Label(self.frame_p2, image=self.img_base)
        self.img_p2.pack(pady=5)

        # RUN
        self.btn_p2 = tk.Button(self.frame_select,
                                text='Run',
                                command=self.run)
        self.btn_p2.pack(pady=5)

    def change_cat(self):
        flower = self.v_flower.get()
        category = self.v_cat.get()
        gens_flower_cat = self.flower_gens[flower][category]
        colors_flower_cat = list(map(fun.find_color, gens_flower_cat, [flower] * len(gens_flower_cat)))

        values_clrs = fun.unique(colors_flower_cat)
        self.cb_clr.config(values=values_clrs)
        self.v_clr.set(values_clrs[0])

        gens_flower_cat_clr = [x for x, y in zip(gens_flower_cat, colors_flower_cat) if y == values_clrs[0]]
        gens_flower_cat_clr = list(map(fun.ter_to_gen, gens_flower_cat_clr))
        self.cb_gen.config(values=gens_flower_cat_clr)
        self.v_gen.set(gens_flower_cat_clr[0])

    def change_clr(self, eventObject):
        flower = self.v_flower.get()
        category = self.v_cat.get()
        color = self.v_clr.get()
        gens_flower_cat = self.flower_gens[flower][category]
        colors_flower_cat = map(fun.find_color, gens_flower_cat, [flower] * len(gens_flower_cat))

        gens_flower_cat_clr = [x for x, y in zip(gens_flower_cat, colors_flower_cat) if y == color]
        gens_flower_cat_clr = list(map(fun.ter_to_gen, gens_flower_cat_clr))
        self.cb_gen.config(values=gens_flower_cat_clr)
        self.v_gen.set(gens_flower_cat_clr[0])

    def run(self):
        self.frame_results.pack_forget()
        self.frame_results = tk.Frame(master, bg="cyan", pady=0)
        self.frame_results.pack(expand=tk.TRUE, fill=tk.Y)
        self.frame_resume = tk.Frame(self.frame_results, bg="orange", pady=0)
        self.frame_resume.pack(expand=tk.TRUE, fill=tk.X)
        self.frame_table = tk.Frame(self.frame_results, bg="coral", pady=0)
        self.frame_table.pack(expand=tk.TRUE, fill=tk.X)

        parent1 = self.v_entry1.get()
        parent2 = self.v_entry2.get()
        flower = self.v_flower.get()

        color_p1 = fun.find_color(fun.gen_to_ter(parent1), flower)
        color_p2 = fun.find_color(fun.gen_to_ter(parent2), flower)
        print(color_p1, color_p2, flower)

        txt_p1 = 'Parent 1: ' + parent1 + ' [' + color_p1 + ']'
        txt_p2 = 'Parent 2: ' + parent2 + ' [' + color_p2 + ']'
        tk.Label(self.frame_resume, text=txt_p1, anchor=tk.W, width=30).pack()
        tk.Label(self.frame_resume, text=txt_p2, anchor=tk.W, width=30).pack()

        table, c1, c2 = fun.punnet(parent1, parent2, 2, False)

        flat_list = [item for sublist in table for item in sublist]

        unique_gens = Counter(flat_list)
        gen_name = unique_gens.keys()
        gen_count = unique_gens.values()
        sum_gen_count = sum(gen_count)
        color_list = list(map(fun.find_color, list(map(fun.gen_to_ter, gen_name)), [flower] * len(unique_gens)))

        # tk.Label(self.results, text='', anchor=tk.W).pack()
        # tk.Label(self.results, text='Gen         Propability', anchor='w', width=wlabels).pack()
        wlabels = 10
        tk.Label(self.frame_table, text='Gen', anchor='w', width=wlabels).grid(row=0, column=0, stick=tk.W)
        tk.Label(self.frame_table, text='Propability', anchor='w', width=wlabels).grid(row=0, column=1, stick=tk.W)
        tk.Label(self.frame_table, text='Color', anchor='w', width=wlabels).grid(row=0, column=2, stick=tk.W)
        i = 1
        names = []
        buttons1 = []
        buttons2 = []
        for [name, count, color] in zip(gen_name, gen_count, color_list):
            # text_gen_prop = name + ': ' + str(count / sum_gen_count) + ' ' + color
            # tk.Label(self.results, text=text_gen_prop, anchor=tk.W, width=wlabels).pack()

            tk.Label(self.frame_table, text=name, anchor=tk.W, width=wlabels).grid(row=i, column=0, stick=tk.W)
            tk.Label(self.frame_table, text=str(count / sum_gen_count), anchor=tk.W, width=wlabels).grid(row=i,
                                                                                                         column=1,
                                                                                                         stick=tk.W)
            tk.Label(self.frame_table, text=color, anchor=tk.W, width=wlabels).grid(row=i, column=2, stick=tk.W)
            btn_p1_mini = tk.Button(self.frame_table,
                                    text='P1',
                                    anchor=tk.W,
                                    command=lambda idx = i-1: self.update_entry(names, idx, 1)
                                    )
            btn_p1_mini.grid(row=i, column=3)

            btn_p2_mini = tk.Button(self.frame_table,
                                    text='P2',
                                    anchor=tk.W,
                                    command=lambda idx = i-1: self.update_entry(names, idx, 2)
                                    )
            btn_p2_mini.grid(row=i, column=4)
            #btn_p2_mini.bind("<Button-1>", lambda e: self.update_entry(e, names, buttons2, 2))

            names.append(name)
            i += 1

    def change_img1(self, a, b, c):
        gen = self.v_entry1.get()
        ter = fun.gen_to_ter(gen)
        try:
            color = fun.gens_with_colors(self.v_flower.get())[ter]
            filename = os.path.join('img', color + '_' + self.v_flower.get() + '.png')
            open_img = Image.open(filename.lower())
            print(open_img.mode)
            flower_img = ImageTk.PhotoImage(open_img)
            self.img_p1.image = flower_img
            self.img_p1.config(image=flower_img)
        except KeyError:
            self.img_p1.config(image=self.img_base)

    def change_img2(self, a, b, c):
        gen = self.v_entry2.get()
        ter = fun.gen_to_ter(gen)
        try:
            color = fun.gens_with_colors(self.v_flower.get())[ter]
            filename = os.path.join('img', color + '_' + self.v_flower.get() + '.png')
            open_img = Image.open(filename.lower())
            print(open_img.mode)
            flower_img = ImageTk.PhotoImage(open_img)
            self.img_p2.image = flower_img
            self.img_p2.config(image=flower_img)
        except KeyError:
            self.img_p2.config(image=self.img_base)

    def update_entry(self, names, idx, p):
        gen = names[idx]

        if p == 1:
            self.v_entry1.set(gen)
        if p == 2:
            self.v_entry2.set(gen)


master = tk.Tk()
window = MainWindow(master)
master.mainloop()

# Calc for later
parent1 = 'RRyywwbb'  # yellow
parent2 = 'RRyywwBb'  # red
parent3 = 'rryyWW'  # white
flower = 'Rose'
color_p1 = fun.find_color(fun.gen_to_ter(parent1), flower)
color_p2 = fun.find_color(fun.gen_to_ter(parent2), flower)

print('Parent 1: ', parent1, '[', color_p1, ']')
print('Parent 2: ', parent2, '[', color_p2, ']')

table, c1, c2 = fun.punnet(parent1, parent2, 2, False)

flat_list = [item for sublist in table for item in sublist]

unique_gens = Counter(flat_list)
gen_name = unique_gens.keys()
gen_count = unique_gens.values()
sum_gen_count = sum(gen_count)
color_list = list(map(fun.find_color, list(map(fun.gen_to_ter, gen_name)), [flower] * len(unique_gens)))
print('')
print('Gen         Propability')
for [name, count, color] in zip(gen_name, gen_count, color_list):
    print(name, ': ', count / sum_gen_count, color)

# print(gen_keys)
# print(gen_values)


unique_colors = Counter(color_list)
color_name = unique_colors.keys()
color_count = unique_colors.values()
sum_color_count = sum(color_count)
print('')
print('Color      Propability')
for [name, count] in zip(color_name, color_count):
    print(name, ': ', count / sum_color_count)
