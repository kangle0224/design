#!/usr/bin/env python
# coding: utf-8

from external import Synthesizer, Human

"""
适配器应该满族开放/封闭原则
适配器可以由子类来实现，但是适配器技术是一种很好的方案
可参考grok和traits来熟悉适配器模式
"""

class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "the {} computer".format(self.name)

    def execute(self):
        return "executes a program"


class Apapter:
    """
    obj：想要适配的对象
    adapted_methods：键是客户端要调用的方法，值是应该被调用的方法
    """

    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer("Asus")]
    synth = Synthesizer("moog")
    # 下面的name是书中对应题目的答案
    objects.append(Apapter(synth, dict(execute=synth.play, name=synth.name)))
    human = Human("Bob")
    objects.append(Apapter(human, dict(execute=human.speak, name=human.name)))

    for i in objects:
        print("{} {}".format(str(i), i.execute()))
        print(i.name)


if __name__ == "__main__":
    main()
