# EmojieCipher
An emoji cipher tool using Python Click.

<img alt="EmojieCipher in use" src="assets/video.gif"></img>

## Installation
```
pip install -r requirements.txt
```

## Usage

```python
# returns '🌓🎹🔁🍘📇 👸🌓👸😬👸🏁'
python main.py encrypt --text "Hello World!" --key 200

# returns 'Hello World!'
python main.py decrypt --text "🌓🎹🔁🍘📇 👸🌓👸😬👸🏁" --key 200

# List available commands and options
python main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.