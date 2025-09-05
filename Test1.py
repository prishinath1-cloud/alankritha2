import os


folder_path = r'C:/Users/prish/PyCharmMiscProject/Alankritha/static/img'
images = [img for img in os.listdir(folder_path) if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

html_content = '<html><style>.container{text-align:center; border:0px;} .fake_img{display:inline-block; margin:2px 2px; padding:2px; border:0px;}</style><body><div class="container">'

for image in images:
    html_content += f'<div class="fake_img"><img src="{os.path.join('/static/img', image)}" alt="{image}" style="width:300px; margin:10px;"></div>'
html_content += '</div></body></html>'

with open('templates/my_photos_gallery_page.html', 'w') as f:
    f.write(html_content)

