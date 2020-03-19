from flask import jsonify, Flask, request
# from udicOpenData.stopwords import *
import jieba
# https://github.com/UDICatNCHU/UdicOpenData
import json

app = Flask(__name__)

def segment(ori_text):
    # seg_text = rmsw(ori_text)
    seg_text = jieba.lcut(ori_text)
    # 使用rmsw速度太慢可改用jieba
    return list(seg_text)


@app.route("/postjson", methods=['POST'])
def postJsonHandler():
    content = request.get_json()
    print (content)
    seg_list = segment(content['data'])
    index = content['index']
    return jsonify({"seg_data":seg_list,"index":index}),200

app.run()