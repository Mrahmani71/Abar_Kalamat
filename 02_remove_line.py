# coding=UTF-8

with open('data/tweets.csv', 'r') as infile,\
        open('data/twline.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace("\n", " ").replace(
        '"', " ").replace("'", " ").replace("    ", " ").replace("ي","ی").replace("ك","ک")
    outfile.write("")
    outfile.write(data)
