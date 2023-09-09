import unittest


def koneksi_ke_db():
    print("[terhubung ke db]")


def putus_koneksi_db(db):
    print("[tidak terhubung ke db {}]".format(db))


class User:
    username = ""
    aktif = False

    def __init__(self, db, username):  # using db sample
        self.username = username

    def set_aktif(self):
        self.aktif = True


class TestUser(unittest.TestCase):
    # Test Case 1
    def test_user_default_not_active(self):
        db = koneksi_ke_db()
        nics = User(db, "nics")
        self.assertFalse(nics.aktif)  # tidak aktif secara default
        putus_koneksi_db(db)

    # Test Case 2
    def test_user_is_active(self):
        db = koneksi_ke_db()
        nics = User(db, "nics")
        nics.set_aktif()  # aktifkan user baru
        self.assertTrue(nics.aktif)
        putus_koneksi_db(db)


if __name__ == "__main__":
    # Test Runner
    unittest.main()
