class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


if __name__ == '__main__':
    Singleton()
    Singleton()
