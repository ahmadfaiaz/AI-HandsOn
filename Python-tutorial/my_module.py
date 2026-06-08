
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# module can contain executable statment and func definition. statements are executed 
# only the first time the module name is encountered in an import statement

print("hey I am out side the main module lol")

if __name__ == '__main__':
    print(__name__)
    print(__spec__)