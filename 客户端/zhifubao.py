# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from alipay import AliPay
import time
import qrcode


alipay_public_key_string = '''-----BEGIN PUBLIC KEY-----  
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3SR2KYvarYLqO74YKfMs1y7YF/3It9grR0y2138s920sq4yGjdvGgbpBtkSecaVrvPVTMtQJ1t/l8UAV4Tfy1TfL2ey0S+znbP5gKguqdWqwaJYTo3N5/k2SiEStlq/OBpoAgYwn0mfu6BGol0p0c4ZYimbfSeJLk4W5AUuifHROuEIHPbtKOUrYER8N+KGx9qcYBw9dZxRb0QgtVnehtMGDp9mvpo9NvUuUUYIMpoA9G64lgL6Q5revuJVKCaROj/YJMK1fl9gkI1i07ze7lw+sjMWkHB/z2SN6wecCYUC9OnwHrZgYYM18Ls0vvG7Ebpc+iV1/yoH5NB8YhDHEAwIDAQAB
-----END PUBLIC KEY-----'''


app_private_key_string = '''-----BEGIN RSA PRIVATE KEY-----
    MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC/GK4uK/73ZDdp4ovyWZMiH4nJEnFm1olwFsh14K6bCTagj40yZCr2gnsMnE5NYrVFJwgEPqyWx5d8HPq0qjIFk/jfNCnn86KFzOt3r4QeTNNg2ZoyGXS1kB+zLUvkQBHnVtcIK8YRNrYUdbf7c1XVtm+yRj86TOYsjdvsWVwi4OvHWw4nzvAK0WvHZLnAhY9y3JKsPQ5JBWMBRXWp4I+TjEcKJEDqUPzal1mddWMZ2mrynYnp/MRC+nsSY6/DKzXTt1E6U9b4RJsWNqdgvCUcWGL0XMEBXoACYJ/nmyRgIi/bM1tJd13ofoJh4BNeVdM5HBspepdawyzCybKgu97rAgMBAAECggEADFHKAN4DPO2wCNp7DS+rJZsE5fqTZv7Ts280kyzd9M6+P9GhV6tPfb7hseltvt1rND8U7DkiJUJOyMiRfQ4v1V45wCH7xaFWS+vvDjM5gD6Rrf+5ShuMA5x7/rAf4WIkBVb62+L+jOOLD3ybVNGVqgZt4v9WWirU9/BZSj5kizb6DribgAPjp1W3s1yT+BlbtxmK1KIMYWk4I6Is+zirfjRbyMpbovIkP8jtt1SCXTobR+BGL7ibkCxPPHxbaUSd4Djs4dbL0JQchPar0EWSSUgH3gtYqKWWJkdfCPzlQYagl9F/zbcHUYODFueLbccG44H97CJam5aHZeXggqxWyQKBgQD+uQyu7z2X2rEF/8MgINR8DYrsJYGXkd7RH89lSaTQ/WYuCv7EIUn0SgxLEmlyZeuJraXOq6y1tnNOGMWDz7Sy3MCYdUftMbMJTJbSBrApMFUS1+WQmtFFRuv3P6Bl3jq+qgikEnmgK8RuDMfwcdYl4cXQ5vufydGqQ3xJJhK+twKBgQDADfaAJSehyxkA1EctXa//Ed5ZQuB8BQkHQXrfwd4lyCVfCBr6rSsx5IM1ynj2mKNpmhDAg+Jt33xdlP/pkLJeEvgb6XtNPpr0jCw86AzrcyyBnC4SpoWL7u1Wp2C0i3wRAYlC/KbKPzDsf5db3EsLC008YGlZ+HyCDBnS4BmtbQKBgGD8IkklDEWaXdaT6D5+YYkOOvvo1+vW/YiQXQ4KuTddlB8pzpDsv9TEsOOQkhedmM3mEQCcuvjBDCwLIIEsf3eut6IU3ZsBVlLPF4nGRCKapXm0PFMPr2h6NXQBhNfkgmeAJCQcaLTElVj1gtcY8NmhmgkNOXdAh5UVduf/GBoHAoGATZrWyn05AIXC+rTMdiZvYZBk2ojNkQ+v0EDDV/tMutOfVkE+NaEX3TdLVccVDgAruBZLQp+INYGjDWWR611O1fiwTQcRjesITlz92zahUdreVxk2/M5RFHRdbzB/QTVD0tNeFbVl6D+Uk1wTW0kvAa11bjo/F93y4dHl9XIcrhkCgYAYjuJaGNqdM1Sz9ZGXdvARmdeZqSerp13xw1BM0yikhlrYSGWcz4uagx71SrK6jNH9ptQ6KlAKjLmwOFfXxqpj+4ZigdM6JhH7Y/LAbAE2/L7kDswQqj4QT+URyup5rZc0cxZKSGDAWmolu+bsqbx++ieHb9RkZxAiAdAn/AWyhA==
-----END RSA PRIVATE KEY-----'''

# 注意：一个是支付宝公钥，一个是应用私钥

APP_ID = '2016091700528524'
NOTIFY_URL = 'https://openapi.alipaydev.com/gateway.do'


def init_alipay_cfg():
    '''
    初始化alipay配置
    :return: alipay 对象
    '''
    alipay = AliPay(
        appid=APP_ID,
        app_notify_url=NOTIFY_URL,  # 默认回调url
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=True  # 默认False ,若开启则使用沙盒环境的支付宝公钥
    )
    return alipay


def get_qr_code(code_url):
    '''
    生成二维码
    :return None
    '''
    # print(code_url)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    qr.add_data(code_url)  # 二维码所含信息
    img = qr.make_image()  # 生成二维码图片
    img.save(r'erweima.png')
    print('二维码保存成功！')


def preCreateOrder(subject: 'order_desc', out_trade_no: int, total_amount: (float, 'eg:0.01')):
    '''
    创建预付订单
    :return None：表示预付订单创建失败  [或]  code_url：二维码url
    '''
    result = init_alipay_cfg().api_alipay_trade_precreate(
        subject=subject,
        out_trade_no=out_trade_no,
        total_amount=total_amount)
    print('返回值：', result)
    code_url = result.get('qr_code')
    if not code_url:
        print(result.get('预付订单创建失败：', 'msg'))
        return
    else:
        get_qr_code(code_url)
        # return code_url


def query_order(out_trade_no: int):
    '''
    :param out_trade_no: 商户订单号
    :return: None
    '''
    print('预付订单已创建,请在120秒内扫码支付,过期订单将被取消！')
    # check order status
    _time = 0
    # while True:
    #     # check every 3s, and 10 times in all

    #     print("now sleep 2s")
    #     time.sleep(2)

    result = init_alipay_cfg().api_alipay_trade_query(out_trade_no=out_trade_no)
    if result.get("trade_status", "") == "TRADE_SUCCESS":
        print('订单已支付!')
        print('订单查询返回值：', result)
        return "支付成功"
    _time += 1
    if _time >= 120:
        # cancel_order(out_trade_no, cancel_time)
        ni.zhifu.stop()
        return "支付失败"


# def cancel_order(out_trade_no: int, cancel_time=None):
#     '''
#     撤销订单
#     :param out_trade_no:
#     :param cancel_time: 撤销前的等待时间(若未支付)，撤销后在商家中心-交易下的交易状态显示为"关闭"
#     :return:
#     '''
#     result = init_alipay_cfg().api_alipay_trade_cancel(out_trade_no=out_trade_no)
#     #print('取消订单返回值：', result)
#     resp_state = result.get('msg')
#     action = result.get('action')
#     if resp_state == 'Success':
#         if action == 'close':
#             if cancel_time:
#                 print("%s秒内未支付订单，订单已被取消！" % cancel_time)
#         elif action == 'refund':
#             print('该笔交易目前状态为：', action)

#         return action

#     else:
#         print('请求失败：', resp_state)
#         return


# def need_refund(out_trade_no: str or int, refund_amount: int or float, out_request_no: str):
#     '''
#     退款操作
#     :param out_trade_no: 商户订单号
#     :param refund_amount: 退款金额，小于等于订单金额
#     :param out_request_no: 商户自定义参数，用来标识该次退款请求的唯一性,可使用 out_trade_no_退款金额*100 的构造方式
#     :return:
#     '''
#     result = init_alipay_cfg().api_alipay_trade_refund(out_trade_no=out_trade_no,
#                                                        refund_amount=refund_amount,
#                                                        out_request_no=out_request_no)

#     if result["code"] == "10000":
#         return result  # 接口调用成功则返回result
#     else:
#         return result["msg"]  # 接口调用失败则返回原因


# def refund_query(out_request_no: str, out_trade_no: str or int):
#     '''
#     退款查询：同一笔交易可能有多次退款操作（每次退一部分）
#     :param out_request_no: 商户自定义的单次退款请求标识符
#     :param out_trade_no: 商户订单号
#     :return:
#     '''
#     result = init_alipay_cfg().api_alipay_trade_fastpay_refund_query(
#         out_request_no, out_trade_no=out_trade_no)

#     if result["code"] == "10000":
#         return result  # 接口调用成功则返回result
#     else:
#         return result["msg"]  # 接口调用失败则返回原因

# def

    # print('5s后订单自动退款')
    # time.sleep(5)
    # print(need_refund(out_trade_no, 0.01, 111))

    # print('5s后查询退款')
    # time.sleep(5)
    # print(refund_query(out_request_no=111, out_trade_no=out_trade_no))
    # 操作完登录 https://authsu18.alipay.com/login/index.htm中的对账中心查看是否有一笔交易生成
