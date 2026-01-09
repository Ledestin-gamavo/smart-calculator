# Une calculatrice GUI

# Import de la bibliothèque pour l'interface graphique en python

import tkinter as tk

# Gestion des themes

themes = {
    
    "light": {
        "bg": "#f0f0f0",
        "entry_bg": "white",
        "entry_fg": "black",
        "btn_bg": "#e0e0e0",
        "btn_fg": "black",
        "op_bg": "#ff9800",
        "eq_bg": "#4CAF50",
        "clear_bg": "#f44336"
    },
    
    "dark": {
        "bg": "#1e1e1e",
        "entry_bg": "#2b2b2b",
        "entry_fg": "white",
        "btn_bg": "#3a3a3a",
        "btn_fg": "white",
        "op_bg": "#ffb74d",
        "eq_bg": "#66bb6a",
        "clear_bg": "#e57373"
    }
    
}

current_theme = "light"

# Fonctions pour appliquer les themes

def apply_theme(theme_name):
    
    theme = themes[theme_name]

    root.configure(bg=theme["bg"])
    
    entry.configure(
        
        bg=theme["entry_bg"],
        
        fg=theme["entry_fg"],
        
        insertbackground=theme["entry_fg"]
        
    )

    for btn in all_buttons:
        
        if btn["text"] in "+-*/":
            
            btn.configure(bg=theme["op_bg"], fg=theme["btn_fg"])
            
        elif btn["text"] == "=":
            
            btn.configure(bg=theme["eq_bg"], fg="white")
            
        elif btn["text"] in ("Reset", "C"):
            
            btn.configure(bg=theme["clear_bg"], fg="white")
            
        else:
            
            btn.configure(bg=theme["btn_bg"], fg=theme["btn_fg"])


# Fonction pour basculer entre les themes

def toggle_theme():
    
    global current_theme
    
    current_theme = "dark" if current_theme == "light" else "light"
    
    apply_theme(current_theme)

# Logique de la calculatrice 

# Les boutons pour les chiffres et les opérations

def press(num):
    
    current = entry.get()

    if current == "0":
        
        if num in "0123456789":
            
            entry.delete(0, tk.END)
            
            entry.insert(0, str(num))
            
        else:
            
            entry.insert(tk.END, str(num))
            
    else:
        
        if current[-1] in "+-*/" and num == "0":
            
            entry.insert(tk.END, str(num))
            
        elif current[-2:] in ("+0", "-0", "*0", "/0") and num in "123456789":
            
            entry.delete(len(current)-1, tk.END)
            
            entry.insert(tk.END, str(num))
            
        else:
            
            entry.insert(tk.END, str(num))


def equal():
    
    try:
        
        result = eval(entry.get())
        
        if isinstance(result, float) and result.is_integer():
            
            result = int(result)
            
        entry.delete(0, tk.END)
        
        entry.insert(0, str(result))
        
    except Exception:
        
        entry.delete(0, tk.END)
        
        entry.insert(0, "Error")


def clear():
    
    entry.delete(0, tk.END)
    
    entry.insert(0, "0")
    
    

root = tk.Tk()

root.title("Smart Calculator")

root.geometry("460x600")

root.resizable(True, True)


entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")

entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

entry.insert(0, "0")


buttons = [
    
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    
]



all_buttons = []


for (text, row, col) in buttons:
    
    if text == '=':
        
        btn = tk.Button(root, text=text, font=("Arial", 18), command=equal)
        
    else:
        
        btn = tk.Button(root, text=text, font=("Arial", 18),
                        
                        command=lambda t=text: press(t))
        
        
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    
    all_buttons.append(btn)

clear_btn = tk.Button(root, text='Reset', font=("Arial", 18), command=clear)

clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

all_buttons.append(clear_btn)


theme_btn = tk.Button(root, text="🌙 / ☀", font=("Arial", 14), command=toggle_theme)

theme_btn.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=10, pady=5)

all_buttons.append(theme_btn)


for i in range(7):
    
    root.grid_rowconfigure(i, weight=1)
    
for i in range(4):
    
    root.grid_columnconfigure(i, weight=1)
    

# Lancement de l'application avec le thème par défaut

apply_theme(current_theme)

root.mainloop()
