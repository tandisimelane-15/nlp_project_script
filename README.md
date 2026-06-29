# News Article Text Analysis Tool

## Description
This is a Python command-line application developed for an NLP tech startup that performs various text analysis tasks on a given news article. The program provides an interactive menu-driven interface that allows users to extract valuable insights from text, including word frequency, sentence structure, and paragraph organisation.

## Features
- Count occurrences of a specific word (case-insensitive)
- Identify the most common word in the article
- Calculate the average word length (excluding punctuation and special characters)
- Count the number of paragraphs based on empty-line separation
- Count the number of sentences based on terminal punctuation
- Full analysis mode that runs all tasks at once
- Edge case handling for empty strings and unmatched searches
- Interactive while-loop menu that runs until the user chooses to exit

## How to Run the Project
1. Clone the repository
2. Open the project folder
3. Ensure Python 3 is installed on your machine
4. Run the script from your terminal:
   ```bash
   python pythonAssessment.py
   ```
5. Follow the on-screen menu to select an analysis option

## Functions

| Function | Arguments | Returns | Description |
|---|---|---|---|
| `count_specific_word(text, search_word)` | `str, str` | `int` | Counts occurrences of a word (case-insensitive, whole-word match) |
| `identify_most_common_word(text)` | `str` | `str \| None` | Returns the most frequently used word |
| `calculate_average_word_length(text)` | `str` | `float` | Returns average character count per word |
| `count_paragraphs(text)` | `str` | `int` | Counts paragraph blocks separated by empty lines |
| `count_sentences(text)` | `str` | `int` | Counts sentences ending in `.` `!` or `?` |

## Edge Cases Handled

- `count_specific_word('', 'AI')` → `0`
- `identify_most_common_word('')` → `None`
- `calculate_average_word_length('')` → `0`
- `count_paragraphs('')` → `1`
- `count_sentences('')` → `1`

## Technologies Used
- Python 3
- `re` module (Regular Expressions)

## Project Structure
```
├── pythonAssessment.py   # Main script with all functions and menu
└── README.md             # Project documentation
```

## Future Implementations
- Allow users to load and analyse their own text files
- Add support for identifying named entities (people, places, organisations)
- Export analysis results to a `.csv` or `.json` file
- Add a sentiment analysis feature using an NLP library such as NLTK

## How to Contribute
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT License

Copyright (c) 2026 NLP Tech Team

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.