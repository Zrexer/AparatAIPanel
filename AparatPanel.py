import CryptoX
import MyBaleCloud.balecloud as mb
import random
import platform

token = ""

green = "\033[92m"
yellow = "\033[93m"
lblack = "\033[90m"
white = "\033[00m"

t = """

{:<2}{:<2}{:<2}{:<6}{:<}{:<4}{:<}{:<2}
{:<2}{:<2}{:<2}{:<6}{:<}{:<6}{:<}{:<2}
{:<2}{:<2}{:<2}{:<6}{:<}{:<4}{:<}{:<2}
{:<2}{:<2}{:<2}{:<6}{:<}{:<7}{:<}{:<2}
{:<2}{:<2}{:<2}{:<6}{:<}{:<5}{:<}{:<2}
{:<2}{:<2}{:<2}{:<6}{:<}{:<4}{:<}{:<2}
""".format(lblack, "┌", green, "Created By", lblack, " ╔", yellow, "Host1let", lblack, "├", green, "Telegram", lblack, "   ╠", yellow, "Gnome_shell", lblack, "├", green, "Powered By", lblack, " ╠", yellow, "Python3.11", lblack, "├", green, "Node is", lblack, "    ╠", yellow, platform.node(), lblack, "├", green, "System is", lblack, "  ╠", yellow, platform.system(), lblack, "└", green, "Release is", lblack, " ╚", yellow, platform.release())

print(f"""{green}
         o           o__ __o     o__ __o   
        <|>         <|     v\   <|     v\  
        / \         / \     <\  / \     <\ 
      o/   \o       \o/     o/  \o/     o/ 
     <|__ __|>       |__  _<|/   |__  _<|/ 
     /       \       |           |         
   o/         \o    <o>         <o>        
  /v           v\    |           |         
 />             <\  / \         / \        
        {t}{white}
""")

msg_lis = []
emj_lis = ['🗿','🌪','🕰','👾','⌚️','🔦','⌛️','⏳','🧭','⏰','🔮','🏺','🔭','🔬','🕳','📿','🧿','💈','⚗️','📨']
danger_emj_lis = ['🅰️','🅱️','🆎','🅾️','🛑','⭕️','💢']

app = mb.BaleCloud(token)
hoyo = CryptoX.Client()

numberList = []
for i in range(100):
    numberList.append(str(i))

class loggers(object):
    def __init__(self, msg = None):
        self.msg = str(msg)
        
    @property
    def faild(self):
        return f"🔴Faild\nExample: {self.msg}"
    
    def unlocker() -> str:
        return "🔓"
    
    def locker() -> str:
        return "🔒"


def VIP():
    while 1:
        for msg in app.getUpdates_1():
            text = str(msg.text)
            chat = msg.chat_id
            msg_id = msg.message_id
            
            if not msg_id in msg_lis:
                msg_lis.append(msg_id)
                print(f"message: {text}")
                
                if text.startswith(("/start", "start", "/run", "run", "/help", "help")):
                    app.sendMessage("Will Be Soon", chat, msg_id)
                
                if text.startswith("/login"):
                    if len(text.split()) <= 2:
                        app.sendMessage(loggers("/login USERNAME PASSWORD => replace your username on 'USERNAME' and replace the password on 'PASSWORD'").faild, chat, msg_id)
                    else:
                        username = text.split()[1]
                        password = text.split()[2]
                        dataForLogin = hoyo.loginSession(username=username, password=password)['login']
                        dt = ""
                        for key, val in dataForLogin.items():
                            dt += "{} {:<5} ─> {:<}\n".format(random.choice(danger_emj_lis), str(key), str(val))
                        
                        app.sendMessage(f"{loggers.unlocker()}Request Received\n\n{dt}", chat, msg_id)
                
                if text.startswith("/get-username-videos"):
                    if len(text.split()) <= 1:
                        app.sendMessage(loggers("/get-username-videos USERNAME => replace username on 'USERNAME'").faild, chat, msg_id)
                        
                    else:
                        
                        
                        if not text.split()[1] in numberList:
                            username = text.split()[1]
                            dataForUserSearch = hoyo.getVideoByUsername(username)['videobyuser']
                            dt = ""
                            
                            for i in range(len(dataForUserSearch)) if not dataForUserSearch is None else []:
                                for key, val in dataForUserSearch[i].items():
                                    dt += "{} {:<5} ─> {:<}\n".format(random.choice(danger_emj_lis), str(key), str(val))
                            
                            app.sendMessage(f"{loggers.unlocker()}Request Received\n\n{dt}", chat, msg_id)
                            
                        else:
                            username = text.split()[2]
                            ppage = text.split()[1]
                            dataForUserSearch = hoyo.getVideoByUsername(username, ppage)['videobyuser']
                            dt = ""
                            
                            for i in range(len(dataForUserSearch)) if not dataForUserSearch is None else print("Is None") and []:
                                dt += "\n"+random.choice(emj_lis)+"-"*10+f"{i+1}"+"-"*10+random.choice(emj_lis)+"\n\n"
                                for key, val in dataForUserSearch[i].items():
                                    dt += "{} {:<5} ─> {:<}\n".format(random.choice(danger_emj_lis), str(key), str(val))
                            
                            app.sendMessage("{}Request Received\n\n{}".format(loggers.unlocker(), dt), chat, msg_id)

                if text.startswith("/get-profile-info"):
                    if len(text.split()) < 2:
                        app.sendMessage(loggers("/get-profile-info USERNAME => replace username on 'USERNAME'").faild, chat, msg_id)
                    else:
                        username = text.split()[1]
                        data = hoyo.getProfileInfoByUsername(username=username)['profile']
                        dt = ""
                        for key, val in data.items():
                            dt += "{} {:<5} ─> {:<}\n".format(random.choice(danger_emj_lis), str(key), str(val))
                            
                        app.sendMessage("{}Request Received\n\n{}".format(loggers.unlocker(), dt), chat, msg_id)
                
            else:
                msg_lis.append(msg_id)
                


if __name__ == "__main__":
    try:
        VIP()
    except KeyboardInterrupt:
        print("Exit by Client")
    
    except Exception as e:
        print(e)
        print("pass")
        pass
