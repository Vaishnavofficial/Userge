from pyrogram import filters

from userge import userge


@userge.on_message(filters.command('block', '?'))
async def block(userge, message):
      if message.reply_to_message:
         ban_id = message.reply_to_message.from_user.id
         await userge.block_user(ban_id)
         await message.edit("`Haa! Blocked that user`")
      else:
          args = message.text.split(None, 1)
          ban_name = args[1]
          await userge.block_user(ban_name)
          await message.edit("Blocked that user")
 
@userge.on_message(filters.command('unblock', '?', about={
    'header': "Globally Ban A User",
    'description': "Adds User to your blocked users List. "
                   "Blocks the user and prevents him from pm ing you. "
                   "[NOTE: Works only in groups..]",))
async def unblock(bot, message):
    try:
      if message.reply_to_message:
         ban_id = message.reply_to_message.from_user.id
         await bot.unblock_user(ban_id)
         await message.edit("`Haa! Unblocked that user`")
      else:
         args = message.text.split(None, 1)
         ban_name = args[1]
         await userge.unblock_user(ban_name)
         await message.edit("Unblocked that user")
    except Exception as e:
         await message.edit("Something went wrong! Check app logs")
         print(e)
