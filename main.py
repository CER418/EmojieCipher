import click
import base64
import keymap


def encrypt(text: str):
    text = text.encode('utf-8')
    return base64.b64encode(text).decode('utf-8')


def decrypt(text: str):
    return base64.b64decode(text).decode('utf-8')


@click.command()
@click.option('-t', '--text', prompt='Encode text')
def encode(text):
    text = encrypt(text)
    print("".join(keymap.get(c, " ") for c in text))


@click.command
@click.option('-t', '--text', prompt='Decode text')
def decode(text):
    mp = {v: k for k, v in keymap.items()}
    print(decrypt("".join(mp.get(c, " ") for c in text)))


@click.group
def main():
    pass


main.add_command(encode)
main.add_command(decode)
main.help = "Example: python main.py encode -t 'Hello World!'"
main.add_help_option = False

if __name__ == '__main__':
    main()
