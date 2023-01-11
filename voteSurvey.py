import requests, json

def selectSurvey(url):
  """アンケートのtitleを出力して選択の数字を入力する

      Args:
      url (String): Google firebase Realtime Database URL
  """
  res = requests.get(url)
  cnt = 0 # アンケートの数

    # 200成功する場合
  if (res.status_code == 200):
    print("===========[アンケート選択]===========")
    for i in range(len(res.json()['servay'])):
      print("title : ", res.json()['servay'][i]['title'])
      print("番号 : ", res.json()['servay'][i]['id']+1)
      cnt += 1
      print("------------------------------------")

    while(True):
      print("アンケートの番号を入力してください")
      print("番号 : ", end="")
      num = int(input())
      if (num < 1 or num > cnt):
        pass
      else:
        break
    return res, num - 1
  else: # 200以外の場合
    return -1


def vote(res, i):
  """選択したアンケートに賛成と反対を投票する

  Args:
      res (Response): データベースのgetリクエスト
      i (int): 選択したアンケートのid

  Returns:
      voteData: 投票した内容
  """

  agree = res.json()['servay'][i]['agree']
  against = res.json()['servay'][i]['against']
  voter = res.json()['servay'][i]['voter']
  print("title : ", res.json()['servay'][i]['title'])

  while(True):
    print("賛成なら'1'を、反対なら'2'を入力してください。")
    print("番号 : ", end="")
    num = int(input())
    if (num == 1):
      agree += 1
      voter += 1
      break
    elif (num == 2):
      against += 1
      voter += 1
      break
    else:
      print("1か2を入力してください。")
  
  voteData = {"agree": agree, "against": against, "voter": voter}
  
  return voteData
  
def postVoid(url, i, voteData):
  """投票の内容をデータベースに送信する

  Args:
      url (String): Google firebase Realtime Database URL
      i (int): 選択したアンケートのid
      voteData (json): 投票した内容
  """
  # 新しいアンケートデータに代わる
  getRes = requests.get(url)
  orgData = getRes.json()
  orgData['servay'][i]['agree'] = voteData['agree']
  orgData['servay'][i]['against'] = voteData['against']
  orgData['servay'][i]['voter'] = voteData['voter']

  # データベースに投票した内容を送信する
  putRes = requests.put(url, data=json.dumps(orgData))

  # 200成功する場合
  if (putRes.status_code == 200):
    print("投票に成功しました。")
  else: # 200以外の場合
    print("投票にエラーが発生しました。\n(サーバーとのエラーが発生しました。)")