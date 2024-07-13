from flask import Flask, render_template, send_from_directory
import os
from k_mean import main as run_lda

app = Flask(__name__)

def check_and_run_lda():
    image_dir = os.path.join(app.root_path, 'static', 'images')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    images = os.listdir(image_dir)
    if len(images) < 40:  
        run_lda()

@app.route('/')
def index():
    check_and_run_lda()
    mini_clusters = [f"mini_cluster_{i}.png" for i in range(20)]
    newsgroups_clusters = [f"20newsgroups_cluster_{i}.png" for i in range(20)]
    return render_template('index.html', mini_clusters=mini_clusters, newsgroups_clusters=newsgroups_clusters)

@app.route('/static/images/<filename>')
def images(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'), filename)

if __name__ == '__main__':
    app.run(debug=True)
