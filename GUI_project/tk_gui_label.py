""" Python tkinter 강좌  : https://076923.github.io/posts/Python-tkinter-2/

    Label, Button, Entry, ListBox, CheckButton 
"""
import tkinter

window=tkinter.Tk()
window.title("KIM HONG WAN")
window.geometry("640x400+100+100")
window.resizable(False, True) # 좌우, 상하

label0=tkinter.Label(window, text="파이썬", width=10, height=5, fg="red", relief="solid")
label0.pack()


count = 0

def countUP():
    global count
    count +=1
    label.config(text=str(count))

# Label을 이용하여 삽입한 이미지나 도표, 그림 등에 사용되는 주석문을 생성할 수 있습니다.
label = tkinter.Label(window, text="0")
label.pack()

# Button을 이용하여 메서드 또는 함수 등을 실행시키기 위한 단추를 생성할 수 있습니다.
button = tkinter.Button(window, overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()


label2 = tkinter.Label(window, text="0")
label2.pack()

def calc(event):
    label2.config(text="결과="+str(eval(entry.get())))

# Entry을 이용하여 텍스트를 입력받거나 출력하기 위한 기입창을 생성할 수 있습니다
entry=tkinter.Entry(window)
entry.bind("<Return>", calc)
entry.pack()


# Listbox을 이용하여 목록을 불러와 추가, 제거 또는 선택하기 위한 리스트박스를 생성할 수 있습니다
listbox = tkinter.Listbox(window, selectmode='extended', height=0)
listbox.insert(0, "1번")
listbox.insert(1, "2번")
listbox.insert(2, "2번")
listbox.insert(3, "2번")
listbox.insert(4, "3번")

listbox.delete(1, 2)

listbox.insert(1, "1-1번")

listbox.pack()

# Checkbutton을 이용하여 옵션 등을 다중 선택하기 위한 체크버튼을 생성할 수 있습니다.
def flash():
    checkbutton1.flash()

CheckVariety_1=tkinter.IntVar()
CheckVariety_2=tkinter.IntVar()

checkbutton1=tkinter.Checkbutton(window, text="O", variable=CheckVariety_1, activebackground="blue")
checkbutton2=tkinter.Checkbutton(window, text="△", variable=CheckVariety_2)
checkbutton3=tkinter.Checkbutton(window, text="X", variable=CheckVariety_2, command=flash)

checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()


# Radiobutton을 이용하여 옵션 등을 단일 선택하기 위한 라디오버튼을 생성할 수 있습니다.
def check():
    label.config(text= "RadioVariety_1 = " + str(RadioVariety_1.get()) + "\n" +
                       "RadioVariety_2 = " + str(RadioVariety_2.get()) + "\n\n" +
                       "Total = "          + str(RadioVariety_1.get() + RadioVariety_2.get()))

RadioVariety_1=tkinter.IntVar()
RadioVariety_2=tkinter.IntVar()

radio1=tkinter.Radiobutton(window, text="1번", value=3, variable=RadioVariety_1, command=check)
radio1.pack()

radio2=tkinter.Radiobutton(window, text="2번(1번)", value=3, variable=RadioVariety_1, command=check)
radio2.pack()

radio3=tkinter.Radiobutton(window, text="3번", value=9, variable=RadioVariety_1, command=check)
radio3.pack()

label=tkinter.Label(window, text="None", height=5)
label.pack()

radio4=tkinter.Radiobutton(window, text="4번", value=12, variable=RadioVariety_2, command=check)
radio4.pack()

radio5=tkinter.Radiobutton(window, text="5번", value=15, variable=RadioVariety_2, command=check)
radio5.pack()


# Menu을 이용하여 자주 사용하는 기능 등을 다양한 선택사항으로 나누는 메뉴을 생성할 수 있습니다.
def close():
    window.quit()
    window.destroy()

menubar=tkinter.Menu(window)

menu_1=tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="하위 메뉴 1-1")
menu_1.add_command(label="하위 메뉴 1-2")
menu_1.add_separator()
menu_1.add_command(label="하위 메뉴 1-3", command=close)
menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)

menu_2=tkinter.Menu(menubar, tearoff=0, selectcolor="red")
menu_2.add_radiobutton(label="하위 메뉴 2-1", state="disable")
menu_2.add_radiobutton(label="하위 메뉴 2-2")
menu_2.add_radiobutton(label="하위 메뉴 2-3")
menubar.add_cascade(label="상위 메뉴 2", menu=menu_2)

menu_3=tkinter.Menu(menubar, tearoff=0)
menu_3.add_checkbutton(label="하위 메뉴 3-1")
menu_3.add_checkbutton(label="하위 메뉴 3-2")
menubar.add_cascade(label="상위 메뉴 3", menu=menu_3)

window.config(menu=menubar)


window.mainloop()



print("Window Close")

