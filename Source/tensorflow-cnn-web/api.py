def predict1( string):
 import requests as r
 import json
 a=r.get('https://api.edamam.com/api/nutrition-data?app_id=f7a6a659&app_key=c8e521fcc893cafd6a9f94bb33c514e4&ingr=1%20large%20'+string)
 b=a.text

 res=json.loads(b)
 calories=res['calories']
 fat=res['totalNutrients']['FAT']['quantity']
 energy=res['totalNutrients']['ENERC_KCAL']['quantity']
 carbs=res['totalNutrients']['Carbs']['quantity']
 sugar=res['totalNutrients']['SUGAR']['quantity']
 data=[calories,fat,energy,carbs,sugar]
 return data