from schedule.schedule import Schedule

with Schedule() as bot:
  bot.logging()
  bot.horario_tienda(region = "Costa Norte", LN = "José Cedeño", tienda = "1090-FY")

