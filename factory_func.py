#!/usr/bin/env python
# coding: utf-8

"""
简单工厂模式
不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例

优点：
1、隐藏了对象创建的实现细节
2、客户端不需要修改代码
缺点：
1、违反了单一职责原则，将创建逻辑放到一个工厂类里
2、当添加新产品时，需要修改工厂类代码，违反了开闭原则
"""
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print "花呗支付%d元." % money
        else:
            print "支付宝支付%d元." % money


class WechatPay(Payment):
    def pay(self, money):
        print "微信支付%d元." % money


class PaymentFactory:
    def create_payment(self, method):
        if method == "alipay":
            return AliPay()
        elif method == "huabei":
            return AliPay(use_huabei=True)
        elif method == "wechat":
            return WechatPay()
        else:
            raise TypeError("No such payment named %s" % method)


# client
l = PaymentFactory()
p = l.create_payment("alipay")
p.pay(100)
