import csv
import pyperclip

#ファイル名は任意のものに変えてください。
f = open("{任意のCSVファイル名}.csv", "r")
lst = list(csv.reader(f))
bl = True #無限ループ終了フラグ
input_count = 0 #重複する値をカウント
swap_address = [] #重複する値を格納する配列

while bl:
    x = input("input name：")
    for row in range(len(lst)):
        if x in lst[row][0]:
            swap_address.append(row)

            #print (lst[row][0],":",lst[row][1])
            #pyperclip.copy(lst[row][1])
        elif x == "exit":
            bl = False #exitが打ち込まれると処理終了

    for row2 in range(len(lst)):
        if x in lst[row2][1]:
            swap_address.append(row2)
    
    if bl == False:
        print("terminated")
    elif len(swap_address) == 0:
        print ("not found")
    elif len(swap_address) == 1:
            print (lst[swap_address[0]][0]," Clip to ",lst[swap_address[0]][2])
            pyperclip.copy(lst[swap_address[0]][2])
    elif len(swap_address) >= 2:
            print(len(swap_address),"hit:")
            for row in range(len(swap_address)):    
                print(" ",row,":",lst[swap_address[row]][0]," ",lst[swap_address[row]][2])
            x2 = input("who choice?:")
            x2 = int(x2)
            if x2 > len(swap_address) -1:
                print("value is over")
            else:
                print(lst[swap_address[x2]][0]," Clip to ",lst[swap_address[x2]][2])
                pyperclip.copy(lst[swap_address[x2]][2])

    swap_address = []
