
class EnglishToFrenchTranslator(object):

    DICTIONARY = {
        'Hello World!': 'Bonjour le monde!'
    }

    def __get__(self, instance, owner):
        # returns original message if no translation found
        return EnglishToFrenchTranslator.DICTIONARY.get(
            instance.msg, instance.msg
        )


class EnglishToGermanTranslator(object):

    DICTIONARY = {
        'Hello World!': 'Hallo Welt!'
    }

    def __get__(self, instance, owner):
        # returns original message if no translation found
        return EnglishToGermanTranslator.DICTIONARY.get(
            instance.msg, instance.msg
        )


class EnglishTranslator(object):

    DICTIONARY = {
        'Hello World!': 'Hello World!'
    }

    def __get__(self, instance, owner):
        return EnglishTranslator.DICTIONARY.get(
            instance.msg, instance.msg
        )


class Message(object):
    in_french = EnglishToFrenchTranslator()
    in_german = EnglishToGermanTranslator()

    def __init__(self, msg):
        self.msg = msg


if __name__ == '__main__':
    msg = Message('Hello World!')
    print 'English ->', msg.msg
    print 'French ->', msg.in_french
    print 'German ->', msg.in_german