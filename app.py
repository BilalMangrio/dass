from flask import Flask,request,jsonify
import pickle
import numpy as np


gb=pickle.load(open('gb.pickle','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return 'API For Depression, Stress and Anxiety'

@app.route('/depression', methods=['POST'])
def depression_api_method():
  data = request.get_json()
  array = data['questionScoresArray']
  question_scores = np.array(array, ndmin=2)
  #print(question_scores)
  prediction = gb.predict(question_scores)
  final_prediction=int(prediction[0])
  if(final_prediction==0):
    final_='you are normal '
  elif(final_prediction==1):
    final_='you have mild depression'
  elif(final_prediction==2):
    final_='you have moderate depression'
  elif(final_prediction==3):
    final_='you have severe depression'
  else:
    print('unfortunately we couldnt predict ')
    
  print(final_)
  return  jsonify(final_prediction)



if __name__ == '__main__':
    app.run(debug=True)