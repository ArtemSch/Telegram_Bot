from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_dates import buy_callback


choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Купить грушу",
                                          callback_data=buy_callback.new(item_name="pear",
                                                                         quantity=2)

                                      ),
                                      InlineKeyboardButton(
                                          text="Купить яблоки",
                                          callback_data="buy:apple:5"

                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Отмена",
                                          callback_data="cancel"
                                      )
                                  ]
                              ])

pear_keyboard = InlineKeyboardMarkup()

PEAR_LINK = "http://vk.com"

pear_link = InlineKeyboardButton(text="Купи тут", url=PEAR_LINK)

pear_keyboard.insert(pear_link)