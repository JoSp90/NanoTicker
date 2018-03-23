from tkinter import *
import urllib.request
import json
import threading
from tkinter import ttk
import time, datetime

def main():

    global win
    win = Tk()
    win.tk_setPalette(background='gray48', foreground='white smoke')
    win.title('Nano Ticker')
    win.geometry('288x38')
    
    global T
    T = Text(win, height=3, width=100)
    T.pack()

    T.config(state=DISABLED)
    refresh()
    win.call('wm', 'attributes', '.', '-topmost', True)
    win.mainloop()    
    
def refresh():
    
    global current_time
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")

    # get the information NANO
    url_nano = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/nano/")
    data_nano = json.loads(url_nano.read())
    price_usd_nano = "%.2f" % float(data_nano[0]['price_usd'])
    onehourchange_nano = "%.2f" % float(data_nano[0]['percent_change_1h'])
    rank_nano = data_nano[0]['rank']
    volume_nano = "%.2f" % (float(data_nano[0]['24h_volume_usd'])/1000000.0)
    
    if float(data_nano[0]['percent_change_1h']) >= 0:
             plus_sign_nano = "+"
    else:
             plus_sign_nano = ""

    output_nano = (price_usd_nano+"[USD]    "+ plus_sign_nano + onehourchange_nano+"% " + "   #" + rank_nano + "    " +volume_nano + "[Vol]" )
    #output_nano = f'{price_usd_nano}[USD] {plus_sign_nano}{onehourchange_nano}% #{rank_nano} {volume_nano}[Vol]'
    # update the display
    T.configure(state="normal")
    T.delete("1.0", "end")
    T.insert(END,  '================= ' + str(current_time) + ' ================' + '\n' + output_nano +'\n©joesp90')
    T.configure(state="disabled")

    # call again in 6 seconds
    win.after(6000, refresh)

main()