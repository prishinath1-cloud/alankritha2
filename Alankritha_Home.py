import psycopg2
from flask import Flask, request, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

app = Flask(__name__, static_url_path='/static')

folder_path = r'C:/Users/prish/PyCharmMiscProject/Alankritha/static/img'
images = [img for img in os.listdir(folder_path) if img.endswith(('.png', '.jpg', '.jpeg', '.gif')) and '_' not in img]

@app.route('/')
def my_form_fun():
    return render_template('alankritha_home_page.html')

@app.route('/my_photos_gallery_path',methods= ['GET'])
def my_photos_gallery_fun():
    return render_template('my_photos_gallery_page.html',images_para = images)

@app.route('/photo_detail_page_path/',methods= ['GET'])
def my_photo_detail_fun(product_id):
    return render_template('product_detail_page.html',product_id_para = product_id)

@app.route('/product_detail_fun/<product_id>', methods=['GET','POST'])
def product_detail_fun(product_id):
    check = ''
    with open('details.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == product_id:
                return render_template('product_detail_page.html',product_id_para = product_id, desc_para = row[1], sellingprice_para = row[2], costprice_para = row[3], size_para = row[4])
            else:
                check = 'false'
    if check == 'false':
        return render_template('product_detail_page.html', product_id_para=product_id)

if __name__ == '__main__':
    app.run(debug=True)