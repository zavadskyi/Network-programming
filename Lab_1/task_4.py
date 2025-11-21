from telethon import TelegramClient

api_id = 39887407
api_hash = '225908aa2a846035df7e44057d6fb270'

phone_number = '+38'
password_2fa = ''

client = TelegramClient('my_session', api_id, api_hash)

async def main():
    target_group = 'python'
    async for user in client.iter_participants(target_group, limit=10):
        print(f"{user.id} {user.first_name}")

    await client.send_message('me', 'Lab work done')
    print("Done")

client.start(phone=phone_number, password=password_2fa)

with client:
    client.loop.run_until_complete(main())