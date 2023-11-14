# Create a function called start_playing which will receive an instance and will return its play() method.
#
# Test code1:
# class Guitar:
#     def play(self):
#         return "Playing the guitar"
#
# guitar = Guitar()
# print(start_playing(guitar))
#
# Output1:
# Playing the guitar
#
# Test code2:
# class Children:
#     def play(self):
#         return "Children are playing"
#
# children = Children()
# print(start_playing(children))
#
# Output2:
# Children are playing

class Guitar:
    def play(self):
        return "Playing the guitar"


def start_playing(self):
    return self.play()


guitar = Guitar()
print(start_playing(guitar))


class Children:
    def play(self):
        return "Children are playing"


def start_playing(obj):
    return obj.play()


children = Children()
print(start_playing(children))
