import requests, os

def selectSurvey():
  """アンケートのtitleを出力して選択の数字を入力する
  """
  res = requests.get('https://API.json')
  cnt = 0

  print("------------[アンケート選択]------------")
  for i in range(len(res.json()['servay'])):
    print("title : ", res.json()['servay'][i]['title'])
    print("番号 : ", res.json()['servay'][i]['id']+1)
    cnt += 1
    print("------------------------------------")

  print("アンケートの番号を入力してください")
  print("番号 : ", end="")
  num = int(input()) - 1
  vote(res, num)

  # os.system("pause") #Press any key to continue


def vote(res, i):
  """選択したアンケートに賛成と反対を投票する

  Args:
      res (Response): データベースのgetリクエスト
      i (int): 選択したアンケートのid
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
      break
    elif (num == 2):
      against += 1
      break
    else:
      print("1か2を入力してください。")
  
  postVoid(agree, against, voter)
  
def postVoid(agree, against, voter):
  """投票の内容をデータベースに送信する

  Args:
      agree (int): 賛成数
      against (int): 反対数
      voter (int): 投票者の数
  """
  voter += 1
  
  print(agree, against, voter)
  #TODO 투표 내용 post 하기


selectSurvey()