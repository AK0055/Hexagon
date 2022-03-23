from flask import Flask, render_template
  
app = Flask(__name__)
  
@app.route('/')
def form():
     return render_template('form.html')
@app.route('/index')
def index():
     return render_template('editor.html')
# @app.route('/favicon.ico')
# def favicon():
#     return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run()

