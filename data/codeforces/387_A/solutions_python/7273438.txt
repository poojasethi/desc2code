#!/usr/bin/env python

gio, phut = map(int, raw_input().split(":"))
h, m  = map(int, raw_input().split(":"))

g = gio - h
p = phut - m
if p < 0:
    p += 60
    g -= 1
if g < 0:
    g += 24

print "%02d:%02d" % (g, p)
