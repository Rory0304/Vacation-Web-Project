from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/about')
def hello_world2():
    return render_template("about.html")


@app.route('/post', methods=['POST'])
def login():
    if request.method == "POST" :

        id = request.form['id']
        password = request.form['password']

        # 데이터베이스에 저장

        return jsonify({'status':'OK','id':id,'password':password})


@app.route('/get')
def get_data():


    # 미리 지정해놓은 정보들
    list = ["a", "b", "c", "d"]

    return render_template("search_success.html", data = list)

if __name__ == '__main__':
    app.run()




