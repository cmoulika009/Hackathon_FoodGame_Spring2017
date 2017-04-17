import tensorflow as tf, sys
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import base64
import requests as r
import json

# webapp
app = Flask(__name__)
#image_path = sys.argv[1]


@app.route('/api/predict', methods=['POST'])
@cross_origin()
def predict():
    data = request.values['imageBase64']
    with open("imageToPredict.jpeg", "wb") as fh:
        fh.write(base64.b64decode(data))
    # image_data = re.sub('^data:image/.+;base64,', '', image_b64).decode('base64')

    image_path = 'imageToPredict.jpeg'
    # Read in the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("data/output_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("data/output_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                               {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        print(predictions)
        #print('`````````````````````````````')
        output_string = []
        output_score = []
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            output_string.append(human_string)
            output_score.append(score)
            print('%s (score = %.5f)' % (human_string, score))


        print(label_lines[top_k[0]])
        #print('-------------------------------------------------')
        a = r.get('https://api.edamam.com/api/nutrition-data?app_id=f7a6a659&app_key=c8e521fcc893cafd6a9f94bb33c514e4&ingr=1%20' + label_lines[top_k[0]])
        b = a.text
        res = json.loads(b)
        calories = res['calories']
        #fat = res['totalNutrients']['FAT']['quantity']
        #energy = res['totalNutrients']['ENERC_KCAL']['quantity']
        #carbs = res['totalNutrients']['CHOCDF']['quantity']
        #sugar = res['totalNutrients']['SUGAR']['quantity']
        data = [calories]
        #print('1111111111111111111111111111111111111111111111111111111111111')
        print(data)

    return jsonify(results=[output_string[0],data])
@app.route('/api/predict1', methods=['POST'])
@cross_origin()
def predict1():
    data = request.values['imageBase64']


    a = r.get('http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment?apikey=d0e7bf68cdda677938e6c186eaf2b755ef737cd8&outputMode=json&text=' + data)
    b = a.text
    res = json.loads(b)
    sentiment = res['docSentiment']
    score=sentiment['score']
    type=sentiment['type']
    print(score)
    print(type)
    return jsonify(results=[score,type])


@app.route('/')
def main():
    return render_template('index.html')