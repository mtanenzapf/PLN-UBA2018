from collections import defaultdict
import random


class NGramGenerator(object):

    def __init__(self, model):
        """
        model -- n-gram model.
        """
        self._n = model._n

        # compute the probabilities
        probs = defaultdict(dict)
        for ngram, count in model._count.items():
            if len(ngram) == self._n:
                probs[ngram[:-1]][ngram[-1]] = count / model._count[ngram[:-1]]
        self._probs = probs

        # sort in descending order for efficient sampling
        my_sorted = lambda xs: sorted(xs, key=lambda x: (-x[1], x[0]))
        self._sorted_probs = sorted_probs = {}
        for prev_tokens, prob_dict in probs.items():
            sorted_probs[prev_tokens] = my_sorted(prob_dict.items())

    def generate_sent(self):
        """Randomly generate a sentence."""
        n = self._n

        sent = []
        prev_tokens = ['<s>'] * (n - 1)
        token = self.generate_token(tuple(prev_tokens))
        while token != '</s>':
            # WORK HERE!!
            pass

        return sent

    def generate_token(self, prev_tokens=None):
        """Randomly generate a token, given prev_tokens.

        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self._n
        if not prev_tokens:
            prev_tokens = ()
        assert len(prev_tokens) == n - 1

        r = random.random()
        probs = self._sorted_probs[prev_tokens]
        # WORK HERE!!

        return token
