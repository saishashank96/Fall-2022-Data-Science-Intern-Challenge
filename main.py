import pandas as pd
data=pd.read_csv('2019 Winter Data Science Intern Challenge Data Set.csv')
#print(data)
#On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe
#print(data['order_id'])
dict1={}
#Check whether there is any anomaly, check if same shop_id has different rates for same sneaker
for i in range(len(data)-1):
  if data['shop_id'][i] in dict1:
    if data['order_amount'][i]/data['total_items'][i]!=dict1[data['shop_id'][i]]:
      print(data['shop_id'][i])
  else:
    dict1[data['shop_id'][i]]=data['order_amount'][i]/data['total_items'][i]
pd.set_option('display.max_columns', None)
#There was no anomaly found i.e no price difference for same sneakers(shop_id)
print(data.describe())
#box plot to check skewness 
import matplotlib.pyplot as plt
plt.boxplot(data.order_amount)
plt.show()
#It seems that few transaction are big on order_amount, it can be a anomaly if it happens few number of times
high=data.sort_values(by='order_amount',ascending=False) 
print(high.head(10))
#it seems that the shop_id =42 and user_id=607 are having multiple big transactions hence anomaly can be ruled out.

# Median would be a better measure
print("Median: ",data.order_amount.median())
#284