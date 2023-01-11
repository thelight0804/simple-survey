"""
Date:
  23.01.09
author:
  @thelight0804 (PARK SANGHYEON)
"""
import os
import printSurvey, voteSurvey, managementSurvey

# Google firebase Realtime Database URL
url = 'https://API'

# input number
while(True):
  print("===========[[アンケート]]===========")
  print("@PARK SANGHYEON @72270002")
  print("------------------------------------")
  print("* 1. アンケート一覧の表示")
  print("* 2. アンケートへの回答投稿")
  print("* 3. アンケート回答の一覧表示")
  print("* 4. アンケート管理")
  print("* 5. プログラム終了")
  print("------------------------------------")

  print("番号を入力してください。")
  print("番号 : ", end="")
  num = int(input())

  if(num == 1): #アンケート一覧の表示
    os.system('cls') #clear screen
    printSurvey.printVote(url)

  elif(num == 2): #アンケートへの回答投稿
    os.system('cls') #clear screen
    res, num = voteSurvey.selectSurvey(url)
    if (num == -1): #error
      print("サーバーとのエラーが発生しました。")
    else:
      os.system('cls') #clear screen
      voteData = voteSurvey.vote(res, num)
      voteSurvey.postVoid(url, num, voteData)
  elif(num == 3): # アンケート回答の一覧表示
    os.system('cls') #clear screen
    res, num = voteSurvey.selectSurvey(url)
    if (num == -1): #error
      print("サーバーとのエラーが発生しました。")
    else:
      os.system('cls') #clear screen
      printSurvey.printResult(res, num)
  elif(num == 4):
      os.system('cls') #clear screen
      managementSurvey.management(url)
  elif(num == 5): # プログラム終了
    break
  else:
    print("1から5の番号を入力してください。")
  os.system("pause") #Press any key to continue
  os.system('cls') #clear screen

print("プログラムが終了しました。")