def convert(emo):
    emo = emo.replace(':)', '🙂')
    emo = emo.replace(':(', '🙁')
    return emo

def main():
    text = input("enter the text: ")
    print(convert(text))


if __name__ == "__main__":
    main()

