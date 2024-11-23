
# Spam Detection Using NLP and Machine Learning

This project focuses on building a spam detection model using Natural Language Processing (NLP) techniques and machine learning. It processes and analyzes text data to classify messages as **Spam** or **Ham** (Not Spam).

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Project Structure](#project-structure)
7. [License](#license)
8. [Contact](#contact)

---

## Overview

Spam messages are a persistent problem in digital communication. This project uses a labeled dataset of text messages to train a machine learning model that can differentiate between legitimate and spam messages. The model is designed with the following capabilities:

- Text preprocessing (e.g., tokenization, stopword removal).
- Feature extraction (e.g., word count, sentence count, character count).
- Classification using algorithms like Logistic Regression.

---

## Features

- **Preprocessing**:
  - Tokenization of sentences and words.
  - Removal of stopwords and punctuation.
- **Feature Engineering**:
  - Calculates word count, sentence count, and character count.
  - Supports additional features like TF-IDF or bag-of-words.
- **Machine Learning**:
  - Trains models using `scikit-learn`.
  - Evaluates performance with metrics like accuracy, precision, recall, and F1-score.
- **Visualization**:
  - Plots data distributions and model performance metrics.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Himansh9532/spam-detection.git
   cd spam-detection
   ```

2. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download NLTK resources:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

---

## Usage

1. Add your dataset (e.g., `spam.csv`) to the `data/` folder.
2. Run the main script:
   ```bash
   python main.py
   ```
3. For experimentation, use the Jupyter Notebook:
   ```bash
   jupyter notebook notebooks/analysis.ipynb
   ```

---

## Technologies Used

- **Programming Language**: Python 3.x
- **Libraries**:
  - `pandas` - Data manipulation and analysis.
  - `nltk` - Text processing and tokenization.
  - `scikit-learn` - Machine learning algorithms.
  - `matplotlib` - Data visualization.
- **Tools**:
  - Jupyter Notebook for experimentation.
  - Git for version control.

---

## Project Structure

```
├── data/
│   └── spam.csv                # Dataset
├── notebooks/
│   └── analysis.ipynb          # Jupyter Notebook for exploration
├── src/
│   ├── preprocess.py           # Preprocessing functions
│   ├── features.py             # Feature engineering
│   ├── model.py                # Model training and evaluation
├── main.py                     # Main script
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
```

---


---
## Visualization

Below is a word cloud visualization of the dataset:

![Word Cloud](images/wordcloud_target1.png)


## Contact

For any questions, feel free to reach out:

- **Name:** Himanshu Gupta  
- **Email:** 2022blaiml03@axiscoleges.in  
- **GitHub:** [Himansh9532](https://github.com/Himansh9532)  
- **LinkedIn:** [Himanshu Gupta](https://linkedin.com/in/HimanshuGupta)  

---
