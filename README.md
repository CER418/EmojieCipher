# EmojieCipher
An emoji cipher tool using base64 encryption and Python Click.

<img alt="EmojieCipher in use" src="assets/video.gif"></img>

## Installation
```
pip install -r requirements.txt
```

## Usage

```python
# returns 'π―π€π€πΆππ€πππ€πππππ€π¦π'
python main.py encode --text 'Hello World!'

# returns 'Hello World!'
python main.py decode --text 'π―π€π€πΆππ€πππ€πππππ€π¦π'

# List available commands and options
python main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.