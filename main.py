import click
import random

keymap = {'a': '\U0001F38F', 'b': '\U0001F3C7', 'c': '\U0001F697', 'd': '\U0001F4C7', 'e': '\U0001F358',
          'f': '\U0001F44B',
          'g': '\U0001F68B', 'h': '\U0001F3C1', 'i': '\U0001F45C', 'j': '\U0001F573', 'k': '\U0001F52E',
          'l': '\U0001F478',
          'm': '\U0001F570', 'n': '\U0001F326', 'o': '\U0001F313', 'p': '\U0001F522', 'q': '\U0001F575',
          'r': '\U0001F501', 's': '\U0001F636', 't': '\U0001F392', 'u': '\U0001F4C0', 'v': '\U0001F530',
          'w': '\U0001F3B9',
          'x': '\U0001F34A',
          'y': '\U0001F61F', 'z': '\U0001F458',

          '0': '\U0001F40A', '1': '\U0001F4E3', '2': '\U0001F3D3',
          '3': '\U0001F42A', '4': '\U0001F966', '5': '\U0001F6A8', '6': '\U0001F6F6', '7': '\U0001F3A0',
          '8': '\U0001F50D',
          '9': '\U0001F48A',

          '.': '\U0001F982', ',': '\U0001F4B3', '-': '\U0001F34E',
          '?': '\U0001F32A', '!': '\U0001F62C', "'": '\U0001F356'}


def shuffle(text, key):
    random.seed(key)
    lst = list(range(len(text)))
    random.shuffle(lst)
    return lst


@click.command()
@click.option('-t', '--text', prompt='Encrypt text', type=str)
@click.option('-k', '--key', prompt='Encryption key', type=int)
def encrypt(text: str, key: int):
    try:
        lst = shuffle(text, key)
        shuffled_text = "".join([text[x] for x in lst])
        print("".join(keymap.get(c, " ") for c in shuffled_text.lower()))
    except ValueError:
        print(f"Something went wrong encrypting the character(s): {text}")
        pass


@click.command
@click.option('-t', '--text', prompt='Decrypt text', type=str)
@click.option('-k', '--key', prompt='Decryption key', type=int)
def decrypt(text: str, key: int):
    lst = shuffle(text, key)
    deshuffled_text = "".join(text[i] for i, x in sorted(enumerate(lst), key=lambda x: x[1]))
    mp = {v: k for k, v in keymap.items()}
    print("".join(mp.get(c, " ") for c in deshuffled_text.lower()))


@click.group
def main():
    pass


main.add_command(encrypt)
main.add_command(decrypt)

if __name__ == '__main__':
    main()
