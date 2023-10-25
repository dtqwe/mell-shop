from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery, SuccessfulPayment
from aiogram.filters import CommandStart
from core.keyboards.reply import menu
from core.keyboards.inline import get_inline_keyboard, get_products_keyboard, get_guarantee, get_contacts, shop_marci, shop_dawnbreaker, shop_dazzle, shop_scpectre, shop_snapfire
router = Router()
from run import bot, dp, YKASSA_TOKEN


@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f'''<b>
        🌟 Добро пожаловать в MellqweShop! 🌟

        🛒 У нас вы найдете широкий выбор скинов на все вкусы и бюджеты. 

        🌈 Мы постоянно обновляем ассортимент, чтобы предложить вам новинки и редкие предметы. Наша команда готова помочь вам в выборе и ответить на все ваши вопросы. 📱 

        🔽 Для навигации пользуйся кнопками ниже: 🔽
        </b>''', parse_mode='HTML', reply_markup=get_inline_keyboard())
    
#------------------------------------SHOP-----------------------------------
@router.callback_query(F.data == 'shop')
async def shop(callback: CallbackQuery):
   # Удаляем сообщение с командой /start
    await callback.message.delete()
    # Отправляем клавиатуру с товарами
    await callback.message.answer('Выберите товар:', reply_markup=get_products_keyboard())

@router.callback_query(F.data == 'product_1')
async def product_1(callback: CallbackQuery):
   # Удаляем сообщение с командой /start
    await callback.message.delete()
    # Отправляем клавиатуру с товарами
    await callback.message.answer('Цена: 1000rub', reply_markup=shop_marci())

@router.callback_query(F.data == 'buy_marci')
async def buy_marci(callback: CallbackQuery):
   # Удаляем сообщение с командой /start
    await callback.message.delete()
    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title='Marci Brightfist',
        description='Комплект, Mythical',
        provider_token=YKASSA_TOKEN,
        payload='buy_marci_pack',
        currency='RUB',
        start_parameter='test_bot',
        prices=[{'label': 'rub', 'amount': 100000}]
    )

@router.pre_checkout_query()
async def pre_checkout_query_handler(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_callback_query(pre_checkout_query.id)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    successful_payment = message.successful_payment

    if successful_payment.invoice_payload == 'buy_marci_pack':
        # Здесь вы можете выполнить действия после успешной оплаты, например, обновить базу данных
        # или отправить пользователю подтверждение оплаты
        await message.answer('Поздравляем! Оплата успешно прошла.')
    
@router.callback_query(F.data == 'marci_back_to_shop')
async def marci_back_to_shop(callback: CallbackQuery):
    # Отправляем клавиатуру с товарами (shop)
    await callback.message.answer('Выберите товар:', reply_markup=get_products_keyboard())

    # Удаляем inline-клавиатуру
    await callback.message.edit_reply_markup(reply_markup=None)
    # Удаляем текст "Цена: 1000rub"
    await callback.message.delete()


@router.callback_query(F.data == 'product_2')
async def product_2(callback: CallbackQuery):
   # Удаляем сообщение с командой /start
    await callback.message.delete()
    # Отправляем клавиатуру с товарами
    await callback.message.answer('Цена: 500rub', reply_markup=shop_scpectre())

@router.callback_query(F.data == 'scpectre_back_to_shop')
async def scpectre_back_to_shop(callback: CallbackQuery):
    # Отправляем клавиатуру с товарами (shop)
    await callback.message.answer('Выберите товар:', reply_markup=get_products_keyboard())

    # Удаляем inline-клавиатуру
    await callback.message.edit_reply_markup(reply_markup=None)
    # Удаляем текст "Цена: 500rub"
    await callback.message.delete()

@router.callback_query(F.data == 'product_3')
async def product_3(callback: CallbackQuery):
   # Удаляем сообщение с командой /start
    await callback.message.delete()
    # Отправляем клавиатуру с товарами
    await callback.message.answer('Цена: 1000rub', reply_markup=shop_snapfire())

@router.callback_query(F.data == 'snapfire_back_to_shop')
async def snapfire_back_to_shop(callback: CallbackQuery):
    # Отправляем клавиатуру с товарами (shop)
    await callback.message.answer('Выберите товар:', reply_markup=get_products_keyboard())

    # Удаляем inline-клавиатуру
    await callback.message.edit_reply_markup(reply_markup=None)
    # Удаляем текст "Цена: 1000rub"
    await callback.message.delete()

@router.callback_query(F.data == 'product_4')
async def product_4(callback: CallbackQuery):
   # Удаляем сообщение с командой /start
    await callback.message.delete()
    # Отправляем клавиатуру с товарами
    await callback.message.answer('Цена: 400rub', reply_markup=shop_dazzle())

@router.callback_query(F.data == 'dazzle_back_to_shop')
async def dazzle_back_to_shop(callback: CallbackQuery):
    # Отправляем клавиатуру с товарами (shop)
    await callback.message.answer('Выберите товар:', reply_markup=get_products_keyboard())

    # Удаляем inline-клавиатуру
    await callback.message.edit_reply_markup(reply_markup=None)
    # Удаляем текст "Цена: 400rub"
    await callback.message.delete()

@router.callback_query(F.data == 'product_5')
async def product_5(callback: CallbackQuery):
   # Удаляем сообщение с командой /start
    await callback.message.delete()
    # Отправляем клавиатуру с товарами
    await callback.message.answer('Цена: 400rub', reply_markup=shop_dawnbreaker())

@router.callback_query(F.data == 'dawnbreaker_back_to_shop')
async def dawnbreaker_back_to_shop(callback: CallbackQuery):
    # Отправляем клавиатуру с товарами (shop)
    await callback.message.answer('Выберите товар:', reply_markup=get_products_keyboard())

    # Удаляем inline-клавиатуру
    await callback.message.edit_reply_markup(reply_markup=None)
    # Удаляем текст "Цена: 400rub"
    await callback.message.delete()

@router.callback_query(F.data == 'shop_back_to_main')
async def shop_back_to_main(callback: CallbackQuery):
    # Проверяем, существует ли сообщение
    if callback.message:
        await command_start_handler(callback.message)
        # Удаляем inline-клавиатуру
        await callback.message.edit_reply_markup(reply_markup=None)
        # Удаляем текст "Выберите товар:"
        await callback.message.delete()
#------------------------------------END SHOP-------------------------------

#------------------------------------PROFILE-----------------------------------
@router.callback_query(F.data == 'profile')
async def profile(callback: CallbackQuery):
    # Удаляем inline-клавиатуру
    await callback.message.edit_reply_markup(reply_markup=None)
#------------------------------------END PROFILE--------------------------------

#------------------------------------GUARANTEE----------------------------------
@router.callback_query(F.data == 'guarantee')
async def guarantee(callback: CallbackQuery):
    # Удаляем сообщение с командой /start
    await callback.message.delete()
    # Отправляем клавиатуру с товарами
    await callback.message.answer('Все отзывы находятся в нашем канале в разделе Наши контакты🎭', reply_markup=get_guarantee())

@router.callback_query(F.data == 'guarantee_back_to_main')
async def guarantee_back_to_main(callback: CallbackQuery):
    # Проверяем, существует ли сообщение
    if callback.message:
        await command_start_handler(callback.message)
        # Удаляем inline-клавиатуру
        await callback.message.edit_reply_markup(reply_markup=None)
        # Удаляем текст "Выберите товар:"
        await callback.message.delete()
#------------------------------------END GUARANTEE------------------------------

#------------------------------------CONTACTS----------------------------------
@router.callback_query(F.data == 'contacts')
async def contacts(callback: CallbackQuery):
    # Удаляем сообщение с командой /start
    await callback.message.delete()
    # Отправляем клавиатуру с товарами
    await callback.message.answer('👤Менеджер: @dtqwe\n📢Наш канал: @mellqweshop', reply_markup=get_contacts())

@router.callback_query(F.data == 'contacts_back_to_main')
async def contacts_back_to_main(callback: CallbackQuery):
    # Проверяем, существует ли сообщение
    if callback.message:
        await command_start_handler(callback.message)
        # Удаляем inline-клавиатуру
        await callback.message.edit_reply_markup(reply_markup=None)
        # Удаляем текст "Выберите товар:"
        await callback.message.delete()
#------------------------------------END CONTACTS------------------------------




