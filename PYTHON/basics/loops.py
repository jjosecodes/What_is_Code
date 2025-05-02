import math



# while 
class different_loops:
    def WhileLoop(self ,counter: int = 1 ):

        while counter <= 10:
            print("hello world ", counter)
            counter = counter + 1

    def ForLoop(self, n :int = 1):
        print(f'n = {n}')
        for item in range(n):
            print(item **2 , "is the square of", item)

    def ForLetters(self):
        word_list = ["cat", "dog", "rabbit" ]
        letter_list = []
        for a_word in word_list:
            for a_letter in a_word:
                letter_list.append(a_letter)
        print(letter_list)

# selection statements
# if else lol
    def IfElse(self,n: int = 16):
        if n < 0:
            print(" value is negative loser , try again ")
        else:
            print(math.sqrt(n))

# -------------------------- #
# list comprehension 
    def ListComprehension(self, v1 = 1, v2 =  11):
        sq_list = [x * x for x in range (v1, v2) if x % 2 == 0]
        print(sq_list)



# ------------run loops------------ #
loop = different_loops()
loop.WhileLoop(4)
loop.ForLoop(5)
loop.IfElse()
loop.ForLetters()
loop.ListComprehension(1, 11)
