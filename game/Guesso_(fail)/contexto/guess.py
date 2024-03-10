import os
import random
from typing import Tuple, List

import numpy as np
from sklearn.metrics.pairwise import cosine_distances

from contexto.config import DATA_DIR


class Finder:
    def __init__(self):
        embeddings_path = os.path.join(DATA_DIR, 'words_embeddings.npy')
        words_path = os.path.join(DATA_DIR, 'words_filtered.txt')
        self.embeddings = np.load(embeddings_path)
        self.words = list(map(str.strip, open(words_path).readlines()))

        self.results = [
            # (word, order)
        ]

        self.word_to_distances = {}

    def get_distances(self, word: str):
        try:
            word_id = self.words.index(word)
        except ValueError:
            return None
        return cosine_distances([self.embeddings[word_id]], self.embeddings)[0]

    def find_closest(self, word_id: int, mask=None, top=10):  # Not used
        if mask is None:
            mask = np.array([True] * len(self.words))

        mask[word_id] = False
        ids = np.arange(len(self.words))[mask]

        masked_words_embeddings = self.embeddings[mask]

        masked_top = np.argsort(cosine_distances(
            [self.embeddings[word_id]], masked_words_embeddings))[0][:top + 1]

        real_top = ids[masked_top]

        return real_top

    def get_word_to_distances(self, guesses: List[Tuple[str, int]]):
        word_to_distances = {}

        for word, _ in guesses:
            dists = self.get_distances(word)
            if dists is not None:
                word_to_distances[word] = dists

        return word_to_distances

    def add_result(self, word, order):
        self.results.append((word, order))
        self.word_to_distances[word] = self.get_distances(word)

    def get_score(self, guesses, word_to_distances, min_gap=0.1, num_samples=50):
        scores = np.zeros(len(self.words))

        for _ in range(0, num_samples):

            word_a, order_a = random.choice(guesses)
            word_b, order_b = random.choice(guesses)

            if order_a < order_b * (1.0 - min_gap):
                scores += (word_to_distances[word_a] -
                           word_to_distances[word_b] < 0)

            if order_a > order_b * (1.0 + min_gap):
                scores += (word_to_distances[word_a] -
                           word_to_distances[word_b] > 0)

        return scores

    def best_scores(self, guesses, word_to_distances, top: int):
        """ Returns a mask of the top scores of the best guess
        """
        best_guess_word, best_guess_rank = sorted(
            guesses, key=lambda x: x[1])[0]
        best_guess_distances = word_to_distances[best_guess_word]
        top_distances = np.argsort(best_guess_distances)[:top]
        top_distances_mask = np.zeros(len(self.words), dtype=bool)
        top_distances_mask[top_distances] = True
        return top_distances_mask

    def already_guessed_mask(self, guesses):
        already_guessed_mask = np.zeros(len(self.words), dtype=bool)
        for word, _ in guesses:
            word_id = self.words.index(word)
            already_guessed_mask[word_id] = True
        return already_guessed_mask

    def sample_score(self, min_gap=0.1, num_samples=50, guesses=None, word_to_distances=None):
        if guesses is None:
            guesses = self.results

        if word_to_distances is None:
            word_to_distances = self.word_to_distances

        guesses = [
            (word, order)
            for word, order in guesses
            if word in word_to_distances
        ]

        scores = self.get_score(
            guesses, word_to_distances, min_gap=min_gap, num_samples=num_samples)

        already_guessed_masked = self.already_guessed_mask(guesses)
        scores[already_guessed_masked] = 0

        best_scores_masked = self.best_scores(
            guesses, word_to_distances, top=100)
        scores[~best_scores_masked] = 0

        top_score = max(scores)
        # top_score = np.percentile(scores, 90)

        while True:
            mask = scores >= top_score

            for word, _ in guesses:
                word_id = self.words.index(word)
                mask[word_id] = False

            closest_ids = np.arange(len(self.words))[mask]
            if len(closest_ids) > 0:
                break
            else:
                top_score -= 1

        return closest_ids

    def guess_next(self, guesses=None, word_to_distances=None):
        closest = self.sample_score(
            min_gap=0.3, num_samples=500, guesses=guesses, word_to_distances=word_to_distances)
        return self.words[closest[random.randint(0, closest.size-1)]]


if __name__ == '__main__':
    results = [
    ]

    finder = Finder()

    # ctrl+c handler:
    import signal
    import sys

    def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        print('Results:')
        print(finder.results)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    for word, order in results:
        finder.add_result(word, order)

    if len(finder.results) == 0:
        word = input('Word: ')
        order = int(input('Order: '))
        finder.add_result(word, order)

    while True:
        next_word = finder.guess_next()
        print(next_word)
        try:
            order = int(input('Order: '))
            if order == 0:
                order = None
        except ValueError as e:
            print('Invalid order')
            continue

        finder.add_result(next_word, order)
