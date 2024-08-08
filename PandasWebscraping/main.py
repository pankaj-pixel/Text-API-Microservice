
from bs4 import BeautifulSoup
import pandas as pd
import requests


#Extract Data From url and create list and store in Pandas Data Frame

"""
url = "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.ram%255B%255D%3D8%2BGB%2Band%2BAbove"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
#print(soup)

product_name =[]
Ratings = []
Prices = []
 
title =  soup.find_all('div',class_="KzDlHZ")
for i in title:
    name = i.text
    product_name.append(name)

print("Product_name : ", product_name)  
#print(len(product_name))  

   
rate = soup.find_all('div',class_="XQDdHH")   
for i in rate:
    name2 = i.text
    Ratings.append(name2)

print("Ratings : " ,Ratings)    
#print(len(Ratings))  


Rate = soup.find_all('div',class_="Nx9bqj _4b5DiR")
for i in Rate:
    name3 = i.text
    Prices.append(name3)



#print("Prices : " ,Prices)    
#print(len(Prices))  

# Create DataFrame of multiple List using Pandas Library
#column2 = pd.DataFrame(Ratings,columns=['Ratings'])
#column3 = pd.DataFrame(Prices,columns=["Price"])


df = pd.DataFrame({
    "Product_Name": product_name,
    "Price": Prices,
    "Ratings": Ratings
})
#print(df)

#convert the dataframe into csv file
#df.to_csv("product_details.csv")

"""



#extracted  Data from Nested HTML Tag
"""url ="https://www.flipkart.com/search?q=mobile+under+30000+to+40000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_2_17_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_17_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile+under+30000+to+40000&requestId=b7a6bf26-8ddb-4c82-800a-b302514e2a23&as-backfill=on"
r = requests.get(url)

soup = BeautifulSoup(r.text ,"lxml")
#print(soup)



mobile = soup.find_all("div",class_="col col-7-12")[1]
for i in mobile:
    name =(i.text)
    print(name)"""


# extract information From Nested Html tag 
#<ul> 
#<li>
#<ul>

"""url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers"
r  = requests.get(url)
soup = BeautifulSoup(r.text , "lxml")
#print(soup)


ul = soup.find_all("ul",class_="nav flex-column",id="side-menu")
#print(ul)

name = soup.find("a", class_ ="nav-link")
for i in name:
    print(i.text)
"""






#Extract Tables from website
url = "https://prsindia.org/covid-19/cases"  
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
#print(soup)


table = soup.find_all("table",class_="table table-striped table-bordered")
print(table)
















