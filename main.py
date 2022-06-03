def get_text():
    letter_path = 'Input/Letters/starting_letter.txt'
    with open(letter_path, 'r') as f:
        data = f.read()
        f.close()
        return data


def get_names():
    names_path = 'Input/Names/invited_names.txt'
    with open(names_path, 'r') as f:
        data = f.read()
        f.close()
        return data.splitlines()


def main():
    output_path = 'Output/ReadyToSend'
    text = get_text()
    names = get_names()

    for name in names:
        with open(f'{output_path}/letter_for_{name}.txt', 'w') as f:
            letter = text.replace('[name]', name)
            f.write(letter)
            f.close()

    print('Letter were successfully saved')


if __name__ == '__main__':
    main()
