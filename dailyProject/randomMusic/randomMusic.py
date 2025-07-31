import tkinter as tk
import random

def add_music():
    print('add')

def end_music():
    print('end')

def recommend_music():
    print('recommend')


window = tk.Tk()
window.title('랜덤 노래 추천기')
window.geometry('600x400')

font = ('맑은 고딕', 25, 'bold')
label = tk.Label(window,text='당신이 좋아하는 노래를 알려주세요.', font=font, wraplength=500)
entry = tk.Entry(window,font=font, width=20, borderwidth=4)
add_button = tk.Button(window, text='추가', font=font, width=5, height=1, 
                      bg="skyblue", fg="white", 
                      highlightbackground="skyblue", 
                      activebackground="skyblue", 
                      activeforeground="white",
                      relief="raised", 
                      command=add_music)

end_button = tk.Button(window, text='완료', font=font, width=5, height=1, 
                      bg="pink", fg="white", 
                      highlightbackground="pink", 
                      activebackground="pink", 
                      activeforeground="white",
                      relief="raised", 
                      command=end_music)

recommend_button = tk.Button(window, text='노래 추천', font=font, width=20, height=1, 
                           bg="pink", fg="white", 
                           highlightbackground="pink", 
                           activebackground="lightpink", 
                           activeforeground="white",
                           relief="raised", 
                           command=recommend_music)

label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
add_button.place(relx=0.35, rely=0.65, anchor=tk.CENTER)
end_button.place(relx=0.65, rely=0.65, anchor=tk.CENTER)
# recommend_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

window.mainloop()