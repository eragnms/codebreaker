#!/usr/bin/env python3

from random import randrange

def main():
    all_pins = [Pin("red"), Pin("green"), Pin("yellow"), Pin("orange"), Pin("blue"), Pin("purple")]
    for n in range(4):
        index = randrange(len(all_pins))
        pin = all_pins[index]
        print(pin.color)



class Pin:

    def __init__(self, color):
        self.color = color


if __name__ == "__main__":
    main()
