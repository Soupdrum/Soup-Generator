import csv
import random
from typing import List
from pathlib import Path
from PIL import Image as PILImage
import numpy as np
import wave
import datetime
import string
import re


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

    def phone(self) -> str:
        """
        Generates a random US phone number.
        
        Returns:
            str: A formatted US phone number.
        """
        area_code = random.randint(100, 999)
        central_office_code = random.randint(100, 999)
        line_number = random.randint(1000, 9999)
        return f"({area_code}) {central_office_code}-{line_number}"

    def credit_card(self) -> str:
        """
        Generates a random credit card number (for testing only!).
        
        Returns:
            str: A formatted credit card number.
        """
        prefix = random.choice(['4', '5', '37', '6'])  # Common card prefixes
        length = 16 if prefix != '37' else 15
        number = prefix + ''.join([str(random.randint(0, 9)) for _ in range(length - len(prefix))])
        return ' '.join(number[i:i+4] for i in range(0, len(number), 4))

    def url(self) -> str:
        """
        Generates a random URL.
        
        Returns:
            str: A formatted URL.
        """
        protocols = ['http', 'https']
        domains = ['example.com', 'test.com', 'demo.com']
        return f"{random.choice(protocols)}://{self.noun(1).lower()}.{random.choice(domains)}"

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

    def address(self) -> str:
        """
        Generates a random address.
        
        Returns:
            str: A formatted address.
        """
        street_types = ['St', 'Ave', 'Blvd', 'Rd', 'Lane', 'Drive']
        return f"{self.number(random.randint(1, 999))} {self.noun(1).title()} {random.choice(street_types)}"

    def company(self) -> str:
        """
        Generates a random company name.
        
        Returns:
            str: A formatted company name.
        """
        suffixes = ['Inc', 'LLC', 'Corp', 'Solutions', 'Technologies']
        return f"{self.noun(1).title()} {random.choice(suffixes)}"

    def hashtag(self, count: int = 1) -> str:
        """
        Generate trending-style hashtags
        """
        tags = []
        for _ in range(count):
            words = [self.noun(1), self.adjective(1)]
            random.shuffle(words)
            tag = ''.join(word.title() for word in ' '.join(words).split())
            tags.append(f"#{tag}")
        return ' '.join(tags)

    def emoji(self, count: int = 1) -> str:
        """
        Generate random emojis
        """
        emojis = ['😀', '😎', '🔥', '💡', '🚀', '💻', '🎮', '📱', '🎨', '🎯']
        return ''.join(random.sample(emojis, min(count, len(emojis))))
    
    def filename(self, extension: str = None) -> str:
        """
        Generate random filename
        """
        if not extension:
            extension = random.choice(['.txt', '.pdf', '.doc', '.jpg', '.png'])
        name = self.alphanumeric(8).lower()
        return f"{name}{extension}"


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


class Audio:
    """
    Generate various audio content
    dependencies: numpy
    """
    
    def wav(self, duration=1.0, sample_rate=44100, filepath=None):
        """
        Generate random WAV audio data
        duration: length in seconds
        sample_rate: samples per second
        filepath: optional path to save the WAV file
        """
        samples = int(duration * sample_rate)
        audio_data = np.random.uniform(-1, 1, samples)
        data = (audio_data * 32767).astype(np.int16)
        
        if filepath:
            with wave.open(filepath, 'wb') as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(sample_rate)
                wav_file.writeframes(data.tobytes())
        
        return data

    def tone(self, frequency=440, duration=1.0, sample_rate=44100, filepath=None):
        """
        Generate a pure tone
        frequency: in Hz
        """
        t = np.linspace(0, duration, int(sample_rate * duration))
        audio_data = np.sin(2 * np.pi * frequency * t)
        data = (audio_data * 32767).astype(np.int16)
        
        if filepath:
            with wave.open(filepath, 'wb') as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(sample_rate)
                wav_file.writeframes(data.tobytes())
        
        return data


class DataGenerator:
    """
    Generate structured data
    """
    
    def __init__(self):
        self.text = TextGenerator()
        self.phrase = PhraseGenerator()

    def person(self):
        """
        Generate random person data
        """
        return {
            "id": self.text.alphanumeric(8),
            "name": f"{self.text.noun(1).title()} {self.text.noun(1).title()}",
            "age": random.randint(18, 80),
            "email": f"{self.text.alphanumeric(8)}@example.com",
            "bio": self.phrase.noam(),
            "phone": self.text.phone(),
            "address": self.text.address()
        }

    def product(self):
        """
        Generate random product data
        """
        return {
            "id": self.text.alphanumeric(6),
            "name": f"{self.text.adjective(1)} {self.text.noun(1)}",
            "price": round(random.uniform(1.0, 999.99), 2),
            "description": self.phrase.noam(),
            "in_stock": random.choice([True, False]),
            "company": self.text.company()
        }


class SoupPattern(SoupImageRGB):
    """
    Generate patterned images
    """
    
    def __init__(self, width, height, path, pattern_type='checker'):
        self.width = width
        self.height = height
        self.path = path
        
        if pattern_type == 'checker':
            self.pixels = self._checker_pattern()
        elif pattern_type == 'gradient':
            self.pixels = self._gradient_pattern()
        else:
            self.pixels = self._noise_pattern()
            
        img = PILImage.fromarray(self.pixels, 'RGB')
        img.save(self.path)

    def _checker_pattern(self, size=32):
        pattern = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        for i in range(0, self.height, size):
            for j in range(0, self.width, size):
                if (i//size + j//size) % 2:
                    pattern[i:i+size, j:j+size] = np.random.randint(0, 256, (3,))
        return pattern

    def _gradient_pattern(self):
        pattern = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        for i in range(self.height):
            for j in range(self.width):
                pattern[i,j] = [
                    int(255 * i/self.height),
                    int(255 * j/self.width),
                    int(255 * (i+j)/(self.height+self.width))
                ]
        return pattern

    def _noise_pattern(self):
        return np.random.randint(0, 256, (self.height, self.width, 3), dtype=np.uint8)


class CodeGenerator:
    """
    Generate code snippets
    """
    
    def __init__(self):
        self.text = TextGenerator()

    def html(self):
        """
        Generate random HTML snippet
        """
        tags = ['div', 'p', 'span', 'section']
        classes = [self.text.noun(1), self.text.adjective(1)]
        tag = random.choice(tags)
        return f'<{tag} class="{"-".join(classes)}">{self.text.word(5)}</{tag}>'

    def sql(self):
        """
        Generate random SQL query
        """
        tables = ['users', 'products', 'orders']
        conditions = ['active = 1', 'created_at > NOW()', 'status = "pending"']
        return f'SELECT * FROM {random.choice(tables)} WHERE {random.choice(conditions)} LIMIT {random.randint(10,100)};'

    def css(self) -> str:
        """Generate random CSS rule"""
        properties = {
            'color': f'#{random.randint(0, 0xFFFFFF):06x}',
            'margin': f'{random.randint(0, 30)}px',
            'padding': f'{random.randint(0, 20)}px',
            'font-size': f'{random.randint(12, 24)}px',
            'border-radius': f'{random.randint(0, 10)}px'
        }
        
        selector = f'.{self.text.noun(1)}'
        props = [f"    {k}: {v};" for k, v in random.sample(properties.items(), 3)]
        return f"{selector} {{\n" + "\n".join(props) + "\n}"

    def javascript(self) -> str:
        """Generate random JavaScript code"""
        function_name = f"handle{self.text.noun(1).title()}"
        param = self.text.noun(1).lower()
        return f"""function {function_name}({param}) {{
    console.log('Processing {param}...');
    return {param}.toString().toUpperCase();
}}"""


class TimeGenerator:
    """
    Generate time-related content
    """
    
    def date(self, start_year=2000, end_year=2024):
        """
        Generate random date
        """
        start = datetime.date(start_year, 1, 1)
        end = datetime.date(end_year, 12, 31)
        days_between = (end - start).days
        random_days = random.randint(0, days_between)
        return start + datetime.timedelta(days=random_days)

    def timestamp(self):
        """
        Generate random timestamp
        """
        return self.date().strftime("%Y-%m-%d %H:%M:%S")


class SocialMediaGenerator:
    """Generate social media style content"""
    
    def __init__(self):
        self.text = TextGenerator()
        self.phrase = PhraseGenerator()

    def tweet(self) -> str:
        """Generate a tweet-like message"""
        content = self.phrase.noam()
        hashtags = self.text.hashtag(2)
        emoji = self.text.emoji(1)
        return f"{content} {hashtags} {emoji}"
    
    def comment(self) -> str:
        """Generate a social media comment"""
        patterns = [
            lambda: f"{self.text.emoji(1)} {self.text.word(random.randint(3,8))}",
            lambda: f"This is {self.text.adjective(1)}! {self.text.emoji(2)}",
            lambda: f"{self.text.hashtag(1)} {self.text.emoji(1)}"
        ]
        return random.choice(patterns)()

    def username_with_handle(self) -> str:
        """Generate username with handle"""
        return f"@{self.text.username()}"


class FileGenerator:
    """Generate various file contents"""
    
    def __init__(self):
        self.text = TextGenerator()
        self.data = DataGenerator()

    def csv_data(self, rows: int = 5) -> str:
        """Generate CSV content"""
        headers = ['id', 'name', 'email', 'status']
        content = [','.join(headers)]
        
        for _ in range(rows):
            row = [
                self.text.alphanumeric(6),
                f"{self.text.noun(1)} {self.text.noun(1)}",
                f"{self.text.alphanumeric(8)}@example.com",
                random.choice(['active', 'pending', 'inactive'])
            ]
            content.append(','.join(row))
        
        return '\n'.join(content)

    def log_entry(self) -> str:
        """Generate a log file entry"""
        levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        return f"{timestamp} [{random.choice(levels)}] {self.text.word(random.randint(5,10))}"

    def config_ini(self) -> str:
        """Generate INI configuration file content"""
        sections = {
            'database': {
                'host': 'localhost',
                'port': str(random.randint(3000, 9999)),
                'username': self.text.username(),
                'password': self.text.alphanumeric(12)
            },
            'api': {
                'key': self.text.alphanumeric(32),
                'timeout': str(random.randint(30, 300)),
                'retry_limit': str(random.randint(1, 5))
            }
        }
        
        content = []
        for section, values in sections.items():
            content.append(f"[{section}]")
            content.extend(f"{k} = {v}" for k, v in values.items())
            content.append("")
        
        return '\n'.join(content)


if __name__ == "__main__":
    text_gen = TextGenerator()
    print(text_gen.verb(2))

    phrase_gen = PhraseGenerator()
    print(phrase_gen.noam())
