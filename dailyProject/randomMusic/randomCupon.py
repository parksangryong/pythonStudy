import tkinter as tk
import random

def good_luck():
    coupons = [ '10등', '9등', '8등', '7등', '6등', '5등', '4등', '3등', '2등', '1등', '꽝']
    pick = random.choice(coupons)
    label.config(text='추첨 결과는 바로바로~~~ \n' +pick + ' 입니다!!!')

    button.config(text='재도전')

window = tk.Tk()
window.title('행운 뽑기')
window.geometry('400x300')

font = ('맑은 고딕', 20, 'bold')
label = tk.Label(text='행운을 뽑아 보세요!', font=font)
button = tk.Button(text='뽑기', font=font, width=5, height=1, command=good_luck)

label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

window.mainloop()