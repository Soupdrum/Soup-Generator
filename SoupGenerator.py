import csv
import random
from typing import List
from pathlib import Path
from PIL import Image as PILImage
import numpy as np


def fix_text(text: str) -> str:
    """
    Formats text by removing specific unwanted characters.
    
    Args:
        text (str): The input text to format.
    
    Returns:
        str: The formatted text.
    """
    return text.replace("'", "").replace("\\[", "").replace("\\]", "")


def cap_text(text: str) -> str:
    """
    Formats and capitalizes the text.
    
    Args:
        text (str): The input text to capitalize.
    
    Returns:
        str: The formatted and capitalized text.
    """
    return fix_text(text).capitalize()


class LibraryLoader:
    """
    Loads and caches word libraries from CSV files.
    """
    _cache: dict = {}

    @staticmethod
    def load_lib(filename: str) -> List[str]:
        """
        Loads a list of words from a CSV file located in the 'libs' directory.
        
        Args:
            filename (str): The name of the CSV file without extension.
        
        Returns:
            List[str]: A list of words.
        
        Raises:
            FileNotFoundError: If the CSV file does not exist.
        """
        if filename in LibraryLoader._cache:
            return LibraryLoader._cache[filename]
        
        path = Path('libs') / f'{filename}.csv'
        if not path.exists():
            raise FileNotFoundError(f"Library file '{path}' not found.")
        
        with path.open(newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            lib = [fix_text(word.strip()) for row in reader for word in row if word.strip()]
        
        LibraryLoader._cache[filename] = lib
        return lib


class TextGenerator:
    """
    Generates various types of text elements such as numbers, nouns, adjectives, etc.
    """

    def number(self, length: int) -> str:
        """
        Generates a string of random numbers.
        
        Args:
            length (int): The number of digits to generate.
        
        Returns:
            str: A string of random digits.
        """
        return ''.join(str(random.randint(0, 9)) for _ in range(length))

    def noun(self, length: int) -> str:
        """
        Generates a string of random nouns.
        
        Args:
            length (int): The number of nouns to generate.
        
        Returns:
            str: A string of random nouns separated by spaces.
        """
        nouns = LibraryLoader.load_lib("nouns")
        return fix_text(" ".join(random.choice(nouns).lower() for _ in range(length)))

    def adjective(self, length: int) -> str:
        """
        Generates a string of random adjectives.
        
        Args:
            length (int): The number of adjectives to generate.
        
        Returns:
            str: A string of random adjectives separated by spaces.
        """
        adjectives = LibraryLoader.load_lib("adjectives")
        return fix_text(" ".join(random.choice(adjectives).lower() for _ in range(length)))

    def adverb(self, length: int) -> str:
        """
        Generates a string of random adverbs.
        
        Args:
            length (int): The number of adverbs to generate.
        
        Returns:
            str: A string of random adverbs separated by spaces.
        """
        adverbs = LibraryLoader.load_lib("adverbs")
        return fix_text(" ".join(random.choice(adverbs).lower() for _ in range(length)))

    def verb(self, length: int) -> str:
        """
        Generates a string of random verbs.
        
        Args:
            length (int): The number of verbs to generate.
        
        Returns:
            str: A string of random verbs separated by spaces.
        """
        verbs = LibraryLoader.load_lib("verbs")
        return fix_text(" ".join(random.choice(verbs).lower() for _ in range(length)))

    def alphabet(self, length: int) -> str:
        """
        Generates a string of random alphabet characters.
        
        Args:
            length (int): The number of letters to generate.
        
        Returns:
            str: A string of random letters separated by spaces.
        """
        alphabets = LibraryLoader.load_lib("alphabet")
        return fix_text(" ".join(random.choice(alphabets).lower() for _ in range(length)))

    def alphanumeric(self, length: int) -> str:
        """
        Generates a string of random alphanumeric characters.
        
        Args:
            length (int): The number of characters to generate.
        
        Returns:
            str: A string of random alphanumeric characters.
        """
        alphanumerics = LibraryLoader.load_lib("alphabet") + [str(i) for i in range(10)]
        return fix_text("".join(random.choice(alphanumerics) for _ in range(length)))

    def word(self, length: int) -> str:
        """
        Generates a string of mixed words (adjectives, adverbs, nouns, verbs).
        
        Args:
            length (int): The number of words to generate.
        
        Returns:
            str: A capitalized string of mixed words ending with a period.
        """
        adjectives = LibraryLoader.load_lib("adjectives")
        adverbs = LibraryLoader.load_lib("adverbs")
        nouns = LibraryLoader.load_lib("nouns")
        verbs = LibraryLoader.load_lib("verbs")
        words = adjectives + adverbs + nouns + verbs
        return cap_text(" ".join(random.choice(words) for _ in range(length)) + ".")


class PhraseGenerator:
    """
    Generates predefined phrase structures such as Noam, similes, and clichés.
    """

    def noam(self) -> str:
        """
        Generates a Noam-like phrase with adjectives, nouns, verbs, and adverbs.
        
        Returns:
            str: A formatted Noam phrase.
        """
        adjectives = LibraryLoader.load_lib("adjectives")
        adverbs = LibraryLoader.load_lib("adverbs")
        nouns = LibraryLoader.load_lib("nouns")
        verbs = LibraryLoader.load_lib("verbs")
        val = f'{random.choice(adjectives)} {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)}s {random.choice(adverbs)}.'
        return cap_text(val)

    def simile(self) -> str:
        """
        Generates a simile phrase.
        
        Returns:
            str: A formatted simile sentence.
        """
        adjectives = LibraryLoader.load_lib("adjectives")
        nouns = LibraryLoader.load_lib("nouns")
        val = f'He was as {random.choice(adjectives)} as a {random.choice(nouns)}.'
        return cap_text(val)

    def cliche(self) -> str:
        """
        Generates a cliché phrase.
        
        Returns:
            str: A formatted cliché sentence.
        """
        adverbs = LibraryLoader.load_lib("adverbs")
        verbs = LibraryLoader.load_lib("verbs")
        val = f'It\'s not rocket science, just {random.choice(adverbs)} {random.choice(verbs)} it.'
        return cap_text(val)


class SoupImage:
    """
    Generates random grayscale images.
    """

    def __init__(self, width: int, height: int, path: str):
        """
        Initializes the SoupImage with dimensions and saves a random grayscale image.
        
        Args:
            width (int): The width of the image.
            height (int): The height of the image.
            path (str): The file path to save the image.
        """
        self.width = width
        self.height = height
        self.path = Path(path)
        self.pixels = np.random.randint(0, 256, size=(self.height, self.width), dtype=np.uint8)
        img = PILImage.fromarray(self.pixels, 'L')
        img.save(self.path)
        print(f"Grayscale image saved to {self.path}")

    def show(self):
        """
        Displays the generated image.
        """
        img = PILImage.fromarray(self.pixels, 'L')
        img.show()


class SoupImageRGB:
    """
    Generates random RGB images.
    """

    def __init__(self, width: int, height: int, path: str):
        """
        Initializes the SoupImageRGB with dimensions and saves a random RGB image.
        
        Args:
            width (int): The width of the image.
            height (int): The height of the image.
            path (str): The file path to save the image.
        """
        self.width = width
        self.height = height
        self.path = Path(path)
        self.pixels = np.random.randint(0, 256, size=(self.height, self.width, 3), dtype=np.uint8)
        img = PILImage.fromarray(self.pixels, 'RGB')
        img.save(self.path)
        print(f"RGB image saved to {self.path}")

    def show(self):
        """
        Displays the generated RGB image.
        """
        img = PILImage.fromarray(self.pixels, 'RGB')
        img.show()


class AudioGenerator:
    """
    Placeholder for audio generation functionalities.
    """
    
    def wav(self, duration: float = 1.0, freq: float = 440.0, path: str = "output.wav"):
        """
        Generates a simple WAV file with a sine wave.
        
        Args:
            duration (float): Duration of the audio in seconds.
            freq (float): Frequency of the sine wave.
            path (str): File path to save the WAV file.
        """
        import wave
        import struct

        sample_rate = 44100
        amplitude = 32767
        n_samples = int(sample_rate * duration)
        with wave.open(path, 'w') as wav_file:
            wav_file.setparams((1, 2, sample_rate, n_samples, 'NONE', 'not compressed'))
            for i in range(n_samples):
                value = int(amplitude * np.sin(2 * np.pi * freq * (i / sample_rate)))
                data = struct.pack('<h', value)
                wav_file.writeframesraw(data)
        print(f"WAV audio saved to {path}")
