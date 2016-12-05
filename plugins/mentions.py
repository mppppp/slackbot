from slackbot.bot import respond_to

@respond_to('疲れた')
@respond_to('つかれた')
def cheer(message):
    import random
    msg = ["本当にお疲れさま","よく頑張ってるね、偉いね","あまり無理せず自分を大事にしろよ","今日はご飯作ってあげるから、ゆっくりしてて","辛かったら辞めていいよ。面倒を見てあげるから"]
    one_msg = random.choice(msg)
    message.reply(one_msg)

