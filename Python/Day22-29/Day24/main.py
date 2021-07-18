with open("C:/Users/bucal/Desktop/test.txt", mode="a") as file:
    # you don't need to call close() if you use "with" keyword
    # r = read
    # w = write, will create the file if it doesn't exist, remove the contents of the file if it does exist
    # r+ = read and write
    # a = append
    # default = r
    file.write(" is very handsome")

with open("C:/Users/bucal/Desktop/test.txt", mode="r") as file:
    my_string_2 = file.read()
    print(my_string_2)
