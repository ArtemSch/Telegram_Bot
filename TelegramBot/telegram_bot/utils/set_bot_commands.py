from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("menu", "Пюрешки или котлетки?"),
        types.BotCommand("test", "Сдать тест"),
        types.BotCommand("invoices", "Купить TESLA"),
        types.BotCommand("callback", "Перезвон менеджера"),
        types.BotCommand("items", "Купить яблоки или груши")
    ])
