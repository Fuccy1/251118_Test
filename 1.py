import csv
import random
from datetime import datetime, timedelta

def random_tracking():
    return "TK" + datetime.now().strftime("%y") + "".join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10))

senders = ["张三","李四","王五","赵六","钱七","孙八","周九","吴十","郑十一","冯十二"]
recipients = ["刘一","陈二","杨三","朱四","秦五","许六","何七","吕八","施九","孔十"]
cities = ["北京","上海","广州","深圳","杭州","南京","成都","重庆","武汉","西安","长沙","苏州","郑州","青岛"]
statuses = ["已揽收","运输中","到达分拨中心","派送中","已签收","异常件"]
carriers = ["顺丰","京东物流","邮政EMS","圆通","中通","韵达","申通","极兔"]
products = ["服饰","数码产品","图书","食品","日用品","家居用品","美妆","玩具","母婴用品","运动装备"]

def random_weight():
    return round(random.uniform(0.2, 15.0), 2)

def random_cost(weight):
    base = 8
    return round(base + weight * random.uniform(0.8, 1.6), 2)

def random_dates():
    ship_date = datetime.now() - timedelta(days=random.randint(0, 10))
    transit_days = random.randint(1, 7)
    expected = ship_date + timedelta(days=transit_days)
    return ship_date.date().isoformat(), expected.date().isoformat()

rows = []
for i in range(500):
    tracking = random_tracking()
    sender = random.choice(senders)
    recipient = random.choice(recipients)
    origin = random.choice(cities)
    # 保证目的地不同
    dest_choices = [c for c in cities if c != origin]
    destination = random.choice(dest_choices)
    status = random.choice(statuses)
    carrier = random.choice(carriers)
    product = random.choice(products)
    weight = random_weight()
    cost = random_cost(weight)
    ship_date, expected_date = random_dates()
    rows.append({
        "tracking_number": tracking,
        "sender": sender,
        "recipient": recipient,
        "origin_city": origin,
        "destination_city": destination,
        "product_type": product,
        "status": status,
        "carrier": carrier,
        "weight_kg": weight,
        "shipping_cost": cost,
        "ship_date": ship_date,
        "expected_delivery": expected_date
    })

file_name = "express_sample.csv"  # 根目录下生成

headers = [
    "tracking_number","sender","recipient","origin_city","destination_city",
    "product_type","status","carrier","weight_kg","shipping_cost","ship_date","expected_delivery"
]

with open(file_name, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)

print(f"已生成文件 {file_name}，包含 {len(rows)} 行示例快递信息。")