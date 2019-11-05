def count_words(filename):
    # count an file included how mang word
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file {0} does not exist.".format(filename)
        print(msg)
    else:
        # count the file included about how many word
        words = contents.split()
        num_words = len(words)
        print("The file {0} has about {1} words".format(filename, str(num_words)))


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
