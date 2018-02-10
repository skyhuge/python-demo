#! /usr/bin/env python3

age = input('please enter your age :')
content = int(age)
if content > 18:
    print('hello ,', content)
elif content > 30:
    print('so, who are you')
else:
    print('old')        