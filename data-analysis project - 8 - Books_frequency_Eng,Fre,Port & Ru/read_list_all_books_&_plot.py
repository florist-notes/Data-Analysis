import os
import pandas as pd

book_dir = "./Books"
os.listdir(book_dir)

stats=pd.DataFrame(columns=("language","author","title","length","unique"))
title_num=1
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir+"/"+language):
        for title in os.listdir(book_dir+"/"+language+"/"+author):
            inputfile=book_dir+"/"+language+"/"+author+"/"+title
            print(inputfile)
            text=read_book(inputfile)
            (num_unique,counts) = word_stats(count_words_fast(text))
            stats.loc[title_num]=language,author.capitalize(),title.replace(".txt",""),sum(counts), num_unique
            title_num+=1
stats
# >>>stats.head() #top 5 rows
# >>>stats.tail() #bottom 5 rows
# >>>stats.columname ---> gives the column
import matplotlib.pyplot as plt
plt.plot(stats.length,stats.unique,"bo-")

plt.loglog(stats.length,stats.unique,"ro")

stats[stats.language=="English"]

plt.figure(figsize=(10,10))
subset=stats[stats.language=="English"]
plt.loglog(subset.length,subset.unique,"o",label="English",color="crimson")
subset=stats[stats.language=="French"]
plt.loglog(subset.length,subset.unique,"o",label="French",color="forestgreen")
subset=stats[stats.language=="German"]
plt.loglog(subset.length,subset.unique,"o",label="German",color="orange")
subset=stats[stats.language=="Portuguese"]
plt.loglog(subset.length,subset.unique,"o",label="Portuguese", color="blueviolet")
plt.legend()
plt.xlabel("Book Length")
plt.ylabel("NUmber of Unique words")
plt.savefig("we.pdf")
plt.show()
