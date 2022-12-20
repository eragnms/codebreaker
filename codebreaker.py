#!/usr/bin/env python3

def main():
    one_pin = Pin("red")
    print(one_pin.color)


class Pin:

    def __init__(self, color):
        self.color = color


if __name__ == "__main__":
    main()
