import requests
from bs4 import BeautifulSoup
import pandas as pd

items_info = []

for number in range(1,20):
  url=f"https://bank.uz/credits?PAGEN_1={number}"
  
  reqs=requests.get(url=url)
  soup =BeautifulSoup(reqs.content, "html.parser")


  section_info  = soup.find_all("div", class_="table-card-offers-bottom")

  def bank_uz():

    for i in section_info:
      
      item_name = i.find("div",class_ ="table-card-offers-block1-text")
      name = item_name.span.text

      item_kredit = i.find("div", class_ = "table-card-offers-block1-text")
      kredit = item_kredit.a.text

      item_procent = i.find("div", class_ = "table-card-offers-block2")
      procent = item_procent.span.text
      

      item_term = i.find("div", class_ ="table-card-offers-block3")
      term = item_term.span.text

      item_amount = i.find("div", class_="table-card-offers-block4")
      amount = item_amount.span.text

      item_link = i.find("div",class_ ="table-card-offers-block5")
      link = item_link.a.get("href")
      

      items_info.append([name,kredit,procent,term,amount,link])

      

    return items_info
  bank_uz()

columns = ["Bank","Kredit(for)","Procent","Term","Amount","Details"]
df = pd.DataFrame(data= items_info, columns=columns)
df.to_csv("bank_uz_kredits.csv", index = False)