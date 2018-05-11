from random import choice
marks = map(chr, range(768, 879))
string = 'clear the current exception in between your catch and the bare raise OH GOD NO EVENTLET IT COMES'
words = string.split()
print(' '.join(''.join(c + ''.join(choice(marks)
                                   for _ in range(i // 2 + 1)
                                   ) * c.isalnum()
                       for c in word)
               for i, word in enumerate(words)))
