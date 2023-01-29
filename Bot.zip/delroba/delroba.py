#pylint:disable=E0001
#source delroba build in team arianbot

from arsein import Messenger
from arsein.Zedcontent import Antiadvertisement
from Api import api_text
import asyncio
from time import sleep

#meghdars

auth = "jofgzcbvtybynilgebihjplfqkfezjgx"

Gap = "g0BnqKo05ef1d5c18ddf6abb151e7f8a"

app,zed = Messenger(auth),Antiadvertisement(auth)

limsg,hoshdar,zedtab,deleteChat,One = [],[],False,True,True


while 1:
	try:
		GetAdmin = [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]
		listblockGroup = [karbar["member_guid"] for karbar in app.getbanGroupUsers(Gap)["data"]["in_chat_members"]]
		message = app.getChatGroup(Gap)
		for msg in message:

			#Clean group
			if deleteChat != False:
				try:
					print("Ok clear chat group")
					app.deleteChatHistory(Gap,msg['message_id'])
					deleteChat = False
					sleep("5")
				except:
					continue

			elif deleteChat == False:
				...

			if not msg['message_id'] in limsg:
				
				# zedlink and forwards
				if zedtab == True:
					try:
						forward = zed.Anti("forward",Gap,msg)
						linkide = zed.Anti("link",Gap,msg)
						if forward == "delete forward" or linkide == "delete link":
							print("Ok delete link or forwards")
						else:...
					except:
						continue

				elif zedtab == False:
					...
			if msg["type"] == 'Text' and not msg['message_id'] in limsg:
				print(f"message: {msg['text']}")
				limsg.append(msg['message_id'])

				# zedlink and forwards
				if msg.get("text") == "لینکیان نارد حذف که" and msg.get("author_object_guid") in GetAdmin:
					zedtab = True
					app.sendMessage(Gap,"بچاوان",message_id = msg['message_id'])

				elif msg.get("text") == "/zedlinkOff" and msg.get("author_object_guid") in GetAdmin:
					zedtab = False
					app.sendMessage(Gap,"ضد لینک و فوروارد با موفقیت خاموش شد",message_id = msg['message_id'])

				        #Words
				elif msg.get("text") == "سلام" or msg.get("text") == "سلم" or msg.get("text") == "سیلام" or msg.get("text") == "صلوم" or msg.get("text") == "سلوم" or msg.get("text") == "صیلام"  or msg.get("text") == "صل" or msg.get("text") == "سل" or msg.get("text") == "ثل" or msg.get("text") == "ثلام" or msg.get("text") == "شلام" or msg.get("text") == "شلوم" or msg.get("text") == "صلام" or msg.get("text") == "صلم" and One == True:
					try:
						getname = app.getUserInfo(msg["author_object_guid"])["data"]["user"]["first_name"]
						app.sendMessage(Gap,f"بخیری {getname}",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "باشی" or msg.get("text")=="بشی"and One == True:
					try:
						app.sendMessage(Gap,"باشم اتوش هر باش بی",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "چدکی" or msg.get("text")=="چدکی"and One == True:
					try:		

              
						app.sendMessage(Gap,"کابلمی له ددم",message_id = msg['message_id'])
					except:
						continue
						
				elif msg.get("text") == "ممنون" or msg.get("text")=="قوربانت" or msg.get("text")=="بوس" or msg.get("text")=="ممنان" and One == True:
					try:
						app.sendMessage(Gap,"ماچت دکم",message_id = msg['message_id'])
					except:
						continue
				
						
				elif msg.get("text") == "چونی" or msg.get("text")=="چنی"and One == True:
					try:
						app.sendMessage(Gap,"باشم اتوش هر باش بی",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "لسر چه" or msg.get("text")=="لسر چه؟"  or msg.get("text")=="لسرچه؟" and One == True:
					try:
						app.sendMessage(Gap,"لسر او کچانی گروهی ",message_id = msg['message_id'])
					except:
						continue		
		 
				elif msg.get("text") == "/sohayb" and One == True:
					try:
						app.sendMessage(Gap,"صهیب 18 ربط ",message_id = msg['message_id'])
					except:
						continue
						
				elif msg.get("text") == "خداحافظ" or msg.get("text") == "بای" and One == True:
					try:
						app.sendMessage(Gap,"سر چیرم",message_id = msg['message_id'])
					except:
						continue
			
				elif msg.get("text") == "ربات" or msg.get("text") == "رباط" and One == True:
					try:
						app.sendMessage(Gap,"جیانه",message_id = msg['message_id'])
					except:
						continue
		
				elif msg.get("text") == "/help" and One == True:
					try:
						file = open("help_admin.txt",'r',encoding ='utf-8').read()
						app.sendMessage(Gap,str(file),message_id = msg['message_id'])
						print("Ok sended Help bot")
						file.close()
					except:
						continue
				
	

						#dastor API
				elif msg.get("text") == "/jok" and One == True:
					try:
						jok = asyncio.get_event_loop().run_until_complete(api_text("https://api.codebazan.ir/jok/json/","json"))["result"]["jok"]
						app.sendMessage(Gap,jok,message_id = msg['message_id'])
					except:
						continue
               
				elif msg.get("text") == "/bio" and One == True:
					try:
						bio = asyncio.get_event_loop().run_until_complete(api_text("https://api.codebazan.ir/bio/","text"))
						app.sendMessage(Gap,bio,message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/time" and One == True:
					try:
						time = asyncio.get_event_loop().run_until_complete(api_text("https://dxprit-gif-photo-audio-film-your-sexy.github.io/salam.12.in/","text"))
						app.sendMessage(Gap,time,message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/alaki" and One == True:
					try:
						alaki = asyncio.get_event_loop().run_until_complete(api_text("http://api.codebazan.ir/jok/alaki-masalan/","text"))
						app.sendMessage(Gap,alaki,message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/danesh" and One == True:
					try:
						danesh = asyncio.get_event_loop().run_until_complete(api_text("http://api.codebazan.ir/danestani/","text"))
						app.sendMessage(Gap,danesh,message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/hadis" and One == True:
					try:
						hadis = asyncio.get_event_loop().run_until_complete(api_text("http://api.codebazan.ir/hadis/","text"))
						app.sendMessage(Gap,hadis,message_id = msg['message_id'])
					except:
						continue


						#dastor admins
				elif msg.get("text") == "/cleanlist" and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						for guid in listblockGroup:
							app.unbanGroupMember(Gap,guid)
						print("Ok clean list dark group")
						app.sendMessage(Gap,"لیست سیاه گروه با موفقیت خالی شد",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/warning" and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						if "reply_to_message_id" in msg:
							getguid = app.getMessagesInfo(Gap, [msg.get("reply_to_message_id")])["data"]["messages"][0]["author_object_guid"]
							if not getguid in GetAdmin and hoshdar.count(getguid) != 2:
								hoshdar.append(getguid)
								app.sendMessage(Gap,"کاربر گرامی شما اخطار دریافت کردید بعد از دریافت ۲ اخطار از گروه حذف خواهید شد",Type = "MentionText",Guid_mention = getguid,message_id = msg['message_id'])
								if hoshdar.count(getguid) == 2:
									app.sendMessage(Gap,"بدلیل رعایت نکردن قوانین هم اکنون حذف خواهید شذ",message_id = msg['message_id'])
									app.banGroupMember(Gap,getguid)
									print("Ok remove by warning with replay")
								else:...
							else:
								app.sendMessage(Gap,"این کاربر آدمین گروه می باشد",message_id = msg['message_id'])
						elif "@" in msg.get("text"):
							getusername = msg.get("text").split("/warning")[1].replace("@","")
							getguid = app.getInfoByUsername(getusername)["data"]["user"]["user_guid"]
							if not getguid in GetAdmin and hoshdar.count(getguid) != 2:
								hoshdar.append(getguid)
								app.sendMessage(Gap,"کاربر گرامی شما اخطار دریافت کردید بعد از دریافت ۲ اخطار از گروه حذف خواهید شد",Type = "MentionText",Guid_mention = getguid,message_id = msg['message_id'])
								if hoshdar.count(getguid) == 2:
									app.sendMessage(Gap,"بدلیل رعایت نکردن قوانین هم اکنون حذف خواهید شذ",message_id = msg['message_id'])
									app.banGroupMember(Gap,getguid)
									print("Ok remove by warning with ide")
								else:...
							else:
								app.sendMessage(Gap,"این کاربر آدمین گروه می باشد",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/One" and msg.get("author_object_guid") in GetAdmin:
					try:
						if One == False:
							One = True
							app.sendMessage(Gap,"با موفقیت روشن شد",message_id = msg['message_id'])
						else:
							app.sendMessage(Gap,"خطا: ربات از قبل روشن است",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/Off" and msg.get("author_object_guid") in GetAdmin:
					try:
						if One == True:
							One = False
							app.sendMessage(Gap,"با موفقیت خاموش شد",message_id = msg['message_id'])
						else:
							app.sendMessage(Gap,"خطا: ربات از قبل خاموش است",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/lock" and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						app.lockGroup(Gap)
						print("Ok locked group")
						app.sendMessage(Gap,"گروه با موفقیت بسته شد",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/unlock" and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						app.unlockGroup(Gap)
						print("Ok unlocked group")
						app.sendMessage(Gap,"گروه با موفقیت باز شد",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text").startswith("/timer") and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						time = msg.get("text").split("/timer")[-1]
						app.setGroupTimer(Gap,time)
						print("Ok timer group")
						app.sendMessage(Gap,f"تایمر گروه بر روی   {time}قرار گرفت",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/pin" and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						if "reply_to_message_id" in msg:
							app.pin(Gap,msg.get("reply_to_message_id"))
							print("Ok pin message in group")
							app.sendMessage(Gap,"با موفقیت سنجاق شد",message_id = msg["reply_to_message_id"])
						else:
							app.sendMessage(Gap,"نحوه ارسال دستور استباه است!",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/unpin" and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						if "reply_to_message_id" in msg:
							app.unpin(Gap,msg.get("reply_to_message_id"))
							print("Ok unpin message in group")
							app.sendMessage(Gap,"با موفقیت سنجاق حذف شد",message_id = msg["reply_to_message_id"])
						else:
							app.sendMessage(Gap,"نحوه ارسال دستور استباه است!",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text").startswith("/ban") and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						if "reply_to_message_id" in msg:
							getguid = app.getMessagesInfo(Gap, [msg.get("reply_to_message_id")])["data"]["messages"][0]["author_object_guid"]
							if not getguid in listblockGroup:
								app.banGroupMember(Gap,getguid)
								print("Ok remove with replay")
								app.sendMessage(Gap,"کاربر مورد نظر با موفقیت حذف شد",message_id = msg['message_id'])
							else:
								app.sendMessage(Gap,"این کاربر قبلا از گروه حذف شده است",message_id = msg['message_id'])
						elif "@" in msg.get("text"):
							getusername = msg.get("text").split("/ban")[1].replace("@","")
							getguid = app.getInfoByUsername(getusername)["data"]["user"]["user_guid"]
							if not getguid in listblockGroup:
								app.banGroupMember(Gap,getguid)
								print("Ok remove with username")
								app.sendMessage(Gap,"کاربر مورد نظر با موفقیت حذف شد",message_id = msg['message_id'])
							else:
								app.sendMessage(Gap,"این کاربر قبلا از گروه حذف شده است",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text").startswith("/unban") and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						if "reply_to_message_id" in msg:
							getguid = app.getMessagesInfo(Gap, [msg.get("reply_to_message_id")])["data"]["messages"][0]["author_object_guid"]
							if getguid in listblockGroup:
								app.unbanGroupMember(Gap,getguid)
								print("Ok unbanGroup with replay")
								app.sendMessage(Gap,"کاربر مورد نظر با موفقیت از لیست سیاه برداشته شد",message_id = msg['message_id'])
							else:
								app.sendMessage(Gap,"این کاربر قبلا از لیست سیاه خارج شده است",message_id = msg['message_id'])
						elif "@" in msg.get("text"):
							getusername = msg.get("text").split("/unban")[1].replace("@","")
							getguid = app.getInfoByUsername(getusername)["data"]["user"]["user_guid"]
							if getguid in listblockGroup:
								app.unbanGroupMember(Gap,getguid)
								print("Ok unbanGroup with usernam")
								app.sendMessage(Gap,"کاربر مورد نظر با موفقیت از لیست سیاه برداشته شد",message_id = msg['message_id'])
							else:
								app.sendMessage(Gap,"این کاربر قبلا از لیست سیاه خارج شده است",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/changelink" and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						link = app.changeGroupLink(Gap)
						print(f"Ok change in link group: {link}")
						app.sendMessage(Gap,"لینک گروه با موفقیت عوض شد",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/delete" and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						if "reply_to_message_id" in msg:
							app.deleteMessages(Gap,[msg.get("reply_to_message_id")])
							print("Ok delete message with replay")
							app.sendMessage(Gap,"مسیج مورد نظر با موفقیت حذف شد",message_id = msg['message_id'])
						else:
							app.sendMessage(Gap,"نحوه ارسال دستور استباه است!",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text") == "/link" and One == True:
					try:
						link = app.getGroupLink(Gap)
						app.sendMessage(Gap,f"link my group:\n\n{link}",message_id = msg['message_id'])
						print(f"Ok get your link group: {link}")
					except:
						continue

				elif msg.get("text").startswith("/admin") and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						if "reply_to_message_id" in msg:
							getguid = app.getMessagesInfo(Gap, [msg.get("reply_to_message_id")])["data"]["messages"][0]["author_object_guid"]
							if not getguid in GetAdmin:
								app.setGroupAdmin(Gap,getguid)
								print("Ok setGroupAdmin with replay")
								app.sendMessage(Gap,f"کاربر مورد نظر با موفقیت آدمین شد",message_id = msg['message_id'])
							else:
								app.sendMessage(Gap,f"این کاربر از قبل آدمین می باشد",message_id = msg['message_id'])
						elif "@" in msg.get("text"):
							getusername = msg.get("text").split("/admin")[1].replace("@","")
							getguid = app.getInfoByUsername(getusername)["data"]["user"]["user_guid"]
							if not getguid in GetAdmin:
								b = app.setGroupAdmin(Gap,getguid)
								print("Ok setGroupAdmin with username")
								app.sendMessage(Gap,f"کاربر مورد نظر با موفقیت آدمین شد",message_id = msg['message_id'])
							else:
								app.sendMessage(Gap,f"این کاربر از قبل آدمین می باشد",message_id = msg['message_id'])
					except:
						continue

				elif msg.get("text").startswith("/unadmin") and msg.get("author_object_guid") in GetAdmin and One == True:
					try:
						if "reply_to_message_id" in msg:
							getguid = app.getMessagesInfo(Gap, [msg.get("reply_to_message_id")])["data"]["messages"][0]["author_object_guid"]
							if getguid in GetAdmin:
								b = app.deleteGroupAdmin(Gap,getguid)
								print("Ok deleteGroupAdmin with replay")
								app.sendMessage(Gap,f"کاربر مورد نظر با موفقیت از آدمینی برداشته شد",message_id = msg['message_id'])
							else:
								app.sendMessage(Gap,f"این کاربر قبلا از ادمینی برداشته شده است",message_id = msg['message_id'])
						elif "@" in msg.get("text"):
							getusername = msg.get("text").split("/unadmin")[1].replace("@","")
							getguid = app.getInfoByUsername(getusername)["data"]["user"]["user_guid"]
							if getguid in GetAdmin:
								b = app.deleteGroupAdmin(Gap,getguid)
								print("Ok deleteGroupAdmin with username")
								app.sendMessage(Gap,f"کاربر مورد نظر با موفقیت از آدمینی برداشته شد",message_id = msg['message_id'])
							else:
								app.sendMessage(Gap,f"این کاربر قبلا از ادمینی برداشته شده است",message_id = msg['message_id'])
					except:
						continue


					#khosh new user group
			elif msg.get("type") == "Event" and not msg['message_id'] in limsg:
				try:
					print("message glass")
					limsg.append(msg['message_id'])
					if msg.get("event_data").get("type") == "JoinedGroupByLink" and One == True:
						app.sendMessage(Gap,"بخیری بو گروهی گه‌وره پیاوکان",message_id = msg['message_id'])

					elif msg.get("event_data").get("type") == "RemoveGroupMembers" and One == True:
						app.sendMessage(Gap,"جارکی که بیوه به قون حاملت دکم",message_id = msg['message_id'])

					elif msg.get("event_data").get("type") == "AddedGroupMembers" and One == True:
						app.sendMessage(Gap,"بخیری بو گروهی گه‌وره پیاوکان",message_id = msg['message_id'])

					elif msg.get("event_data").get("type") == "LeaveGroup" and One == True:
						app.sendMessage(Gap,"بابت دجیم بو لفت ددی",message_id = msg['message_id'])
				except:
					continue
	except:
		continue