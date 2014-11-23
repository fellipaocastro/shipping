#!/usr/bin/env python
# coding: utf-8


def main():
    try:
        n = int(raw_input('Entre com um número inteiro: '))
        print n
    except ValueError:
        print 'Somente números inteiros são aceitos!'
        main()

if __name__ == '__main__':
    main()
