import csv
import pyperclip

#CSVのファイル名は任意のものに変えてください。今はsample.csvにしています。
f = open("sample.csv", "r")
lst = list(csv.reader(f))
bl = True #無限ループ終了フラグ
input_count = 0 #重複する値をカウント
swap_address = [] #重複する値を格納する配列

while bl:
    x = input("input name：")
    for row in range(len(lst)):
        #csvの1列目でヒットする値を探し、配列を作ります。
        if x in lst[row][0]:
            swap_address.append(row)

            #print (lst[row][0],":",lst[row][1])
            #pyperclip.copy(lst[row][1])
        elif x == "exit":
            bl = False #exitが打ち込まれると処理終了（無限ループから抜ける）

    for row2 in range(len(lst)):
        #csvの2列目でヒットする値を探し、配列を作ります。
        if x in lst[row2][1]:
            swap_address.append(row2)
    
    #終了処理をした時
    if bl == False:
        print("terminated")
    #検索がヒットしない時
    elif len(swap_address) == 0:
        print ("not found")
    #検索が1件だけの時
    elif len(swap_address) == 1:
            print (lst[swap_address[0]][0]," Clip to ",lst[swap_address[0]][2])
            pyperclip.copy(lst[swap_address[0]][2])
    #検索が複数件の時。（作った配列(swap_address)を候補として表示。）
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

    #swap_addressを初期化
    swap_address = []
