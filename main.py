import base64

image_file_path = "inputpath"

with open(image_file_path, mode='rb') as f:
    image_file = f.read()

# base64エンコードする
binary_file_b64 = base64.b64encode(image_file)

# base64エンコードしたバイナリデータをターミナルに表示してみる
print(binary_file_b64)

# base64デコードする
image_file = base64.b64decode(binary_file_b64)

# 保存する画像ファイルのパスを指定する
save_image_file_path = "outputpath"

# jpgファイルにバイナリデータを書き込む
with open(save_image_file_path, mode='wb') as f:
    f.write(image_file)