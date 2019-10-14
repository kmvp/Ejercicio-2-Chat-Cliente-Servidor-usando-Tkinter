from tkinter import *
import socket
from threading import *
from tkinter import ttk, font, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import Menu

root = Tk()
class Receive():
  def __init__(self, server, gettext):
###############################################################

###############################################################
    self.server = server
    self.gettext = gettext
    while 1:
      try:
        text = self.server.recv(1024)
        if not text: break
        self.gettext.configure(state=NORMAL)
        self.gettext.insert(END,'Cliente  >> %s\n'%text)
        self.gettext.configure(state=DISABLED)
        self.gettext.see(END)
      except:
        break
class App(Thread):
  server = socket.socket()
  server.bind(('localhost', 20001))
  server.listen(5)
  client,addr = server.accept()
  def __init__(self, master):
    Thread.__init__(self)
    frame = Frame(master)
    frame.pack()
    self.gettext = ScrolledText(frame, height=20,width=80, state=NORMAL)
    self.gettext.pack()
    sframe = Frame(frame)
    sframe.pack(anchor='w')
    self.pro = Label(sframe, text="Servidor>>");
    self.sendtext = Entry(sframe,width=80)
    self.sendtext.focus_set()
    self.sendtext.bind(sequence="<Return>", func=self.Send)
    self.pro.pack(side=LEFT)
    self.sendtext.pack(side=LEFT)
    self.gettext.insert(END,'Bienvenido al Chat Servidor\n\n')
    self.gettext.configure(state=DISABLED)
  def Send(self, args):
    self.gettext.configure(state=NORMAL)
    text = self.sendtext.get()
    if text=="": text=" "
    #self.gettext.insert(END,'Servidor >> {} \n'.format(text))
    self.gettext.insert(END,'Servidor >> {} \n'.format(text))
    self.sendtext.delete(0,END)
    self.client.send(str.encode(text))
    self.sendtext.focus_set()
    self.gettext.configure(state=DISABLED)
    self.gettext.see(END)
  def run(self):
    Receive(self.client, self.gettext)
#root = Tk()
root.title('Chat del Servidor')
root.option_add("*Font", "Fixedsys 12")
app = App(root).start()
root.mainloop()
