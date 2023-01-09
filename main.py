"""
Date:
  23.01.09
author:
  @thelight0804
"""
import printSurvey, voteSurvey

# input number
while(True):
  print("------------[[アンケート]]------------\t@PARK SANGHYEON @72270002")
  print("* 1. アンケート一覧の表示")
  print("* 2. アンケートへの回答投稿")
  print("* 3. アンケート回答の一覧表示")
  print("* 4. プログラム終了")
  print("------------------------------------")

  print("番号を入力してください。")
  print("番号 : ", end="")
  num = int(input())

  if(num == 1): #설문 목록 출력
    printSurvey.printTest()
  elif(num == 2): #설문 투표
    voteSurvey.selectSurvey()
  elif(num == 3): # 답안 전체 출력
    print(num)
  elif(num == 4): #프로그램 종료
    break
  else:
    print("1から4の番号を入力してください。")

print("プログラムが終了しました。")