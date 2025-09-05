import webbrowser

from flask import Flask, render_template
import subprocess
app = Flask(__name__)

@app.route('/')
def home():
    subprocess.call(['python', 'Test1.py'])
    print('processed')
    url = r'C:\Users\prish\PyCharmMiscProject\Alankritha\templates\test1_image_gallery.html'
    webbrowser.open_new_tab(url)

if __name__ == '__main__':
    app.run(debug=True) # debug=True enables auto-reloading and debugger