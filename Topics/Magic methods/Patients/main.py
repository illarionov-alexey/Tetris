class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # create methods here
    def __repr__(self):
        return f"Object of the class Patient. name: {self.name}, last_name: {self.last_name}, age: {self.age}"

    def __str__(self):
        return f"{self.name} {self.last_name}. {self.age}"


def funk(n):
    a = 1
    b = 1
    x = 0
    for j in range(2,n):
        x = a + b
        a = b
        b = x
    return x

funk(11)