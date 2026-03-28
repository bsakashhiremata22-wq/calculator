def my_find(haystack, needle):
    for letter in haystack:
        if letter == needle:
            print(f"The letter '{needle}' is found")
            return
    print(f"The letter '{needle}' is not found")

my_find("hello", "h")