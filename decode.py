import os
import subprocess
from Tkinter import Tk

#decode the text
def decode(word):
	word=list(word)
	for i in range(len(word)):
		t=ord(word[i])
		if t>83:
			t+=10
		if t<80:
			t-=5

		word[i]=str(unichr(t))
	st=''.join(word)
	return st
r = Tk()
r.withdraw()
t=r.clipboard_get()
x=decode(t)
r.clipboard_clear()
r.clipboard_append(x)
#clear the clipboard after 5 seconds
r.after(5000,r.destroy)
r.mainloop()
