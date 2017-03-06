import os
import subprocess
from Tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
#hash the text
def encode(word):
	word=list(word)
	for i in range(len(word)):
		t=ord(word[i])
		if t>93:
			t-=10
		if t<75:
			t+=5

		word[i]=str(unichr(t))
	st=''.join(word)
	return st
word=raw_input()
t=encode(word)
#copy the encoded the texted to clipboard
r.clipboard_append(t)
r.after(5000, r.destroy)
r.mainloop()

