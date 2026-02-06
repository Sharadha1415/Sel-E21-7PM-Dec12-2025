class Numbers:

    def even_odd(self, start, end):
        for num in range(start, end):
            if num%2==0:
                print(f"{num} is even")
            else:
                print(f"{num} is odd")

    def prime_numbers(self):
        for i in range(2, 50):
            for j in range(2, i):
                if i%j==0:
                    break
            else:
                print(i)


num = Numbers()
num.even_odd(10, 20)
num.prime_numbers()






























