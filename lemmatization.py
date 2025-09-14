import pymorphy3
import spacy
from nltk.stem import PorterStemmer, SnowballStemmer


def lemmatization_ru(words: list[str]) -> list[str]:
    """
    Lemmatize Russian words using pymorphy3.

    Parameters
    ----------
    words : list[str]
        List of Russian words to lemmatize.

    Returns
    -------
    list[str]
        List of base forms (lemmas) for the input words.

    """
    base_forms = []
    morph = pymorphy3.MorphAnalyzer()
    for word in words:
        base_forms.append(morph.parse(word)[0].normal_form)

    return base_forms


def lemmatization_en(words: list[str]) -> list[str]:
    """
    Lemmatize English words using spaCy.

    Parameters
    ----------
    words : list[str]
        List of English words to lemmatize.

    Returns
    -------
    list[str]
        List of base forms (lemmas) for the input words.

    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(" ".join(words))
    base_forms = [token.lemma_ for token in doc]

    return base_forms


def lemmatization_porter_stemmer(words: list[str], lang: str) -> list[str]:
    """
    Stem words using Porter/Snowball stemmer algorithms.

    Parameters
    ----------
    words : list[str]
        List of words to stem.
    lang : str
        Language of the words ('en' for English, 'ru' for Russian).

    Returns
    -------
    list[str]
        List of stemmed forms of the input words.

    """
    if lang == "en":
        porter = PorterStemmer()
    elif lang == "ru":
        porter = SnowballStemmer("russian")
    else:
        print("Language not supported. Empty list returned.")
        return []

    base_forms = []
    for word in words:
        stem = porter.stem(word)
        base_forms.append(stem)

    return base_forms


def test():
    """
    Test function to compare lemmatization and stemming results.
    Creates sample word lists in English and Russian, processes them
    using different methods, and displays the results in a formatted table.
    """
    english_words = [
        "running",
        "jumped",
        "better",
        "happiest",
        "studies",
        "mice",
        "was",
        "are",
    ]
    russian_words = [
        "бежавший",
        "стоял",
        "лучше",
        "счастливейший",
        "учусь",
        "мыши",
        "был",
        "есть",
    ]

    print("\nEnglish words:")
    print("-" * 70)
    print(f"{'word':<22} {'spacy':<22} {'PorterStemmer':<22}")
    print("-" * 70)

    en_lemmas = lemmatization_en(english_words)
    en_stems = lemmatization_porter_stemmer(english_words, "en")

    for i, word in enumerate(english_words):
        print(f"{word:<22} {en_lemmas[i]:<22} {en_stems[i]:<22}")

    print("\nRussian words:")
    print("-" * 70)
    print(f"{'word':<22} {'pymorphy3':<22} {'SnowballStemmer':<22}")
    print("-" * 70)

    ru_lemmas = lemmatization_ru(russian_words)
    ru_stems = lemmatization_porter_stemmer(russian_words, "ru")

    for i, word in enumerate(russian_words):
        print(f"{word:<22} {ru_lemmas[i]:<22} {ru_stems[i]:<22}")


if __name__ == "__main__":
    test()
