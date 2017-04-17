import requests as r
import json
data='good food'
a1 = r.get('http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment?apikey=d0e7bf68cdda677938e6c186eaf2b755ef737cd8&outputMode=json&text=' + data)
b=a1.text
res = json.loads(b)
score=res['docSentiment']['score']
sent=res['docSentiment']['type']