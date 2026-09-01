# 📝 NLP Experiments

A collection of hands-on **Natural Language Processing (NLP) experiments** focused on understanding fundamental text preprocessing and linguistic analysis techniques using Python.

This repository documents my learning journey through practical implementations of core NLP concepts such as **tokenization, stop-word removal, stemming, lemmatization, and Part-of-Speech analysis**.

---

## 📚 Experiments Covered

### 1. Python Input Validation

Basic experiments with:

* Integer input validation
* Exception handling using `try-except`
* Input validation using `isdigit()`
* Password length validation

---

### 2. Tokenization & Stop Word Removal

Experimenting with text preprocessing using **NLTK**.

Topics covered:

* Word Tokenization
* Sentence Tokenization
* Stop Word Removal
* Filtering unnecessary words from text

Example:

```text
Input:
Hi, This is Shashikala Gupta. I am a Data Science Student.

After Stop Word Removal:
Hi, This, Shashikala, Gupta, Data, Science, Student
```

---

### 3. Stemming

Exploring the **Porter Stemmer** to reduce words to their root/stem form.

Example:

```text
engine       → engin
engineer     → engin
engineering → engin
engineered   → engin
```

The experiment also applies stemming to words extracted from sentences.

---

### 4. Lemmatization

Using **WordNetLemmatizer** to convert words into their meaningful base forms.

Examples:

```text
rocks   → rock
corpora → corpus
better  → good
```

The experiment also demonstrates how **Part-of-Speech information** can improve lemmatization.

---

### 5. Linguistic Analysis with Stanza

The repository also includes an experiment using **Stanza**, an NLP library for linguistic analysis.

The experiment performs:

* Tokenization
* Lemmatization
* Universal Part-of-Speech (UPOS) tagging
* Morphological feature extraction

Example:

```text
Word: playing
Lemma: play
POS: VERB
```

---

## 🗂️ Repository Structure

```text
NLP-Experiments/
│
├── experiment01.ipynb
├── exp02.ipynb
├── exp03.ipynb
├── exp04.ipynb
├── exp05.py
├── exp05-output.png
│
└── README.md
```

---

## 🛠️ Technologies & Libraries

* 🐍 Python
* 📓 Jupyter Notebook
* 🔤 NLTK
* 🧠 Stanza

---

## 🔄 NLP Preprocessing Pipeline

The experiments demonstrate the basic workflow commonly used when working with text:

```text
Raw Text
   ↓
Tokenization
   ↓
Stop Word Removal
   ↓
Stemming / Lemmatization
   ↓
Linguistic Analysis
   ↓
Processed Text
```

---

## 🎯 Learning Objectives

Through these experiments, I am building an understanding of:

* How computers process human language
* Breaking text into sentences and words
* Removing unnecessary words
* Reducing words to their stems
* Finding meaningful base forms of words
* Understanding Part-of-Speech tags
* Extracting morphological features
* Using NLP libraries for linguistic analysis

---

## 🚀 Future Experiments

More NLP experiments will be added as I continue learning, including:

* Bag of Words
* TF-IDF
* N-Grams
* Word Embeddings
* Word2Vec
* Cosine Similarity
* Text Classification
* Sentiment Analysis
* Named Entity Recognition
* NLP Pipelines
* Recurrent Neural Networks
* Transformers
* Large Language Models

---

## 👩‍💻 Author

**Shashikala Gupta**

GitHub: [Shashikala-11](https://github.com/Shashikala-11)

---

⭐ This repository is part of my hands-on learning journey in **Natural Language Processing and Machine Learning**.
