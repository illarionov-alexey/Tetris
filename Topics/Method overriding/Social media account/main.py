class Account:
    def __init__(self, media, username, n_followers):
        self.media = media
        self.username = username
        self.n_followers = n_followers
        print("Account")


# create the class here
class InstagramAccount(Account):
    def __init__(self,username,n_followers,n_following):
        super().__init__("Instagram",username,n_followers)
        self.n_following = n_following

def foo(numbers):
    counter1 = 0
    counter2 = 0

    for num in numbers:
        if num % 2 == 0:
            counter1 += num if num < 4 else -num
        else:
            counter2 += num if num < 5 else -num

    return counter1 * counter2

print(foo([3, 4, 2, 1, 5, 7]))