from flask import Flask, Response, request
import base64
import requests
import json
import conf_text

app = Flask(__name__)


@app.route('/')
def index():
    ass = '<a href="https://t.me/URL1999">https://t.me/URL1999</a> our telegram Channel'
    return Response(ass, status=200,)


@app.route('/sub/<url>')
def profile(url: str):
    name_num = 0
    url = base64.standard_b64decode(url).decode('utf-8')
    data = requests.get("http://"+url, timeout=30)
    context = data.content.decode("utf-8")
    if context.find("://") == -1:
        context = base64.standard_b64decode(data.content).decode('utf-8')
    context = context.split("\n")
    name_conf = ""
    all_proxy = ""
    for i in context:
        i = i.split("://")
        if i[0] == "vless":
            continue
        else:
            if i[0] == "vmess":
                final: dict = json.loads(
                    base64.standard_b64decode(i[1]).decode('utf-8'))
                ps = final.get("ps")
                ps = f"{ps} {name_num}"
                name_num += 1
                add = final.get("add")
                port = final.get("port")
                type_ = final.get("type", "vmess")
                type_ = "vmess"

                if type_ == "none":
                    type_ = "vmess"
                id_ = final.get("id")
                sni = final.get("sni")
                aid = final.get("aid", "0")
                tls = final.get("tls", "0")
                if tls == "tls":
                    tls = "true"
                net = final.get("net")
                path = final.get("path")
                host = final.get("host")
                all_proxy += conf_text.proxy.format(name=ps, server=add, port=port, type=type_, uuid=id_,
                                                    sni=sni, alterID=aid, tls=tls, network=net, )
                if host == "":
                    pass
                else:
                    all_proxy += conf_text.header.format(path=path, HOST=host)
                name_conf += f"    - {ps}\n"
    conf = conf_text.head + all_proxy + \
        conf_text.fotter.format(pp=name_conf, gg=name_conf)
    # print(conf)
    return Response(conf, status=200, mimetype="application/yaml")


if __name__ == '__main__':

    app.run(debug=False)
