#!/usr/bin/env python
# coding: utf-8

"""
工厂方法
定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类
角色：
    抽象工厂角色
    具体工厂角色
    抽象产品角色
    具体产品角色

优点：
1、每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
2、隐藏了对象创建的实现细节
缺点：
1、每增加一个具体产品类，就必须增加一个相应的工厂类
"""
from abc import ABCMeta, abstractmethod


class Payment():
    __metaclass__ = ABCMeta

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


class BankPay(Payment):
    def pay(self, money):
        print "银行卡支付%d元." % money


class PaymentFactory():
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return AliPay()


class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


class HuabeiPayFactory(PaymentFactory):
    def create_payment(self):
        return AliPay(use_huabei=True)


class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


# client
l1 = HuabeiPayFactory()
p1 = l1.create_payment()
p1.pay(100)

l2 = BankPayFactory()
p2 = l2.create_payment()
p2.pay(300)
