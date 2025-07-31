import tkinter as tk

window = tk.Tk()
window.title("제목")
window.geometry('400x300')

font = ('맑은 고딕', 20, 'bold')
label = tk.Label(text='라벨', font=font)
button = tk.Button(text='버튼', font=font)

label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

window.mainloop()