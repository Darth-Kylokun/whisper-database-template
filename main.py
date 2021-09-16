from folder import ignite_whisper

def main() -> int:
    app: Flask = ignite_whisper(__name__, 'sqlite:///dad.db')

    return 0

if __name__ == '__main__':
    main()