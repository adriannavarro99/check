from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html",row=8,col=8,color1='red',color2='black')


@app.route('/<int:row>')
def row1(row):
    return render_template("index.html",row=row,col=8,color1='red',color2='black')

@app.route('/<int:row>/<int:col>')
def row2(row,col):
    return render_template("index.html",row=row,col=col,color1='red',color2='black')

@app.route('/<int:row>/<int:col>/<string:one>')
def row_col_one(row,col,color1):
    return render_template("index.html",row=row,col=col,color1=color1,color2='black')

@app.route('/<int:row>/<int:col>/<string:one>/<string:two>')
def row_col_two(row,col,color1,color2):
    return render_template("index.html",row=row,col=col,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)