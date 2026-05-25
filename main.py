# game.py
import tkinter as tk

def check_step():
    global step
    val = entry.get().strip().lower()
    
    if step == 1:
        if val == "andrew":
            label.config(text="You are 13. Am I right?", fg="#ffdd59")
            entry.delete(0, tk.END)
            step = 2
        else:
            label.config(text=f"Hello {entry.get()}!", fg="#ff5e7e")
    elif step == 2:
        if val == "yes":
            label.config(text="I know where u live... I am under your bed", fg="#ff4757")
        elif val == "no":
            label.config(text="LIAR thats why i will boil you ALIVE today", fg="#ff6b81")
        else:
            label.config(text="Please answer 'yes' or 'no'.", fg="#ffa502")

step = 1
root = tk.Tk()
root.title("Colorful Name Game")
root.configure(bg="#1a1a2e")

frame = tk.Frame(root, bd=3, relief="solid", bg="#16213e", highlightbackground="#e94560", highlightthickness=2)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="What's your name?", font=("Arial", 16, "bold"), bg="#16213e", fg="#4ee5b6")
label.pack(padx=20, pady=10)

entry = tk.Entry(frame, font=("Arial", 14), bg="#0f3460", fg="#ffffff", insertbackground="white", justify="center")
entry.pack(pady=10)

button = tk.Button(frame, text="Submit", font=("Arial", 12, "bold"), bg="#e94560", fg="#ffffff", activebackground="#ff5e7e", activeforeground="#ffffff", command=check_step)
button.pack(pady=10)

root.mainloop()