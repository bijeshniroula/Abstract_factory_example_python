#!/usr/bin/python
# -*- coding : utf-8 -*-
"""
    @author: Diogenes Augusto Fernandes Herminio <diofeher@gmail.com>
"""

from abc import ABCMeta

#Abstract Factory
class StandardFactory(object):

    @staticmethod
    def get_factory(factory):
        if factory == 'Lampard':
            return LiverpoolFactory()
        elif factory == 'Gerrard':
            return ChelseaFactory()
        raise TypeError('Unknown Factory.')


#Factory
class LiverpoolFactory(object):
    def get_ball(self):
        return Liverpool();


class ChelseaFactory(object):
    def get_ball(self):
        return Chelsea();


# Product Interface
class Ball(object):
    __metaclass__ = ABCMeta
    def play(self):
        pass


# Products
class Liverpool(object):
    def play(self):
            return 'Gerrard played for Liverpool!!'


class Chelsea(object):
    def play(self):
        return 'Lampard played for Chelsea!'


if __name__ =="__main__":
    factory = StandardFactory.get_factory('Lampard')
    ball = factory.get_ball()
    print ball.play()

    factory = StandardFactory.get_factory('Gerrard')
    ball = factory.get_ball()
    print ball.play()
