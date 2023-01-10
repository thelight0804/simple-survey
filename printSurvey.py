import requests, os

def printVote(url):
  """アンカーとの一覧を出力する

    Args:
      url (String): Google firebase Realtime Database URL
  """
  res = requests.get(url)

  # 200成功する場合
  if (res.status_code == 200):
    print("===========[アンケートへの一覧]===========")
    for i in range(len(res.json()['servay'])):
      print("title : ", res.json()['servay'][i]['title'])
      # print("id : ", res.json()['servay'][i]['id'])
      # print("agree : ", res.json()['servay'][i]['agree'])
      # print("against : ", res.json()['servay'][i]['against'])
      print("voter : ", res.json()['servay'][i]['voter'])
      print("------------------------------------")
  else: # 200以外の場合
    print("サーバーとのエラーが発生しました。")

def printResult(res, i):
  """アンケート回答の一覧を表示する

  Args:
      res (Response): データベースのgetリクエスト
      i (int): 選択したアンケートのid
  """
  title = res.json()['servay'][i]['title']

  print(f'===========["{title}"回答]===========')
  print("賛成 : ", res.json()['servay'][i]['agree'])
  print("反対 : ", res.json()['servay'][i]['against'])
  print("投票者 : ", res.json()['servay'][i]['voter'])
  print("------------------------------------")