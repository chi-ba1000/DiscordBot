# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'xx'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「AAA」と発言したら「BBB」が返る処理
    if message.content == 'AAA':
        await message.channel.send('BBB')
    #CCCばーじょん
    if message.content == 'CCC':
	     await message.channel.send('DDD')
	#FFF
    if message.content == 'EEE':
	     await message.channel.send('FFF')
	# サーバーログを表示する
    if message.content == 'ろぐみせて':
      with open('C:/Users/Username/Desktop/minecraftBE/internalStorage/Dedicated_Server.txt','rb') as f:
         picture = discord.File(f)
         await message.channel.send(file=picture)
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)