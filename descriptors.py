import unittest


class RankDescriptor(object):

    def __get__(self, instance, owner):
        """
        :param instance: self variable of the object being updated.
        :param owner: owning class object
        :return:
        """
        return self.__dict__[instance]

    def __set__(self, instance, val):
        """
        :param instance: self variable of the object being updated.
        :param val: value of the object to be set
        :return: None
        """
        if not 1 <= val <= 10:
            raise ValueError(
                'Invalid rank {}, must be between 1 to 10.'.format(val)
            )
        self.__dict__[instance] = val

    def __delete__(self, instance):
        """
        :param instance: self variable of the object being updated.
        :return: None
        """
        del self.__dict__[instance]


class Item(object):
    rank = RankDescriptor()

    def __init__(self, name):
        self.name = name


class TestItemRank(unittest.TestCase):

    def setUp(self):
        self.item = Item('Item-X')

    def test_rank_value_more_than_range(self):
        with self.assertRaises(ValueError):
            self.item.rank = 11

    def test_rank_value_less_than_range(self):
        with self.assertRaises(ValueError):
            self.item.rank = -11

    def test_rank_value_within_range(self):
        self.assertIsNone(setattr(self.item, 'rank', 9))


if __name__ == '__main__':
    unittest.main()
