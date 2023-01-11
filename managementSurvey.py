import requests, os
import voteSurvey

def management(url):
  """アンケート管理画面

  Args:
      url (String): Google firebase Realtime Database URL
  """
  print("===========[アンケート管理]===========")
  while(True):
    print("* 1. アンケート登録")
    print("* 2. アンケート削除")
    print("* 3. メインメニューへ戻る")
    print("------------------------------------")
    print("番号を入力してください。")
    print("番号 : ", end="")
    num = int(input())
    if (num == 1): # アンケート登録
      os.system('cls') #clear screen
      createSurvey(url)
      break
    elif (num == 2): # アンケート削除
      os.system('cls') #clear screen
      deleteSurvey(url)
      break
    elif (num == 3): # メインメニューへ戻る
      print("メインメニューへ戻ります")
      break
    else:
      pass

def createSurvey(url):
  """新しいアンケートを登録

  Args:
      url (String): Google firebase Realtime Database URL
  """
  print("===========[アンケート登録]===========")
  while(True):
    print("[アンケートのタイトルを入力してください]")
    print("タイトル : ", end="")
    title = input()
    print(f'アンケートのタイトルは"{title}"です。')
    print("正しいなら'1'を、キャンセルするなら'2'を入力してください。")
    print("番号 : ", end="")
    num = int(input())
    if (num == 1): #登録
      orgData = requests.get(url).json()
      id = len(orgData['servay']) + 1
      newData = {"id" : id, "title" : title, "agree" : 0, "against" : 0, "voter": 0}
      orgData['servay'].append(newData)
      putRes = requests.put(url, json=orgData)
      if (putRes.status_code == 200):
        print("アンケートを登録しました。")
        break
      else: # 200以外の場合
        print("登録にエラーが発生しました。\n(サーバーとのエラーが発生しました。)")
        break
    elif (num == 2): #キャンセル
      print("メインメニューへ戻ります")
      break
    else:
      print("正しい番号を入力してください。")
      print("メインメニューへ戻ります")
      break

def deleteSurvey(url):
  """アンケート削除

  Args:
      url (String): Google firebase Realtime Database URL
  """
  while(True):
    # アンケート選択
    res, num = voteSurvey.selectSurvey(url)
    if (num == -1): #error
      print("サーバーとのエラーが発生しました。")
    else:
      res = requests.get(url)
      selectSurvey = res.json()['servay'][num]['title']
      print(f'{selectSurvey}を選択しました')
      print("削除するなら'1'を、キャンセルするなら'2'を入力してください。")
      print("番号 : ", end="")
      select = int(input())

      if(select == 1): #削除
        orgData = requests.get(url).json()
        del orgData['servay'][num]

        # アンケートの削除をputする
        putRes = requests.put(url, json=orgData)

        if (putRes.status_code == 200): # 200 成功
          print("アンケートを削除しました。")
          break
        else: # 200以外の場合
          print("削除にエラーが発生しました。\n(サーバーとのエラーが発生しました。)")
          break
      elif(num == 2): #キャンセル
        print("メインメニューへ戻ります")
        break
      else:
        print("正しい番号を入力してください。")
        print("メインメニューへ戻ります")
        break