import twint

with open('data/tweets.csv', 'w+') as outfile:
    outfile.write(" ")
print('file tweets.csv khali shod')
c = twint.Config()
c.Username = "mabbaszadegan"
c.Limit = 4500
c.Search = ""
c.Store_csv = True
c.Output = "data"
twint.run.Search(c)
