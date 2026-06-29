"""
pythonAssessment.py
-------------------
A Python program to perform text analysis tasks on a given news article.
Tasks include:
  - Counting occurrences of a specific word
  - Identifying the most common word
  - Calculating the average word length
  - Counting the number of paragraphs
  - Counting the number of sentences
 
Author: NLP Tech Team
"""
 
import re

 
# 1. Count occurrences of a specific word

def count_specific_word(text: str, search_word: str) -> int:
    """
    Count how many times search_word appears in text (case-insensitive).
 
    Args:
        text (str): The full article text to search through.
        search_word (str): The word to search for.
 
    Returns:
        int: Number of occurrences. Returns 0 if no matches are found.
    """
    if not text or not search_word:
        return 0
 
    count = 0
    # Normalize both to lowercase for case-insensitive matching
    text_lower = text.lower()
    word_lower = search_word.lower()
 
    # Use word boundaries to avoid partial matches (e.g. "AI" inside "FAIL")
    pattern = r'\b' + re.escape(word_lower) + r'\b'
    words_found = re.findall(pattern, text_lower)
 
    # FOR LOOP: iterate over each match and increment count
    for _ in words_found:
        count += 1
 
    return count


# 2. Identify the most common word
def identify_most_common_word(text: str):
    """
    Find the most frequently used word in text (case-insensitive).
 
    Args:
        text (str): The full article text.
 
    Returns:
        str | None: The most common word, or None if text is empty.
    """
    if not text.strip():
        return None
 
    # Extract only alphabetic words, ignoring punctuation
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
 
    if not words:
        return None
 
    # Build a frequency dictionary using a FOR LOOP
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
 
    # Find the most common word
    most_common_word = max(word_freq, key=word_freq.get)
    return most_common_word

# 3. Calculate average word length
def calculate_average_word_length(text: str) -> float:
    """
    Calculate the average number of characters per word,
    excluding punctuation and special characters.
 
    Args:
        text (str): The full article text.
 
    Returns:
        float: Average word length. Returns 0 if text is empty.
    """
    if not text.strip():
        return 0
 
    words = re.findall(r'\b[a-zA-Z]+\b', text)
 
    if not words:
        return 0
 
    total_length = 0
 
    # FOR LOOP: sum up the length of each word
    for word in words:
        total_length += len(word)
 
    average = round(total_length / len(words), 2)
    return average
 
 

# 4. Count paragraphs
def count_paragraphs(text: str) -> int:
    """
    Count the number of paragraphs, defined as blocks of text
    separated by one or more empty lines.
 
    Args:
        text (str): The full article text.
 
    Returns:
        int: Number of paragraphs. Returns 1 for an empty string.
    """
    if not text.strip():
        return 1
 
    # Split on one or more blank lines
    blocks = re.split(r'\n\s*\n', text)
 
    count = 0
 
    # FOR LOOP: count only non-empty paragraph blocks
    for block in blocks:
        if block.strip():
            count += 1
 
    return count
 
 

# 5. Count sentences

def count_sentences(text: str) -> int:
    """
    Count the number of sentences based on terminal punctuation
    (periods, exclamation marks, question marks).
 
    Args:
        text (str): The full article text.
 
    Returns:
        int: Number of sentences. Returns 1 for an empty string.
    """
    if not text.strip():
        return 1
 
    # Match any sequence of characters ending in . ! or ?
    sentences = re.findall(r'[^.!?]*[.!?]', text)
 
    count = 0
 
    # FOR LOOP: count only sentences with real content
    for sentence in sentences:
        if sentence.strip():
            count += 1
 
    # IF/ELSE: guard against zero matches
    if count > 0:
        return count
    else:
        return 1
 
 

# Sample article

ARTICLE = """
Artificial intelligence is transforming the technology industry at an unprecedented pace.
Companies across the globe are investing billions of dollars into AI research and development.
From healthcare to finance, AI applications are reshaping how businesses operate and deliver value.
 
Natural language processing, a subfield of AI, enables machines to understand and generate human language.
NLP powers tools like chatbots, translation services, and sentiment analysis platforms.
Many tech startups are leveraging NLP to build innovative products that solve real-world problems.
 
Despite rapid progress, AI also raises important ethical questions.
Issues such as data privacy, algorithmic bias, and job displacement demand serious attention.
Governments and organisations worldwide are working to establish frameworks that ensure AI is developed responsibly.
 
The future of AI looks promising, but it requires collaboration between technologists, policymakers, and society at large.
Together, we can harness the power of AI to create a more equitable and efficient world.
"""
 
 

# Main runner with WHILE LOOP menu

def main():
    options = {
        "1": "Count occurrences of a specific word",
        "2": "Identify the most common word",
        "3": "Calculate average word length",
        "4": "Count paragraphs",
        "5": "Count sentences",
        "6": "Run all analyses",
        "0": "Exit",
    }
 
    print("=" * 60)
    print("       NEWS ARTICLE TEXT ANALYSIS TOOL")
    print("=" * 60)
    print(f"\nLoaded article ({len(ARTICLE.split())} words)\n")
 
    # WHILE LOOP: keep the menu running until the user exits
    running = True
    while running:
        print("\nSelect an option:")
        for key, label in options.items():
            print(f"  [{key}] {label}")
 
        choice = input("\nEnter your choice: ").strip()
 
        # IF/ELSE block covering all menu branches
        if choice == "1":
            search = input("Enter the word to search for: ").strip()
            result = count_specific_word(ARTICLE, search)
            print(f"\n  → '{search}' appears {result} time(s).")
 
        elif choice == "2":
            result = identify_most_common_word(ARTICLE)
            if result is not None:
                print(f"\n  → Most common word: '{result}'")
            else:
                print("\n  → No words found (empty text).")
 
        elif choice == "3":
            result = calculate_average_word_length(ARTICLE)
            print(f"\n  → Average word length: {result} characters")
 
        elif choice == "4":
            result = count_paragraphs(ARTICLE)
            print(f"\n  → Number of paragraphs: {result}")
 
        elif choice == "5":
            result = count_sentences(ARTICLE)
            print(f"\n  → Number of sentences: {result}")
 
        elif choice == "6":
            print("\n--- Full Analysis ---")
            print(f"  Occurrences of 'AI'  : {count_specific_word(ARTICLE, 'AI')}")
            print(f"  Most common word     : '{identify_most_common_word(ARTICLE)}'")
            print(f"  Avg word length      : {calculate_average_word_length(ARTICLE)} chars")
            print(f"  Paragraphs           : {count_paragraphs(ARTICLE)}")
            print(f"  Sentences            : {count_sentences(ARTICLE)}")
 
            print("\n--- Edge Case Tests ---")
            print(f"  count_specific_word('', 'AI')        → {count_specific_word('', 'AI')}")
            print(f"  count_specific_word(article, 'xyz')  → {count_specific_word(ARTICLE, 'xyz')}")
            print(f"  identify_most_common_word('')        → {identify_most_common_word('')}")
            print(f"  calculate_average_word_length('')    → {calculate_average_word_length('')}")
            print(f"  count_paragraphs('')                 → {count_paragraphs('')}")
            print(f"  count_sentences('')                  → {count_sentences('')}")
 
        elif choice == "0":
            print("\n  Goodbye!")
            running = False  # WHILE LOOP exit condition
 
        else:
            print("\n  Invalid option. Please enter a number from the menu.")
 
    print("=" * 60)
 
 
if __name__ == "__main__":
    main()
