import requests

def management(url):
  """アンケート管理画面

  Args:
      url (String): Google firebase Realtime Database URL
  """
  print("===========[アンケート管理]===========")
  while(True):
    print("* 1. アンケート登録")
    print("* 2. アンケート削除")
    print("------------------------------------")
    print("番号を入力してください。")
    print("番号 : ", end="")
    num = int(input())
    if (num == 1): # アンケート登録
      createSurvey(url)
      break
    elif (num == 2): # アンケート削除
      # TODO アンケート削除
      break

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
        print("投票に成功しました。")
        break
      else: # 200以外の場合
        print("投票にエラーが発生しました。\n(サーバーとのエラーが発生しました。)")
        break
    elif (num == 2): #キャンセル
      print("メインメニューへ戻ります")
      break
    else:
      print("正しい番号を入力してください。")
      print("メインメニューへ戻ります")