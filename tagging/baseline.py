from collections import defaultdict


class BadBaselineTagger:

    def __init__(self, tagged_sents):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        """
        pass

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """
        return 'nc0s000'

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return True


class BaselineTagger:

    def __init__(self, tagged_sents):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        """
        word_tags = defaultdict(dict)

        for sent in tagged_sents:
            for word, tag in set:
                word_tags[word][tag] = word_tags.get(word, {}).get(tag, 0) + 1

        self._word_tags = word_tags

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """
        # WORK HERE!!

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        # WORK HERE!!
