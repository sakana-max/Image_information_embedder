from m_src import decoder_m
from m_src import encoder_m

#モードを聞く
#Listen to the mode
mode = input("Enter mode:encode or decode:0 or 1:")
if(mode == "0"):
  #Encode mode
  print("mode:encode")
 
  #必要情報を取得(格納するファイルのパス、デコードした際のファイル名、書き込む画像パス、出力する画像パス)
  #Get required information (path of file to store, file name when decoded, image path to write, image path to output)
  while True:
     S= input ("Enter the file path to store:")
     O= input ("Enter the file path to output:")
     A= input ("Enter the path of the image to be written:")
     B= input ("Enter the image file path to store:")
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
        A= input ("Enter the path of the image you want to load:")
        confirmation = input("Is the above content correct?:No or Yes:1 or Other input:")
        if confirmation != "1":
           break

     #バイナリ情報とファイル名を画像から読み出し
     #Read binary information and filename from image
     decodet,filepas = decoder_m.rood_image_bytes(A)

     #ファイル名を出力
     #Output file name
     print("Loading successful Output:" + filepas)

     #読み込んだファイル名とバイナリでファイルを生成
     #Create a file with the loaded file name and binary
     fw = open(filepas, 'wb')
     fw.write(bytes(decodet))
     fw.close()

RCS = input ("Exsit?:Any Key")
