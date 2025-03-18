from m_src import decoder_m
from m_src import encoder_m
import setting
import os
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox

if os.path.isfile("setting.txt") != True:
    setting.write_file("./setting.txt","en")
Lnag=setting.read_file("./setting.txt")

en = ["caveat","Enter a valid value","Browse Files","Enter the file name to be output.","Enter the image file name to be written.",
"Enter the name of the image file to be output.","Decision","Top Choice","seting","close","save","Please enter a valid file path.",
" Only the [png] extension can be used for the output.","Loading","Loading complete:"
,"↑Warning: A file with the same name as the output file already exists. ↑\nPlease enter a new name or click the OK button again without entering a name.",
"Save complete:","Warning: A file with the same name as the output image already exists. \nChange the name or click the OK button again if you wish.",
"Writing","Writing complete\n","Please enter valid values ​​for all fields。",
"\nOnly the [png,jpg,jpeg] extension can be used for the input.","\nOnly the [png] extension can be used for the output."
,"Enter the file name to embed","Enter the file name to be output.","Enter the image file name to be written.",
"Enter the name of the image file to be output.","Enter the file name to be loaded"
,"decode mode","encode mode","Enter a valid value","decode","encode","Select Mode","Language"]

jp = ["注意","有効な値を入力","ファイルを参照","出力するファイル名を入力してください。","書き込む画像ファイル名を入力してください。",
"出力する画像ファイルの名前を入力してください。","決定","再選択","設定","閉じる","保存","有効なファイル パスを入力してください。",
"出力には [png] 拡張子のみ使用できます","読み込み中","読み込み完了:"
,"↑警告: 出力ファイルと同じ名前のファイルが既に存在します。↑\n新しい名前を入力する、もしくは何もを入力せずに [OK] ボタンをもう一度クリックしてください。",
"保存完了:","警告: 出力画像と同じ名前のファイルが既に存在します。\n必要に応じて名前を変更するか、[OK] ボタンをもう一度クリックしてください。",
"書き込み中","書き込み完了\n","すべての項目に有効な値を入力してください。","\n入力には [png、jpg、jpeg] 拡張子のみ使用できます。",
"\n出力には[png] 拡張子のみ使用できます。","埋め込むファイル名を入力してください","出力する際のファイル名を入力してください","書き込む画像ファイル名を入力してください"
,"出力する画像ファイルの名前を入力してください","読み込むファイル名を入力してください","デコードモード","エンコードモード","有効な値を入力","デコード","エンコード","モードを選択","言語"]

if Lnag == "jp":
   langs = jp
else:
    langs = en
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

cnb = tk.Label(root,text = langs[0])
cnbin = tk.Entry(width=40)
conbasd = tk.Label(text = "")
cmt = tk.Label(root,text = langs[1])
BT = tk.Button(root, text=langs[2],command=lambda:openfile("D",1))
BT1 = tk.Button(root, text=langs[2],command=lambda:openfile("D",1))
text5 = tk.Label(root,text = "")
text1 = tk.Label(root,text = langs[3])
EditBox = tk.Entry(width=40)
text2 = tk.Label(root,text = langs[4])
EditBox2 = tk.Entry(width=40)
text3 = tk.Label(root,text = langs[5])
EditBox3 = tk.Entry(width=40)
text4 = tk.Label(root,text = langs[6])
EditBox4 = tk.Entry(width=40)
submit_button = tk.Button(root, text=langs[6],command=lambda:encode(EditBox.get(),EditBox2.get(),EditBox3.get(),EditBox4.get()))
re_boutton = tk.Button(root, text=langs[7],command=lambda:re_serect())
OpenSeting = tk.Button(root, text=langs[8],command=lambda:open_settings())

# グローバル変数で設定を保存する
settings = {}
def open_settings():
    global settings
    Sver = tk.StringVar(value="en")
    # 設定画面をすでに開いているかどうかを調べる
    if settings.get('window'):
        return
    
    # 設定画面を生成する
    window = tk.Toplevel(root)
    window.geometry("250x250")
    window.title(u"Image_information_embedder")
    iconfile = 'testImage/Image_information_embedder(Icon).ico'
    window.iconbitmap(default=iconfile)
    # 設定画面を閉じる処理
    def close_abd_save_settings():
        window.destroy()
        settings['name'] = Sver.get()
        setting.write_file("setting.txt",Sver.get())
        settings['window'] = None
        
    def close_settings():
        window.destroy()
        settings['window'] = None
    window.protocol("WM_DELETE_WINDOW", close_settings)
    label = tk.Label(window,text = langs[34])
    label.pack()
    Len = tk.Radiobutton(window, text="english", variable=Sver, value="en")
    Len.pack()
    Ljp = tk.Radiobutton(window, text="japanese", variable=Sver, value="jp")
    Ljp.pack()
    
    # 閉じるボタンを作成する
    close_button = tk.Button(window, text=langs[9], command=close_settings)
    close_button.pack(side = tk.BOTTOM)
    
    # セーブボタンを作成する
    save_button = tk.Button(window, text=langs[10], command=close_abd_save_settings)
    save_button.pack(side = tk.BOTTOM)

    # 設定画面を保存する
    settings['window'] = window
    
def reverse_and_sort_for(text):
  """forループを使ってテキストを後ろから読み込み、"."が現れるまで文字を格納し、並べ替えて返す"""
  """Use a for loop to read the text backwards, store the characters until a "." is encountered, sort them, and return them"""
  reversed_text = ""
  for char in reversed(text):
    if char == ".":
      break
    reversed_text += char
  sorted_text = "".join(reversed(reversed_text))
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
        messagebox.showerror("error", langs[11])
    elif reverse_and_sort_for(filename) != "png":
        messagebox.showerror("error", langs[12])
    else:
     global root
     global text5
     text5["text"] = langs[13]
     text5.pack()
     filepas = tempFilename
     decodet = tempDecodet
     if DH2 == False:
         decodet,filepas = decoder_m.rood_image_bytes(filename)
         text5["text"] = langs[14]+filepas
         tempFilename = filepas
         tempDecodet = decodet
     if os.path.isfile(filepas) == True and DH2 == False:
         cnb["text"] = langs[15]
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
       text5["text"] = langs[16]+filepas
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
    fomat = ["png","jpg","jpeg"]
    
    CCC = 0
    
    for i in range(3):
            if(reverse_and_sort_for(inImage) != fomat[i -1]):
                CCC += 1
    #print(reverse_and_sort_for(inImage) )
    if(os.path.isfile(seve) == True and os.path.isfile(inImage) == True and output != "" and reverse_and_sort_for(outImage) == fomat[0] and CCC < 3):
     if os.path.isfile(outImage) == True and H2 == False:
         H1 = True
         cnb["text"] = langs[17]
         cnb.pack(side=tk.BOTTOM)
         H2 = True
     if(H1 == False):
      H2 = False
      text5["text"] = langs[18]
      with open(seve, 'br') as f:
       data = f.read()
    
      caveat = encoder_m.write_image_bytes(data,output,inImage,outImage)#同時に警告を代入:Simultaneously assign warning
      text5["text"] = langs[19]+caveat
      cnb.pack_forget()
     else:
         H1 = False
    else:
        text =langs[20]
        if(CCC == 3):
            text += langs[21]
        if(reverse_and_sort_for(outImage) != fomat[0]):
            text += langs[22]
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
    
    text1 = tk.Label(text = langs[23])
    text1.pack()
    EditBox = tk.Entry(width=40)
    EditBox.insert(tk.END,"")
    EditBox.pack()
    BT.pack()
    
   
    text2 = tk.Label(text = langs[24])
    text2.pack()
    EditBox2 = tk.Entry(width=40)
    EditBox2.insert(tk.END,"")
    EditBox2.pack()
    
    text3 = tk.Label(text = langs[25])
    text3.pack()
    EditBox3 = tk.Entry(width=40)
    EditBox3.insert(tk.END,"")
    EditBox3.pack()
    BT1.pack()
    
    text4 = tk.Label(text = langs[26])
    text4.pack()
    EditBox4 = tk.Entry(width=40)
    EditBox4.insert(tk.END,"")
    EditBox4.pack()
    
    submit_button = tk.Button(root, text=langs[6],command=lambda:encode(EditBox.get(),EditBox2.get(),EditBox3.get(),EditBox4.get()))
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
    text1 = tk.Label(text = langs[27])
    text1.pack()
    EditBox = tk.Entry(width=40)
    EditBox.insert(tk.END,"")
    EditBox.pack()
    BT = tk.Button(root, text=langs[2],command=lambda:openfile("D",1))
    BT.pack()
    submit_button = tk.Button(root, text=langs[6],command=lambda:decode(EditBox.get()))
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
        cmttext = langs[28]
        H = True
        cmt.config(text = cmttext)
        cmt.pack()
        decode_INPUT()
     elif var.get() =="en":
        cmttext = langs[29]
        H = True
        cmt.config(text = cmttext)
        cmt.pack()
        encodeINPUT()
     else:
         cmttext=langs[30]
         cmt.config(text = cmttext)
         cmt.pack()
     

#初期UIを描画する
#Draw the initial UI
OpenSeting.pack(anchor = tk.NW)
radiobutton1 = tk.Radiobutton(root, text=langs[31], variable=var, value="de")
radiobutton2 = tk.Radiobutton(root, text=langs[32], variable=var, value="en")

lbl = tk.Label(root,text = langs[33])
lbl.pack()
radiobutton1.pack()
radiobutton2.pack()
submit_button = tk.Button(root, text=langs[6], command=Enter_encode_or_edcode)
submit_button.pack()
cmt.pack()
tk.mainloop()