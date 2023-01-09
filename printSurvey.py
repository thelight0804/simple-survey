import requests, os

def printTest():
  """アンカーとの一覧を出力する
  """
  res = requests.get('https://API.json')
  print("------------[アンケートへの一覧]------------")
  for i in range(len(res.json()['servay'])):
    print("title : ", res.json()['servay'][i]['title'])
    print("id : ", res.json()['servay'][i]['id'])
    print("agree : ", res.json()['servay'][i]['agree'])
    print("against : ", res.json()['servay'][i]['against'])
    print("voter : ", res.json()['servay'][i]['voter'])
    print("------------------------------------")
  os.system("pause") #Press any key to continue