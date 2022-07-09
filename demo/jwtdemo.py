# -*- coding: utf8 -*-
# @Time    : 2022/7/9 22:12
# @Author  : wxvirus
# @File    : jwtdemo.py
# @Software: PyCharm
# jwt 生成demo
import base64
import json
import time
import hashlib

if __name__ == '__main__':
    # header_data = {"typ": "jwt", "alg": "HS256"}
    # header_json = json.dumps(header_data).encode()
    # # print(header_json)
    # # 头部生成
    # header = base64.b64encode(header_json).decode()
    # # print(header)
    #
    # iat = int(time.time())
    # payload_data = {
    #     "sub": "root",
    #     "exp": iat + 3600,  # 假设1小时过期
    #     "iat": iat,
    #     "name": "wujiedeyouxi",
    #     "avatar": "1.png",
    #     "user_id": 1,
    #     "admin": True,
    #     "acc_pwd": "dqwdqwdqwdqwdqwdqwdqwdwqdqw"
    # }
    # payload = base64.b64encode(json.dumps(payload_data).encode()).decode()
    # # print(payload)
    # # javascript atob(payload) 解析
    #
    # # 秘钥 不能泄露给客户端 我这里是瞎编的
    # secret = "dqwdqwdqwdqwdqwdqwdqwdqwdqwdqdwqdqwdwqdqwdqww"
    # data = header + payload + secret
    # HS256 = hashlib.sha256()
    # HS256.update(data.encode("utf-8"))
    # # 签证 第三段
    # signature = HS256.hexdigest()
    # # print(signature)
    #
    # jwt_token = f"{header}.{payload}.{signature}"
    # print(jwt_token)

    # 验证是否过期
    token = "eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiAicm9vdCIsICJleHAiOiAxNjU3MzgwNDQ4LCAiaWF0IjogMTY1NzM3Njg0OCwgIm5hbWUiOiAid3VqaWVkZXlvdXhpIiwgImF2YXRhciI6ICIxLnBuZyIsICJ1c2VyX2lkIjogMSwgImFkbWluIjogdHJ1ZSwgImFjY19wd2QiOiAiZHF3ZHF3ZHF3ZHF3ZHF3ZHF3ZHF3ZHdxZHF3In0=.74e9c088b4eb2521505ae4e307ccd23240e631941b2273fcd5507dd14a4a8315"
    h, p, s = token.split(".")
    p_data = json.loads(base64.b64decode(p.encode()))
    print(p_data)
    exp = p_data.get("exp", None)
    if exp is not None and int(exp) < int(time.time()):
        print("token 过期")
    else:
        print("没有过期")
