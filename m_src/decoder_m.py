from PIL import Image
import locale
import sys
sys.setrecursionlimit(10000)

def rood_image_system(inpas):
 #画像をロードして情報を返す
 #Load the image and return the information

 im = Image.open(inpas)
 rgb_im = im.convert('RGB')
 size = rgb_im.size
 return size,rgb_im

lists = []
nn = 0
xx= 0
byt = True

def relaed():
    global lists
    global nn
    global xx
    lists = []
    nn = 0
    xx= 0
    byt = True

def setbyt(a):
 #ビット列からバイト列を取り出すプログラム
 #Program to extract byte string from bit string

 
 global lists
 global nn
 global xx
 hann = False
 
  
 #ビット情報をバイト情報にまとめる
 #Combine bit information into byte information

 if nn == 0:
    #8つ読み込んだら配列に新しい項目を作って書き込み
    #After reading 8, create a new item in the array and write it
    lists.append(str(a))
 else :
  #新しい項目を作らないで書き込み
  #Write without creating a new item
  lists[xx]+=str(a)

 #何ビット書き込んだか保存
 #Save how many bits were written
 nn += 1

 if(nn>=8):
     #8ビット書き込んだら次のバイトに移るように示す
     #Indicate to move to the next byte after writing 8 bits
     nn = 0
     xx +=1

def rood_image_bytes(pas):
 #画像からビット情報を読み込むプログラム
 #Program to read bit information from an image

 K = 0
 stopbit = ""
 global byt
 byt = False
 orStop = False

 #画像情報を取得
 #Get image information
 size1,rgb_im1 = rood_image_system(pas)

 for x in range(size1[0]):
     for y in range(size1[1]):

        #32ビット取り出したら一回限りで書き込んだ長さを取得する
        #Once you have extracted 32 bits, get the length written in one go
        if(K > 32 and orStop == False):
           orStop = True
           for i in range(4):
               #4バイト取り出す
               #Extract 4 bytes
               stopbit += str(lists[i])

        #色情報を取得
        #Get color information
        r0,g0,b0 = rgb_im1.getpixel((x,y))
        hhhe = False

        #読み込んだ色情報が偶数なら0を記録奇数なら1を記録　全部読み込んだらループから抜ける
        # If the color information read is even, record 0. If it is odd, record 1. Once all the color information is read, exit the loop.
        if (r0 % 2) == 0:
          setbyt(0)
          if orStop == True and int(stopbit,2)<= K:
            break
        else :
          setbyt(1)
          if orStop == True and int(stopbit,2)<= K:
            break
        K += 1
        #読み込んだ色情報が偶数なら0を記録奇数なら1を記録　全部読み込んだらループから抜ける
        # If the color information read is even, record 0. If it is odd, record 1. Once all the color information is read, exit the loop.
        if (g0 % 2) == 0:
          setbyt(0)
          if orStop == True and int(stopbit,2)<= K:
            break
        else :
          setbyt(1)
          if orStop == True and int(stopbit,2)<= K:
            break
        K += 1
        #読み込んだ色情報が偶数なら0を記録奇数なら1を記録　全部読み込んだらループから抜ける
        # If the color information read is even, record 0. If it is odd, record 1. Once all the color information is read, exit the loop.
        if (b0 % 2) == 0:
          setbyt(0)
          if orStop == True and int(stopbit,2)< K:
            break
        else :
          setbyt(1)
          if orStop == True and int(stopbit,2)<= K:
            break
        K += 1

     #全部読み込んだらループから抜ける
     # Once everything is loaded, exit the loop
     if orStop == True and int(stopbit,2) <= K:
            break
 
 #ビット情報をバイナリとファイル名に加工
 #Process bits into binary and filename
 L=""
 lists1 =[]
 kaka =0
 
 #テキスト情報のバイト列をint配列に区切る
 #Split the byte sequence of text information into an int array
 for nnn in lists:
   kaka = int(nnn,2)
   lists1.append(kaka)
 pas = []
 num = 0
 byts2 = ""

 #先端4バイトから下のファイル名を読み込む
 # Read the file name below from the first 4 bytes
 while num < 100:
    
    #先端4バイト以降を二つずつ連結する
    #Concatenate the first 4 bytes and onwards in pairs
    byts2 = str(lists[num+4]) + str(lists[num+5])

    if byts2== format(0, '016b'):
         #ヌル文字が含まれているなら読み込み終了
         #先端のバイナリ情報ではないバイトの数(4)と今回ループ分の2を足す
         #If null characters are included, stop reading
         #Add the number of bytes that are not binary information at the beginning (4) and the number of bytes for this loop (2)
         num+=6
         break
    
    #16ビットのテキスト情報をリストに追加
    #Add 16-bit text information to the list
    pas.append(str(byts2))

    #先端のバイナリ情報ではないバイトの数を足す]
    #Add the number of bytes that are not binary information at the beginning
    num += 2
 pasT =""
 
 #各要素を文字列に変換
 #Convert each element to a string
 for text in pas:
    pasT += chr(int(text, 2))
    
 #先端のバイナリ情報ではないバイトを抜いたバイナリを返す
 #Returns binary with the leading non-binary bytes removed
 return lists1[num:],pasT
