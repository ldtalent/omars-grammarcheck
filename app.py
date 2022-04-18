from flask import Flask, render_template,request,url_for
from flask_bootstrap import Bootstrap 

import language_tool_python

#text = "These is mi Resume !"
#mes = tool.check(text)
#out = ""
#for elment in mes:
#    out = elment.message
#    print(elment.message)
app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

    
@app.route('/analyse', methods=['POST'])
def analyse():
    ret = list()
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        tool = language_tool_python.LanguageTool('en-US')
        err = tool.check(rawtext)
        received_text2 = rawtext
        for elm in err:
            #print(elm.message)
            ret.append(elm.message)
    return render_template('index.html', received_text = received_text2, summary=ret)

if __name__ == '__main__':
	app.run(debug=True)