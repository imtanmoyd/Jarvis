# Jarvis - Your Personal Virtual Assistant

Jarvis is a powerful and intelligent personal virtual assistant built with Python. It integrates various functionalities to automate tasks through voice commands, making your life easier and more productive.

## Features

- **Voice Command Recognition**: Understands and processes user commands using Google's speech recognition.
- **Web Browsing Automation**: Opens popular websites like Google, YouTube, Facebook, and more.
- **Text-to-Speech**: Converts text to speech for interactive responses.
- **News Fetching**: Retrieves and reads out the latest news headlines.
- **Music Playing**: Plays songs from a predefined music library.
- **AI-Powered Responses**: Handles sophisticated queries using OpenAI's GPT-3.5-turbo model.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/tanmoyaiml/Jarvis.git
    ```

2. Navigate to the project directory:
    ```sh
    cd jarvis
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Obtain an API key from [NewsAPI](https://newsapi.org/) and replace the placeholder in the script:
    ```python
    newsapi="YOUR_NEWSAPI_KEY"
    ```
2. Obtain an API key from [OpenAI](https://openai.com/) and configure it in the script:
    ```python
    client = OpenAI(api_key="YOUR_OPENAI_KEY")
    ```

## Usage

Run the script:
```sh
python main.py
