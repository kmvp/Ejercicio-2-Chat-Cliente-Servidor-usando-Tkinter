from tkinter import *
import socket
from threading import *
from tkinter import ttk, font, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import Menu

class Receive():
  def __init__(self, server, gettext):
    #self.server = server
    #self.gettext = gettext
    while 1:
      try:
        text = server.recv(1024)
        if not text: break
        gettext.configure(state='normal')
        gettext.insert(END,'Servidor >> %s\n'%text)
        gettext.configure(state='disabled')
        gettext.see(END)
      except:
        break
class App(Thread):
  client = socket.socket()
  client.connect(('localhost', 20001))
  def __init__(self, master):
    Thread.__init__(self)
    frame = Frame(master)
    frame.pack()
    self.gettext = ScrolledText(frame, height=20,width=80)
    self.gettext.pack()
    self.gettext.insert(END,'Bienvenido al Chat Cliente\n\n')
    self.gettext.configure(state='disabled')
    sframe = Frame(frame)
    sframe.pack(anchor='w')
    self.pro = Label(sframe, text="Cliente>>");
    self.sendtext = Entry(sframe,width=80)
    self.sendtext.focus_set()
    self.sendtext.bind(sequence="<Return>", func=self.Send)
    self.pro.pack(side=LEFT)
    self.sendtext.pack(side=LEFT)
  def Send(self, args):
    self.gettext.configure(state='normal')
    text = self.sendtext.get()
    if text=="": text=" "
    #self.gettext.insert(END,'Servidor >> {} \n'.format(text))
    self.gettext.insert(END,'Cliente  >> {} \n'.format(text))
    self.sendtext.delete(0,END)
    self.client.send(str.encode(text))
    self.sendtext.focus_set()
    self.gettext.configure(state='disabled')
    self.gettext.see(END)
  def run(self):
    Receive(self.client, self.gettext)
root = Tk()
root.title('Chat del Cliente')
root.option_add("*Font", "Fixedsys 12")
app = App(root).start()
root.mainloop()
