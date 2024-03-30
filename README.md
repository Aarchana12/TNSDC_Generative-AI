```markdown
# Genie

Genie is an AI-powered virtual companion built using Python. It can perform various tasks such as answering questions, searching Wikipedia, playing music, checking the weather forecast, sending emails, and more.

## Features

- **Voice Recognition**: Uses speech recognition to understand user commands.
- **Natural Language Understanding**: Can process natural language queries and provide relevant responses.
- **Integration with OpenAI**: Provides intelligent responses using OpenAI's GPT models.
- **Task Automation**: Performs tasks such as sending emails, playing music, searching Wikipedia, and more.

## Installation

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/your_username/TNSDC_Generative_AI.git
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:
   ```bash
   cd TNSDC_Generative_AI
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**: Obtain an API key from OpenAI for accessing GPT models and replace `YOUR_OPENAI_API_KEY` in the code with your actual API key.

## Usage

1. **Run the Program**: Execute the `genie_virtual_companion.py` file to start the virtual companion:
   ```bash
   python genie.py
   ```

2. **Speak Commands**: Once the program is running, speak commands such as asking questions, requesting weather updates, playing music, etc., to interact with the virtual companion.

## Supported Commands

- **Search Wikipedia**: Ask questions or search topics using Wikipedia.
- **Open Websites**: Open YouTube, Google, Stack Overflow, etc., in a web browser.
- **Play Music**: Play random music from a specified directory.
- **Check Time**: Get the current time.
- **Send Email**: Send emails to specified recipients.
- **Check Weather**: Check the weather forecast for a specified location.
- **Ask Genie**: Engage in conversation with your virtual companion

## Requirements

- Python 3.x
- pyttsx3
- speech_recognition
- wikipedia
- requests
- geopy
- openai

## API Keys

Make sure to obtain and set up the following API keys:

- **OpenAI API Key**: Required for accessing GPT models from OpenAI.
- **SMTP Server Credentials**: If using the email feature, provide SMTP server credentials for sending emails.

## Contributing

Contributions are welcome! If you have any ideas, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

