# import tkinter as tk

# root = tk.Tk()
# root.title("Sandbox")
# root.geometry("400x300")

# my_canvas = tk.Canvas(root, width=200, height=200, background="blue")
# my_canvas.pack(padx=50, pady=25)

# my_canvas.create_rectangle(10, 10, 80, 80, fill="yellow")
# my_canvas.create_line(90, 90, 150, 90, fill="red")
# my_canvas.create_text(
#     100, 100, text="Desenhando", font=("Arial", 18, "bold"), fill="white"
# )

# root.mainloop()

# Learning Dictionary - count word frequency in a text
corpus = "learn all about python and its potential \
    you would also learn to create word frequency and all tests python is \
        can do with and about cesar"
word_freq = dict()
corpus_word = str(corpus).split()
for word in range(len(corpus_word)):
    if corpus_word[word] not in word_freq:
        word_freq[corpus_word[word]] = 1
    else:
        word_freq[corpus_word[word]] += 1
print(word_freq)
