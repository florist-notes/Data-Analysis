def read_book(title_path):
    #read a book and return it as a string
    with open(title_path,"r", encoding="utf8") as current_file:
        text=current_file.read()
        text=text.replace("\n", "").replace("\r","")
    return text

text = read_book("./Books/English/shakespeare/Romeo and Juliet.txt")

# >>>p=text.find("What's in a name?")
# >>>sp=text[p:p+1000]

def word_stats(word_counts):
    num_unique=len(word_counts)
    counts=word_counts.values()
    return (num_unique,counts)

word_counts = count_words_fast(text)          #algorithm from previous program
(num_unique,counts) = word_stats(word_counts)
print(num_unique,sum(counts))      #For English Version

text=read_book("./German/shakespeare/Romeo und Julia.txt")
word_counts=count_words_fast(text)
(num_unique,counts)=word_stats(word_counts)
print(num_unique,sum(counts))      #For German Version
