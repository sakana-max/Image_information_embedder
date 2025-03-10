from PIL import Image
import locale
import sys
sys.setrecursionlimit(10000)

def Imageencerd(bits = [],image_name="",out_name=""):
 #区切られたビット情報を画像に書きむプログラム
 #Program to write separated bit information to an image

 #書き込む画像情報を取得
 #Get image information to write
 im = Image.open(image_name)
 rgb_im = im.convert('RGB')
 size = rgb_im.size

 #書き込むビット情報の長さを取得
 #Get the length of the bit information to write
 Maximum = len(bits)

 count =0
 caveat = ""
 for x in range(size[0]):
    for y in range(size[1]):

        #画像の色を取得
        #Get image color
        r0,g0,b0 = rgb_im.getpixel((x,y))

        #書き込み終わってなかったらビット情報を書き込み
        #If writing is not complete, write the bit information
        if Maximum > count:
         if bits[count] == 0:
          #ビット情報が0なら
          #If bit information is 0
          if (r0 % 2) != 0:
            #奇数のとき色を偶数に変更
            #Change color to even when number is odd
            if (r0+1) > 255:
             r0-=1
            else:
             r0+=1
         #ビット情報が1なら
         #If bit information is 1
         else:
          if (r0 % 2) == 0:
            #偶数のとき色を奇数に変更
            #Change color to odd when number is even
            if (r0-1) < 0:
                r0+=1
            else:
             r0-=1
        count +=1
        #上と同じ
        #Same as above
        if Maximum > count:
         if bits[count] == 0:
          if (g0 % 2) != 0:
            if (g0+1) > 255:
             g0-=1
            else:
             g0+=1
         else:
          if (g0 % 2) == 0:
            if (g0-1) < 0:
                g0+=1
            else:
             g0-=1
        count +=1
        #上と同じ
        #Same as above
        if Maximum > count:
         if bits[count] == 0:
          if (b0 % 2) != 0:
            if (b0+1) > 255:
             b0-=1
            else:
             b0+=1
         else:
          if (b0 % 2) == 0:
            if (b0-1) < 0:
                b0+=1
            else:
             b0-=1
        count +=1

        #色を決定
        #Decide on color
        im.putpixel((x,y),(r0,g0,b0,0))

        #すべて書き込んだらループから抜ける
        # Once everything is written, exit the loop
        if Maximum <= count:
          break

    #すべて書き込んだらループから抜ける
    # Once everything is written, exit the loop
    if Maximum <= count:
          break

 #書き込み
 #write
 im.save(out_name)
 if Maximum >= count:
     #Warning when all files could not be written
     caveat = "caveat[1]!File writing was interrupted. There is no space to embed. The embedded file is corrupted or only partially filled.\nWriteable file size: Approx."+(str(size[0] * size[1]*3/8))+"byt"
 return caveat#警告を返す。ない場合は""を返す:Returns a warning, or "" if none

def write_image_bytes(byt =[],filename="",image_path="",out_path=""):
    #ファイルのバイト情報を区切られたビット情報に変換し、書き込まれた情報の長さと、出力されるファイル名を格納するプログラム
    #A program that converts the byte information of a file into delimited bit information and stores the length of the written information and the output file name.
   
    blist =[]
    for byte in byt:
        #バイト情報を区切られたビット情報に変換
        #Convert byte information into separated bit information
        for i in range(8):
            bit = (byte >> (7 - i)) & 1
            blist.append(bit)
    File_information = []

    bytlen = len(blist)#書き込むバイトの長さを代入#Assign length of bytes to write

    bytlen += 32#書き込むバイトの長さに32（書き込まれた情報の長さ自体を書き込むbit数）を足す# Add 32 (the number of bits to write the length of the written information itself) to the length of the bytes to be written
    
    #区切られたビット情報をint型に変換
    #Convert separated bit information to int type
    for xx in blist:
            File_information.append(int(xx))
    
    Write_Length = ""
    Advanced_Information = []
    s = filename
    
    #ファイル名をビット情報に変換に変換↓#Convert file name to bit information↓
    binary_string = ''.join(format(ord(c), '016b') for c in s)
    int_array = [int(c) for c in binary_string]
    binary_string = format(ord("\0"), '016b')  # ヌル文字を8ビットの2進数文字列に変換
    binary_array = [int(bit) for bit in binary_string]
    #ファイル名をビット情報に変換↑#Convert file name to bit information↑

    #ファイル名分の長さを格納
    #Store the length of the file name
    bytlen += len(int_array)
    bytlen += len(binary_array)
   
    #書き込むファイルの長さをビット情報に変換
    #Convert the length of the file to be written into bit information
    Write_Length = str(format(bytlen, '032b'))

    #区切られたビット情報をint型に変換
    #Convert separated bit information to int type
    for a_text in Write_Length:
        Advanced_Information.append(int(float(a_text)))
    
    #ビット情報を一つにまとめる
    #Combine bit information into one
    int_array = int_array + binary_array
    Advanced_Information.extend(int_array)
    Advanced_Information.extend(File_information)
    
    #ビット情報を書き込み
    #Write bit information
    return Imageencerd(Advanced_Information,image_path,out_path)#警告を返す。ない場合は""を返す:Returns a warning, or "" if none
