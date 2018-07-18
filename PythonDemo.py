from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    s1=int(input('小明上学期期末成绩为：'))
    s2=int(input('小明本学期期末成绩为：'))
    r=((s2-s1)/s1*100)
    print('小明本次成绩变化为 %.1f%%'%r)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
