from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# 替换为你的 API Token
API_TOKEN = '8329743895:AAEqhWzIAeu3q_rCKh7KcfEMpNJJ66fsieQ'  # 请替换为你从 BotFather 获得的 Token

# 配置日志
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# 处理 /start 命令
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f"你好 {user.first_name}! 欢迎使用我的 Telegram 机器人！")

# 处理普通消息
def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text  # 获取用户发送的消息
    update.message.reply_text(f"你说: {user_message}")  # 回复相同的消息

# 处理错误
def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f"更新 {update} 引发错误 {context.error}")

# 发送消息的函数（可以在其他地方调用此函数来发送消息）
def send_message(chat_id: int, text: str) -> None:
    bot = context.bot
    bot.send_message(chat_id=chat_id, text=text)

# 主函数
def main():
    # 创建 Updater 对象并传入 API Token
    updater = Updater(API_TOKEN, use_context=True)

    # 获取调度器和分发器
    dp = updater.dispatcher

    # 注册命令处理器
    dp.add_handler(CommandHandler("start", start))

    # 注册消息处理器
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # 错误日志
    dp.add_error_handler(error)

    # 启动机器人
    updater.start_polling()

    # 保持机器人运行
    updater.idle()

# 启动主程序
if __name__ == '__main__':
    main()
