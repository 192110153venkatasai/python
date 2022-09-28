import re
text = "this is great thanks very much"
def foo(txt):
    max_count=0
    for i in re.split('[!.?]',txt):
        if len(i.split()) > max_count:
            max_count = len(i.split())
    return max_count

print(foo(text))
