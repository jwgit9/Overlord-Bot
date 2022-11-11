#basic calendar json cog
#allows users to add/view/remove events from a calendar

from cogs.calendar.calendarv2_functions import CalHelperJson
from discord.ext import commands

class CalendarJson(commands.Cog, name="Calendarv2"):
    def __init__(self, bot):
        self.bot = bot
        self.calhelper = CalHelperJson(bot)

    @commands.command(
        name="calendarv2",
        help="Add or view events on the calendar! Usage: !calendarv2 <add> <event> <date as in MM/DD/YYYY> or !calendarv2 <clear> or !calendarv2 <view> or !calendarv2 remove <MM/DD/YYYY>"
    )
    async def calendar(self, context, action: str, *, event: str = None, date: str = None):
        """Adds or views events in the calendar. Usage: !calendar <add/remove> <event> <date as in MM/DD/YYYY> or !calendar <view/clear> <week/month>"""
        user_id = str(context.message.author.id)
        user_name = str(context.message.author.name)
        if action.lower() == "add":
            if event:
                await context.send(embed=self.calhelper.print_add_embed(event, user_id))
            else:
                await context.send("Please specify an event.")

        elif action.lower() == "clear":
            await context.send(embed=self.calhelper.print_clear_json())

        elif action.lower() == "view":
            await context.send(embed=self.calhelper.print_view_embed(user_id, user_name))
        
        elif action.lower() == "remove":
            if event:
                await context.send(embed=self.calhelper.print_remove_embed(event, user_id))
            else:
                await context.send("Please specify an event.")

        elif action.lower() == "edit":
            if event:
                temp = str(event.split(" ")[0])
                new_event = event[len(temp)+1:]
                if temp.lower() == "date":
                    await context.send(embed=self.calhelper.edit_date(new_event, user_id))
                elif temp.lower() == "event":
                    await context.send(embed=self.calhelper.edit_event(new_event, user_id))
                elif temp.lower() == "both":
                    pass
            else:
                await context.send("Please specify an event.")
        else:
            await context.send("Please specify an action.")

async def setup(bot):
    await bot.add_cog(CalendarJson(bot))
    