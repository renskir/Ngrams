# Ngrams

Bart Berbers (4262149) b.o.berbers@students.uu.nl\
Sweder Geleijns (1021790) s.w.j.geleijns@students.uu.nl \
Rens Kirchner (6791506) h.l.kirchner@students.uu.nl \
\
The purpose of this project is to generated new sentences based on a bigram model,
which was constructed based on the training corpus. \
\
Files
- corpusreader.py
- generate_text.py
- model.py

The corpusreader.py script opens a .txt file and tokenizes the words in it. 
The generate_text.py script constructs a bigram model, 
generates two paragraphs of five random sentences 
and calculates the perplexity of a few test sentences.
The model.py script defines the bigram model, 
which constructs bigrams from a given corpus, 
computes P_r(w_n | w) and smoothed P_r(w_n | w), 
returns possible next tokens, given a particular token
and calculates perplexity of a given sentence.