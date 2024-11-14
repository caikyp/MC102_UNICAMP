dados = [
    {"dia": 12, "mes": 2, "ano": 2019, "temp" : 30.5},
    {"dia": 18, "mes": 3, "ano": 2019, "temp" : 29.1},
    {"dia": 22, "mes": 4, "ano": 2019, "temp" : 28.5},
    {"dia": 17, "mes": 5, "ano": 2019, "temp" : 26.4},
]

msg = "{0:02d}/{1:02d}/{2}: Tempoeratura: {3}C"
for dic in dados:
    print(msg.format(dic["dia"], dic["mes"], dic["mes"], dic["temp"]))




