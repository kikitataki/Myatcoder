from flask import Flask, render_template,request,redirect
#render_templateでhtmlとpythonを独立させて編集が可能になる
#htmlはtemplatesの中で編集する
app = Flask(__name__)
#__で囲めば自動で変数の中身が変わる
#name:ファイル名 file:ファイルのフルパス init:初期化

import sqlite3

def connectdb():
    # atcoder.db というファイルを作成して接続
    conn = sqlite3.connect('atcoder.db')
    cursor = conn.cursor()
    # postsという名前の表を作る（すでにあれば何もしない）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            memo TEXT
        )
    ''')
    conn.commit()
    conn.close()

connectdb() # アプリ起動時に実行


@app.route('/') #url末尾が/の場所にアクセスするとしたのコードが動く
def index():
    # データベースに接続
    conn = sqlite3.connect('atcoder.db')
    conn.row_factory = sqlite3.Row  # これを書くと辞書形式（post['title']）で扱える
    cursor = conn.cursor()
    
    # データを取得（新しい順）
    cursor.execute('SELECT * FROM posts ORDER BY id DESC')
    posts = cursor.fetchall()  # 全データを取得
    conn.close()

    # 第二引数で HTML に posts という名前でデータを渡す
    return render_template('index.html', posts=posts)


# 追加画面
@app.route('/add')
def add_page():
    return render_template('add.html')

@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form.get('title')
    memo = request.form.get('memo')

    # データベースに保存
    conn = sqlite3.connect('atcoder.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (title, memo) VALUES (?, ?)', (title, memo))
    conn.commit()
    conn.close()

    return redirect('/') # 保存が終わったらトップページに戻る

#実行すると__name__は__main__が代入される
if __name__ == '__main__':
    app.run(debug=True)