import unittest

from db import (
    db,
    ProductModel,
    create_product,
    get_product_by_id,
    update_product,
    delete_product,
)


class TestProducts(unittest.TestCase):

    def setUp(self):
        db.init(':memory:')
        db.connect()
        db.create_tables([ProductModel])

    def tearDown(self):
        db.drop_tables([ProductModel])
        db.close()

    def test_product_crud(self):
        product = create_product("Milk", 32)

        self.assertEqual(get_product_by_id(product.id).name, "Milk")

        update_product(product.id, price=35)
        self.assertEqual(get_product_by_id(product.id).price, 35)

        self.assertTrue(delete_product(product.id))
        self.assertIsNone(get_product_by_id(product.id))


if __name__ == '__main__':
    unittest.main()
