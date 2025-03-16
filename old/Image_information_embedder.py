from m_src import decoder_m
from m_src import encoder_m
import os


def Enter(text="",mode=""):
    while True:
        inputtext= input(text)
        if(mode == "A"):
            if(os.path.isfile(inputtext)):
                break
            else:
                print("caveat[2]!There is no file path to specify. Please re-enter")
        if(mode == "B"):
            if(os.path.isfile(inputtext)):
                print("caveat[3]!A file with the same name already exists. If you leave it as is, it will be overwritten when decoding and outputting. ")
                Input = input("Are you sure? Yes or No:1 or other input:")
                if Input == "1":
                    break
            else:
                break
    return inputtext
#モードを聞く
#Listen to the mode
mode = input("Enter mode:encode or decode:0 or 1:")
if(mode == "0"):
  #Encode mode
  print("mode:encode")
 
  #必要情報を取得(格納するファイルのパス、デコードした際のファイル名、書き込む画像パス、出力する画像パス)
  #Get required information (path of file to store, file name when decoded, image path to write, image path to output)
  while True:
     S = Enter("Enter the file path to store:","A")
     
     O = Enter("Enter the file path to output:","B")
     
     A = Enter("Enter the path of the image to be written:","A")
     
     B = Enter("Enter the file path to output:","B")
     print(S)
     print(O)
     print(A)
     print(B)
     confirmation = input("Is the above content correct?:No or Yes:1 or Other input:")
     if confirmation != "1":
         break

  #格納するファイルのバイナリを取得
  #Get the binary of the file to be stored
  with open(S, 'br') as f:
   data = f.read()

  #ファイルを格納する
  #Store the file
  caveat = encoder_m.write_image_bytes(data,O,A,B)#同時に警告を代入:Simultaneously assign warning
  #警告があるか判断
  # Determine if there is a warning
  if(caveat == ""):
      #警告がない場合
      #If there are no warnings
      print("Write successful")
  else:
      #警告がある場合
      #If there is a warning
      print(caveat)


elif(mode == "1"):
     #If decode mode
     print("mode:decode")

     #読み込む画像のパスを取得
     #Get the path of the image to be loaded
     while True:
        A=Enter("Enter the path of the image you want to load:","A")
        print(A)
        confirmation = input("Is the above content correct?:No or Yes:1 or Other input:")
        if confirmation != "1":
           break

     #バイナリ情報とファイル名を画像から読み出し
     #Read binary information and filename from image
     decodet,filepas = decoder_m.rood_image_bytes(A)

     while True:
         if(os.path.isfile(filepas)):
                print(filepas)
                print("A file with the same name already exists. If you leave it as is, it will be overwritten when decoding and outputting. ")
                Input = input("Are you sure? Yes or No:1 or other input:")
                if Input == "1":
                    break
         else:
                break
     #ファイル名を出力
     #Output file name
     print("Loading successful Output:" + filepas)

     #読み込んだファイル名とバイナリでファイルを生成
     #Create a file with the loaded file name and binary
     fw = open(filepas, 'wb')
     fw.write(bytes(decodet))
     fw.close()

RCS = input ("Exsit?:Any Key")
