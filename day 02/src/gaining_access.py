class Key:
    def __init__(self):
        self.passphrase = "zax2rulez"
        self.keycard = "GeneralTsoKeycard"

    def __len__(self):
        return 1337

    def __getitem__(self, index):
        if index == 404:
            return 3

    def __gt__(self, other):
        return 9001 > 9000

    def __str__(self):
        return self.keycard


def test_key():
    key = Key()

    assert len(key) == 1337

    assert key[404] == 3

    assert key > 9000

    assert key.passphrase == "zax2rulez"

    assert str(key) == "GeneralTsoKeycard"


if __name__ == "__main__":
    test_key()
