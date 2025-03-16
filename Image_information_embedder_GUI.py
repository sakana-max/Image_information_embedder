from m_src import decoder_m
from m_src import encoder_m
import os
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox

#UIを用意したりする
#Prepare the UI

openfile_path = ""
root = tk.Tk()
root.geometry("500x550")
root.title(u"Image_information_embedder")
iconfile = 'testImage/Image_information_embedder(Icon).ico'
root.iconbitmap(default=iconfile)
var = tk.StringVar(value="")
H = False

cnb = tk.Label(root,text = "caveat")
cnbin = tk.Entry(width=40)
conbasd = tk.Label(text = "")
cmt = tk.Label(root,text = "Enter a valid value")
BT = tk.Button(root, text="Browse Files",command=lambda:openfile("D",1))
BT1 = tk.Button(root, text="Browse Files",command=lambda:openfile("D",1))
text5 = tk.Label(root,text = "")
text1 = tk.Label(root,text = "Enter the file name to embed")
EditBox = tk.Entry(width=40)
text2 = tk.Label(root,text = "Enter the file name to be output.")
EditBox2 = tk.Entry(width=40)
text3 = tk.Label(root,text = "Enter the image file name to be written.")
EditBox3 = tk.Entry(width=40)
text4 = tk.Label(root,text = "Enter the name of the image file to be output.")
EditBox4 = tk.Entry(width=40)
submit_button = tk.Button(root, text="Decision",command=lambda:encode(EditBox.get(),EditBox2.get(),EditBox3.get(),EditBox4.get()))
re_boutton = tk.Button(root, text="Top Choice",command=lambda:re_serect())

def reverse_and_sort_for(text):
  """forループを使ってテキストを後ろから読み込み、"."が現れるまで文字を格納し、並べ替えて返す"""
  """Use a for loop to read the text backwards, store the characters until a "." is encountered, sort them, and return them"""
  reversed_text = ""
  for char in reversed(text):
    if char == ".":
      break
    reversed_text += char

  sorted_text = "".join(sorted(reversed_text))
  return sorted_text

def openfile(A = "", B = 0):
    #ファイルを開いて返す
    #Open the file and return
    global EditBox
    global EditBox2
    global EditBox3
    global EditBox4
    fpath = fd.askopenfilename()
    global openfile_path
    if fpath:
        openfile_path = fpath
        if A == "D":
         if B == 1:
            EditBox.delete(0, tk.END)  
            EditBox.insert(tk.END,openfile_path)
        elif A == "E":
         if B == 1:
            EditBox.delete(0, tk.END)  
            EditBox.insert(tk.END,openfile_path)
         if B == 2:
            EditBox3.delete(0, tk.END)  
            EditBox3.insert(tk.END,openfile_path)
def re_serect():
    #UIを初期化
    #Initialize UI
    global cnb
    global BT
    global BT1
    global cmt
    global text5
    global re_boutton
    global text1
    global EditBox
    global text2
    global EditBox2
    global text3
    global EditBox3
    global text4
    global EditBox4
    global submit_button
    global H
    global DH1
    global DH2
    global H1
    global H2
    text1.pack_forget()
    EditBox.pack_forget()
    text2.pack_forget()
    EditBox2.pack_forget()
    text3.pack_forget()
    EditBox3.pack_forget()
    text4.pack_forget()
    EditBox4.pack_forget()
    submit_button.pack_forget()
    text4.pack_forget()
    text5.pack_forget()
    re_boutton.pack_forget()
    submit_button.pack_forget()
    cmt.pack_forget()
    BT.pack_forget()
    BT1.pack_forget()
    conbasd.pack_forget()
    cnb.pack_forget()
    cnbin.pack_forget()
    H = False
    H1 = False
    H2 = False
    DH1 = False
    DH2 = False
   
DH1 = False
DH2 = False
tempFilename = ""
tempDecodet = []
def decode(filename):
    #入力された情報でデコードする。
    # Decode with the entered information.
    global DH1
    global DH2
    global tempFilename
    global tempDecodet
   
    decoder_m.relaed()
    if(os.path.isfile(filename) == False):
        messagebox.showerror("error", "Please enter a valid file path.")
    elif reverse_and_sort_for(filename) != "gnp":
        messagebox.showerror("error", " Only the [png] extension can be used for the output.")
    else:
     global root
     global text5
     text5["text"] = "Loading"
     text5.pack()
     filepas = tempFilename
     decodet = tempDecodet
     if DH2 == False:
         decodet,filepas = decoder_m.rood_image_bytes(filename)
         text5["text"] = "Loading complete:"+filepas
         tempFilename = filepas
         tempDecodet = decodet
     if os.path.isfile(filepas) == True and DH2 == False:
         cnb["text"] = "↑Warning: A file with the same name as the output file already exists. ↑\nPlease enter a new name or click the OK button again without entering a name."
         cnb.pack(side=tk.BOTTOM)
         DH1 = True
         cnbin.pack(side=tk.BOTTOM)
     if DH1 == False:
       #読み込んだファイル名とバイナリでファイルを生成
       #Create a file with the loaded file name and binary\
       if cnbin.get() != "" and DH2 == True:
           filepas = cnbin.get()
       fw = open(filepas, 'wb')
       fw.write(bytes(decodet))
       fw.close()
       cnb.pack_forget()
       DH1 = False
       DH2 = False
       cnbin.pack_forget()
       text5["text"] = "Save complete:"+filepas
     else:
         DH1 = False
         DH2 = True
  
H1 = False
H2 = False
def encode(seve,output,inImage,outImage):
    #入力された情報でエンコードする。
    #Encode with the entered information.
    caveat = ""
    global H1
    global H2
    global root
    global text5
    fomat = ["gnp","gpj","gepj"]
    if(os.path.isfile(seve) == True and os.path.isfile(inImage) == True and output != "" and reverse_and_sort_for(inImage) == fomat[0] or reverse_and_sort_for(inImage) == fomat[1] or reverse_and_sort_for(inImage) == fomat[2]):
     if os.path.isfile(outImage) == True and H2 == False:
         H1 = True
         cnb["text"] = "Warning: A file with the same name as the output image already exists. \nChange the name or click the OK button again if you wish."
         cnb.pack(side=tk.BOTTOM)
         H2 = True
     if(H1 == False):
      H2 = False
      text5["text"] = "Writing"
      with open(seve, 'br') as f:
       data = f.read()
    
      caveat = encoder_m.write_image_bytes(data,output,inImage,outImage)#同時に警告を代入:Simultaneously assign warning
      text5["text"] = "Writing complete\n"+caveat
      cnb.pack_forget()
     else:
         H1 = False
    else:
        text ="Please enter valid values ​​for all fields。"
        if(reverse_and_sort_for(inImage) != fomat[0] or reverse_and_sort_for(inImage) != fomat[1] or reverse_and_sort_for(inImage) != fomat[2]):
            text += "\nOnly the [png,jpg,jpeg] extension can be used for the input."
        if(reverse_and_sort_for(outImage) != fomat[0]):
            text += "\nOnly the [png] extension can be used for the output."
        messagebox.showerror("error", text)
    
def encodeINPUT():
    #エンコードに必要な情報を取得する
    #Get the information required for encoding
    global root
    global H
    global text5
    global text1
    global EditBox
    global text2
    global EditBox2
    global text3
    global EditBox3
    global text4
    global EditBox4
    global submit_button
    global BT
    global BT1
    
    BT.config(command=lambda:openfile("D",1))
    BT1.config(command=lambda:openfile("E",2))
    
    text1 = tk.Label(text = "Enter the file name to embed")
    text1.pack()
    EditBox = tk.Entry(width=40)
    EditBox.insert(tk.END,"")
    EditBox.pack()
    BT.pack()
    
   
    text2 = tk.Label(text = "Enter the file name to be output.")
    text2.pack()
    EditBox2 = tk.Entry(width=40)
    EditBox2.insert(tk.END,"")
    EditBox2.pack()
    
    text3 = tk.Label(text = "Enter the image file name to be written.")
    text3.pack()
    EditBox3 = tk.Entry(width=40)
    EditBox3.insert(tk.END,"")
    EditBox3.pack()
    BT1.pack()
    
    text4 = tk.Label(text = "Enter the name of the image file to be output.")
    text4.pack()
    EditBox4 = tk.Entry(width=40)
    EditBox4.insert(tk.END,"")
    EditBox4.pack()
    
    submit_button = tk.Button(root, text="Decision",command=lambda:encode(EditBox.get(),EditBox2.get(),EditBox3.get(),EditBox4.get()))
    submit_button.pack()
    lbl.pack()
    
    text5.pack()
    re_boutton.pack()
def decode_INPUT():
    #デコードに必要な情報を取得する
    #Get the information needed to decode
    global openfile_path
    global root
    global H
    global text5
    global text1
    global EditBox
    global submit_button
    global BT
    text1 = tk.Label(text = "Enter the file name to be loaded")
    text1.pack()
    EditBox = tk.Entry(width=40)
    EditBox.insert(tk.END,"")
    EditBox.pack()
    BT = tk.Button(root, text="Browse Files",command=lambda:openfile("D",1))
    BT.pack()
    submit_button = tk.Button(root, text="Decision",command=lambda:decode(EditBox.get()))
    submit_button.pack()
    text5.pack()
    re_boutton.pack()
def Enter_encode_or_edcode():
    #モードを判定する
    # Determine the mode
    global var
    global root
    global H
    global cmt
    cmttext =""
    
    if H == False:
     if(var.get() == "de"):
        cmttext = "decode mode"
        H = True
        cmt.config(text = cmttext)
        decode_INPUT()
     elif var.get() =="en":
        cmttext = "encode mode"
        H = True
        cmt.config(text = cmttext)
        encodeINPUT()
     else:
         cmttext="Enter a valid value"
         cmt.config(text = cmttext) 
     cmt.pack()

#初期UIを描画する
#Draw the initial UI

radiobutton1 = tk.Radiobutton(root, text="decode", variable=var, value="de")
radiobutton2 = tk.Radiobutton(root, text="encode", variable=var, value="en")

lbl = tk.Label(root,text = "Select Mode")
lbl.pack()
radiobutton1.pack()
radiobutton2.pack()
submit_button = tk.Button(root, text="Decision", command=Enter_encode_or_edcode)
submit_button.pack()
cmt.pack()
tk.mainloop()