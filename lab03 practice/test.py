import requests
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello_world():
      return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post_ex', methods=["POST"])
def login():
    if request.method == "POST" :
        print("post")
        print(request.form["id_new"])
        print(request.form["password_new"])
        
        #저장
        # 
        # #이미 저장해놓은 행동을 함

        return jsonify({"status" : "ok"})

@app.route('/get_example')
def example():
    req = request.get("hettp://www.naver.com")
    soup = BeautifulSoup(req.text, "html.parser")
    print(soup)
    
if __name__=='__main__':
    app.run()