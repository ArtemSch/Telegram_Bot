from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.item import Item

Tesla_S = Item(
    title="Tesla Model S",
    description="Tesla Model S - пятидвернй электромобиль производства американской компнии Tesla."
                "Прототип был впервые показан в 2009 году;"
                "поставка автомобиля начались в 2012",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Tesla Model S",
            amount=10_000_00
        )
    ],
    start_parameter="create_invoice_tesla_model_s",
    photo_url="https://www.ixbt.com/img/n1/news/2019/10/6/Model-S-hero-e1556066115259_large.jpg",
    photo_size=600
)

Tesla_X = Item(
    title="Tesla Model X",
    description="Tesla Model X -  электромобиль производства американской компнии Tesla."
                "Прототип был впервые показан в 2012 году;"
                "поставка автомобиля начались в 2015",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Tesla Model X",
            amount=35_000_00
        ),
        LabeledPrice(
            label="Доставка",
            amount=15_000_00
        ),
        LabeledPrice(
            label="Скидка",
            amount=5_000_00
        ),
        LabeledPrice(
            label="НДС",
            amount=1_000_00
        ),
    ],
    start_parameter="create_invoice_tesla_model_x",
    photo_url="https://tesla-cdn.thron.com/delivery/public/image/tesla/efbb6471-e1b8-4533-b41a-6df9d50c0a42/bvlatuR/std/0x0/performance-hero@2",
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True
)

POST_REGULAR_SHIPPING = types.ShippingOption(
    id="post_reg",
    title="Почтой",
    prices=[
        types.LabeledPrice(
            "Обычная коробка", 0
        ),
        types.LabeledPrice(
            "Почтой обычной", 1000_00
        ),
    ]
)

POST_FAST_SHIPPING = types.ShippingOption(
    id="post_fast",
    title="Почтой (VIP)",
    prices=[
        types.LabeledPrice(
            "Супер прочная коробка", 1000_00
        ),
        types.LabeledPrice(
            "Почтой срочной - DHL (3 дня)", 15000_00
        ),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(
    id="pickup",
    title="Самовывоз",
    prices=[
        types.LabeledPrice(
            "Самовывоз из магазина", -1000_00
        )
    ]
)
