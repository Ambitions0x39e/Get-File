import tkinter as tk

def get_input():
    global code, year, seasons, paper_number
    code = code_entry.get()
    year = year_entry.get()
    seasons = seasons_entry.get()
    paper_number = paper_number_entry.get()
    root.destroy()

def init_tk():
    global code, year, seasons, paper_number
    global code_label, code_entry, year_label, year_entry, seasons_label, seasons_entry, paper_number_label, paper_number_entry
    global root 
    root = tk.Tk()
    root.title("Paper Collector")

    # 获取窗口宽度
    window_width = root.winfo_reqwidth()

    # 计算标签的固定宽度（窗口宽度的10%）
    label_width = int(window_width * 0.1)

    # 输入框1：code
    code_label = tk.Label(root, text="Code:", width=label_width)
    code_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

    code_entry = tk.Entry(root)
    code_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
    root.columnconfigure(1, weight=1)

    # 输入框2：year
    year_label = tk.Label(root, text="Year:", width=label_width)
    year_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

    year_entry = tk.Entry(root)
    year_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

    # 输入框3：seasons
    seasons_label = tk.Label(root, text="Seasons:", width=label_width)
    seasons_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)

    seasons_entry = tk.Entry(root)
    seasons_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

    # 输入框4：paper_number
    paper_number_label = tk.Label(root, text="Paper Number:", width=label_width)
    paper_number_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)

    paper_number_entry = tk.Entry(root)
    paper_number_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

    # 提交按钮
    submit_button = tk.Button(root, text="Submit", command=get_input)
    submit_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    root.mainloop()
    
    return code, year, seasons, paper_number