# by Arshiya Sharma - made on windows and tested on macOS and Windows 11.
# The dimensions of the GUI window vary from screen to screen - therefore I've selected a safer size.
# libs used - tkinter and pydub
# binary search funtion - fully UNmodified

from pydub.generators import Sine
from pydub import AudioSegment
from tkinter import *

window = Tk()
window.title("Musify")
window.config(bg='#ffeb99')
window.geometry("570x460")
window.resizable(False, False) # so that dimensions dont change

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

notes_real = [130.813, 146.832, 164.814, 174.614, 195.998, 220.000, 246.942, 261.626,0,0,0]
notes_usr = [1,2,3,4,5,6,7,8,9,11,12]

# duration in ms
note_duration = 500
# users music
song_list = []

def notesaver(usr_inp):
    Label(window,text="\t\t\t\t\t\t\t\t",bg="#ffeb99").grid(row=7,column=0,columnspan=9) # to erase previous export message
    while True:
        if usr_inp == 101:
            song_list.clear()
            Label(window, text="You can start over!",  fg='black', bg="#ffeb99").grid(row=7, column=1, columnspan=2, padx=25, pady=20)
            break

        pos = binary_search(notes_usr, usr_inp) # using binary search to search up a note and make music
        if pos==-1:
            window.quit()
            break
        elif pos == 8:
            try:
                song = sum(song_list)
                song.export("Your Music.wav", format="wav")
                Label(window, text="Your music file has been exported!",  fg='black', bg="#ffeb99").grid(row=7, column=1, columnspan=2, padx=25, pady=20)

                song_list.clear()
                break
            except AttributeError:
                Label(window, bg="#ffeb99", fg='black',text="You haven't made any music  :(").grid(row=7, column=1,columnspan=2,padx=25, pady=20)
                break
        else:
            if usr_inp==12:
                sine_wave = Sine(notes_real[pos]).to_audio_segment(duration=250)
            else:
                sine_wave = Sine(notes_real[pos]).to_audio_segment(duration=note_duration)
            song_list.append(sine_wave)
            break


# main buttons and labels
musify = Label(window, fg='darkblue', bg="#ffeb99", text="Musify",font=("Calibri",30,'bold'))
musify.grid(row=0, column=0,columnspan=7,padx=25, pady=2)
cap = Label(window, fg='#237a52', bg="#ffeb99", text="Make your own music!",font=("Calibri",13,'bold'))
cap.grid(row=1, column=0,columnspan=7,padx=25, pady=5)

btn_do= Button(window, fg='black', bg='lightblue',text="Do" ,font=("Calibri",11,'bold'),height= 2, width=7,cursor='star',command= lambda: notesaver(1))
btn_do.grid(row=3, column=0,padx=25, pady=3)

btn_re= Button(window, fg='black', bg='lightblue',text="Re" ,font=("Calibri",11,'bold'),height= 2, width=7,cursor='star',command= lambda: notesaver(2))
btn_re.grid(row=3, column=1,padx=25, pady=3)

btn_mi= Button(window, fg='black', bg='lightblue',text="Mi" ,font=("Calibri",11,'bold'),height= 2, width=7,cursor='star',command= lambda: notesaver(3))
btn_mi.grid(row=3, column=2,padx=25, pady=3)

btn_fa= Button(window, fg='black', bg='lightblue',text="Fa" ,font=("Calibri",11,'bold') ,height= 2, width=7,cursor='star',command= lambda: notesaver(4))
btn_fa.grid(row=3, column=3,padx=25, pady=3)

btn_so= Button(window, fg='black', bg='lightblue',text="So" ,font=("Calibri",11,'bold'),height= 2, width=7,cursor='star',command= lambda: notesaver(5))
btn_so.grid(row=4, column=0,padx=25, pady=20)

btn_la= Button(window, fg='black', bg='lightblue',text="La" ,font=("Calibri",11,'bold'),height= 2, width=7,cursor='star',command= lambda: notesaver(6))
btn_la.grid(row=4, column=1,padx=25, pady=20)

btn_ti= Button(window, fg='black', bg='lightblue',text="Ti" ,font=("Calibri",11,'bold'),height= 2, width=7,cursor='star',command= lambda: notesaver(7))
btn_ti.grid(row=4, column=2,padx=25, pady=20)

btn_doH= Button(window, fg='black', bg='lightblue',text="Do [high]" ,font=("Calibri",11,'bold'),height= 2, width=7,cursor='star',command= lambda: notesaver(8))
btn_doH.grid(row=4, column=3,padx=25, pady=20)

btn_empt= Button(window, fg='black', bg='lightblue',text='0.5s silence' ,font=("Calibri",11,'bold'),height= 2, width=10,cursor='star',command= lambda: notesaver(11))
btn_empt.grid(row=5, column=1,padx=1, pady=1)

btn_empt= Button(window, fg='black', bg='lightblue',text='0.25s silence' ,font=("Calibri",11,'bold'),height= 2, width=10,cursor='star',command= lambda: notesaver(12))
btn_empt.grid(row=5, column=2,padx=1, pady=1)


#for exporting track
btn_exp= Button(window, fg='darkblue',text="Ok" ,font=("Calibri",11,'bold'),height= 2, width=7,cursor='dot',command= lambda: notesaver(9))
btn_exp.grid(row=6, column=0,columnspan=2,padx=25, pady=20)

#for clearing up track [incase of mistakes!!]
btn_clr= Button(window, fg='black',text="Clear" ,font=("Calibri",11,'bold'),height= 2, width=7,cursor='dot',bg='lightgrey',command= lambda: notesaver(101))
btn_clr.grid(row=6, column=1,columnspan=2,padx=25, pady=20)

#for exiting window [without using (x)]
btn_ext= Button(window, fg='red',text="Exit" ,font=("Calibri",11,'bold'),height= 2, width=7,cursor='dot',bg='lightgrey',command= lambda: notesaver(10))
btn_ext.grid(row=6, column=2,columnspan=2,padx=25, pady=20)

# note duration caution
note = Label(window, fg='#3e4042', bg="#ffeb99", text="Note: Duration of each note clicked is 0.5s",font=("Calibri",12))
note.grid(row=7, column=0,columnspan=7,padx=25, pady=5)

window.mainloop()
