# LantraDict - app.py
# Coded by Jackson Ma

from flask import Flask, render_template, request
from pypinyin import lazy_pinyin, Style
from zhconv import convert
from xy_zidian import char_info

app = Flask(__name__)
HANZI = ''


# 获取汉字信息
def get_info(char=''):
    char_explanation = char_info(char)

    hanzi  = char_explanation["name"]
    pinyin = char_explanation["pinyin"]
    bihua  = char_explanation["bihua"]
    bushou = char_explanation["bushou"]
    jiegou = char_explanation["jiegou"]
    bishun = char_explanation["bishun"]
    wubi   = char_explanation["wubi"]

    explanations = char_explanation["explain"]

    zhuyin_style = Style.BOPOMOFO
    zhuyin = lazy_pinyin(hanzi, style=zhuyin_style)[0]

    fanti = convert(hanzi, "zh-hant")

    return hanzi, fanti, pinyin, bihua, bushou, jiegou, bishun, wubi, zhuyin, explanations


# 初始索引页
@app.route('/')
def index():
    return render_template("index.html")


# 查找结果页
@app.route("/search-char", methods=["GET"])
def search_char():
    global HANZI
    HANZI = request.values.get("search-line")

    try:
        hanzi, fanti, pinyin, bihua, bushou, jiegou, bishun, wubi, zhuyin, explanations = get_info(HANZI)

        return render_template("search-result.html",
                hanzi=hanzi, fanti=fanti, pinyin=pinyin, bihua=bihua, bushou=bushou, jiegou=jiegou, bishun=bishun, wubi=wubi, zhuyin=zhuyin,
                explanations=explanations)
    except:
        return render_template("search-result.html", is_err=True)


@app.errorhandler(404)
def err_404(err_msg):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(port=5500)
