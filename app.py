from flask import Flask, render_template,request
#render_templateでhtmlとpythonを独立させて編集が可能になる
#htmlはtemplatesの中で編集する
app = Flask(__name__)
#__で囲めば自動で変数の中身が変わる
#name:ファイル名 file:ファイルのフルパス init:初期化

@app.route('/') #url末尾が/の場所にアクセスするとしたのコードが動く
def index():
    return render_template('index.html')

# 追加画面
@app.route('/add')
def add_page():
    return render_template('add.html')

@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form.get('title')
    memo = request.form.get('memo')
    print(f"受け取った記録: {title} / {memo}")
    return "データを受け取ったよ！"

#実行すると__name__は__main__が代入される
if __name__ == '__main__':
    app.run(debug=True)