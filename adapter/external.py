#!/usr/bin/env python
# coding: utf-8

class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "the {} synthesizer".format(self.name)

    def play(self):
        return "is playing an electronic song"


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "says hello"

    def speak(self):
        return "says hello"
