# 测试flask app 模板

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def fun1():
    greeting = "Hello World."
    return render_template("index.html", greeting=greeting)


def fun2():

    return "You are welcome."


if __name__ == "__main__":
    app.run()
# 运行的是第一个函数,函数名不影响。
