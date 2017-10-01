import datetime
import random

from product.models import Product, ProductCategory, Principle, ProductSell

def gen():
    
    principle = Principle(name='Bombay Sweet', contact_no='01737573157')
    principle.save()

    product_category = ProductCategory(name='Chips')
    product_category.save()
    Product(product_category=product_category, principal=principle, name='Slanty', code='1.06', weight='25 gm',
            mop='80(20×2)', distributor_price='920.0', sell_price='961.0').save()
    Product(product_category=product_category, principal=principle, name='Alooz', code='1.07', weight='25 gm',
            mop='80(20×2)', distributor_price='920.0', sell_price='961.0').save()
    Product(product_category=product_category, principal=principle, name='Potato Ring Chips', code='1.08',
            weight='20 gm', mop='80(20 * 4)', distributor_price='613.36', sell_price='641.0').save()
    Product(product_category=product_category, principal=principle, name='Chipstar ( Cheese Ball)', code='1.09',
            weight='20 gm', mop='80(20 * 4)', distributor_price='613.36', sell_price='641.0').save()
    Product(product_category=product_category, principal=principle, name='Chipstar (onion Ring )', code='1.1',
            weight='20 gm', mop='80(20 * 4)', distributor_price='613.36', sell_price='641.0').save()
    Product(product_category=product_category, principal=principle, name='Pasta Chips (tubes)', code='1.17',
            weight='20 gm', mop='80(20 * 4)', distributor_price='613.36', sell_price='641.0').save()
    Product(product_category=product_category, principal=principle, name='Ring Chips', code='1.01', weight='25 gm',
            mop='80 (20×2)', distributor_price='613.36', sell_price='641.0').save()
    Product(product_category=product_category, principal=principle, name='Potato Crackers', code='1.02', weight='25 gm',
            mop='80(20×4)', distributor_price='613.36', sell_price='641.0').save()
    Product(product_category=product_category, principal=principle, name='Bombay Sticks', code='1.03', weight='14 gm',
            mop='80(20×4)', distributor_price='307.28', sell_price='321.0').save()
    Product(product_category=product_category, principal=principle, name='Mr. Twist', code='1.04', weight='25 gm',
            mop='80(20×2)', distributor_price='920.0', sell_price='961.0').save()
    Product(product_category=product_category, principal=principle, name='Korntos', code='1.05', weight='20 gm',
            mop='80(20×4)', distributor_price='613.36', sell_price='641.0').save()
    Product(product_category=product_category, principal=principle, name='Chipstar ( Potato Sticks)', code='1.11',
            weight='20 gm', mop='80(20 * 4)', distributor_price='613.36', sell_price='641.0').save()
    Product(product_category=product_category, principal=principle, name='Chipstar ( Cheese Puff)', code='1.12',
            weight='20 gm', mop='80(20 * 4)', distributor_price='613.36', sell_price='641.0').save()
    Product(product_category=product_category, principal=principle, name='Chipstar ( Twister)', code='1.13',
            weight='20 gm', mop='80(20 * 4)', distributor_price='613.36', sell_price='641.0').save()
    Product(product_category=product_category, principal=principle, name='Chipstar (smiley )', code='1.14',
            weight='20 gm', mop='80(20 * 4)', distributor_price='613.36', sell_price='641.0').save()
    Product(product_category=product_category, principal=principle, name='Chipstar (choco Sea )', code='1.15',
            weight='20 gm', mop='80(20 * 4)', distributor_price='613.36', sell_price='641.0').save()
    Product(product_category=product_category, principal=principle, name='Pasta Chips (shell)', code='1.16',
            weight='20 gm', mop='80(20 * 4)', distributor_price='613.36', sell_price='641.0').save()

    product_category = ProductCategory(name='Chanachur')
    product_category.save()
    Product(product_category=product_category, principal=principle, name='Bombay Mix', code='2.07', weight='30 gm',
            mop='200(25×8)', distributor_price='1073.4', sell_price='1122.0').save()
    Product(product_category=product_category, principal=principle, name='Bombay Mix', code='2.08', weight='200 gm',
            mop='5', distributor_price='153.335', sell_price='160.0').save()
    Product(product_category=product_category, principal=principle, name='Dalmoth', code='2.09', weight='30 gm',
            mop='160(20×8)', distributor_price='982.56', sell_price='1027.0').save()
    Product(product_category=product_category, principal=principle, name='Dalmoth', code='2.1', weight='200 gm',
            mop='5', distributor_price='153.335', sell_price='160.0').save()
    Product(product_category=product_category, principal=principle, name='Bbq', code='2.11', weight='35 gm',
            mop='160(20×8)', distributor_price='1226.73', sell_price='1282.0').save()
    Product(product_category=product_category, principal=principle, name='Bbq', code='2.12', weight='150 gm',
            mop='40(10×4)', distributor_price='924.6', sell_price='966.0').save()
    Product(product_category=product_category, principal=principle, name='Deshi Mix (geen Chilli)', code='2.13',
            weight='35 gm', mop='160 (20×8)', distributor_price='1226.73', sell_price='1282.0').save()
    Product(product_category=product_category, principal=principle, name='Deshi Mix (geen Chilli)', code='2.14',
            weight='150 gm', mop='40(10×4)', distributor_price='924.6', sell_price='966.0').save()
    Product(product_category=product_category, principal=principle, name='Deshi Mix (red Chilli)', code='2.15',
            weight='35 gm', mop='160 (20×8)', distributor_price='1226.73', sell_price='1282.0').save()
    Product(product_category=product_category, principal=principle, name='Deshi Mix (red Chilli)', code='2.16',
            weight='150 gm', mop='40(10×4)', distributor_price='924.6', sell_price='966.0').save()
    Product(product_category=product_category, principal=principle, name='Chanachur', code='2.01', weight='20 gm',
            mop='160 (20×8)', distributor_price='614.56', sell_price='642.0').save()
    Product(product_category=product_category, principal=principle, name='Chanachur', code='2.02', weight='50 gm',
            mop='160(20×8)', distributor_price='1253.04', sell_price='1310.0').save()
    Product(product_category=product_category, principal=principle, name='Chanachur', code='2.03', weight='85 gm',
            mop='80(10×8)', distributor_price='940.24', sell_price='982.0').save()
    Product(product_category=product_category, principal=principle, name='Chanachur', code='2.04', weight='150 gm',
            mop='40(10×4)', distributor_price='805.0', sell_price='841.0').save()
    Product(product_category=product_category, principal=principle, name='Chanachur', code='2.05', weight='300 gm',
            mop='20(5×4)', distributor_price='800.0', sell_price='836.0').save()
    Product(product_category=product_category, principal=principle, name='Chanachur', code='2.06', weight='650 gm',
            mop='8(8×1)', distributor_price='652.78', sell_price='682.0').save()

    product_category = ProductCategory(name='Fruit Drinks')
    product_category.save()
    Product(product_category=product_category, principal=principle, name='Jucy (fruit Drinks)', code='3.01',
            weight='200 ml', mop='20pcs.', distributor_price='303.0', sell_price='317.0').save()

    product_category = ProductCategory(name='Masala')
    product_category.save()
    Product(product_category=product_category, principal=principle, name='Red Chilli', code='4.01', weight='50 gm',
            mop='160(20×8)', distributor_price='2424.0', sell_price='2533.0').save()
    Product(product_category=product_category, principal=principle, name='Red Chilli', code='4.02', weight='100 gm',
            mop='80(10×8)', distributor_price='2578.0', sell_price='2694.0').save()
    Product(product_category=product_category, principal=principle, name='Red Chilli', code='4.03', weight='200 gm',
            mop='40(5×8)', distributor_price='2464.0', sell_price='2575.0').save()
    Product(product_category=product_category, principal=principle, name='Turmeric', code='4.04', weight='50 gm',
            mop='160(20×8)', distributor_price='2424.0', sell_price='2533.0').save()
    Product(product_category=product_category, principal=principle, name='Turmeric', code='4.05', weight='100 gm',
            mop='80(10×8)', distributor_price='2200.0', sell_price='2299.0').save()
    Product(product_category=product_category, principal=principle, name='Turmeric', code='4.06', weight='200 gm',
            mop='40(5×8)', distributor_price='2085.0', sell_price='2179.0').save()
    Product(product_category=product_category, principal=principle, name='Cumin', code='4.07', weight='50 gm',
            mop='160(20×8)', distributor_price='5156.0', sell_price='5389.0').save()
    Product(product_category=product_category, principal=principle, name='Cumin', code='4.08', weight='100 gm',
            mop='80(10×8)', distributor_price='5308.0', sell_price='5547.0').save()
    Product(product_category=product_category, principal=principle, name='Cumin', code='4.09', weight='200 gm',
            mop='40(5×8)', distributor_price='4928.0', sell_price='5150.0').save()

    product_category = ProductCategory(name='Frozen Foods')
    product_category.save()
    Product(product_category=product_category, principal=principle, name='Malaysian Roti Paratha', code='5.01',
            weight='400 gm', mop='12pkt/ctn', distributor_price='552.0', sell_price='600.0').save()
    Product(product_category=product_category, principal=principle, name='malaysian roti paratha (family pack)',
            code='5.02', weight='1600 gm', mop='6pkt/ctn', distributor_price='1012.002', sell_price='1100.0').save()
    Product(product_category=product_category, principal=principle, name='Dal Puri & Alo Puri', code='5.03',
            weight='500 gm', mop='20pkt/ctn', distributor_price='1049.8', sell_price='1100.0').save()
    Product(product_category=product_category, principal=principle, name='Kishan Cheese', code='5.04', weight='200 gm',
            mop='5pkt/kg', distributor_price='800.0', sell_price='856.0').save()
    Product(product_category=product_category, principal=principle, name='Kishan Butter', code='5.05', weight='200 gm',
            mop='5pkt/kg', distributor_price='467.5', sell_price='500.0').save()
    
def sell():
    products = Product.objects.all()

    for product in products:
        sell_number = random.randint(1,6)
        for i in range(sell_number):
            amount = random.randint(1,10)
            sell_date = datetime.date.today() - datetime.timedelta( random.randint(0,7) )
            ProductSell(product=product,amount=amount,sell_date=sell_date).save()