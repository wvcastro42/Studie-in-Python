import datetime

di = int(input().split()[1])
hi, mi, si = (map(int, input().split(':')))

df = int(input().split()[1])
hf, mf, sf = (map(int, input().split(' : ')))
# fmt = '%H:%M:%S'
delta1 = datetime.timedelta(days=(df-di), hours=(hf-hi), minutes=(mf-mi), seconds=(sf-si))

# t1 = str(hi) + str(mi) + str(si)
# t2 = str(hf) + str(mf) + str(sf)

# print(delta1.days)
# print(delta1.seconds)
tempo_dias = int(delta1.total_seconds()/60/60/24)
tempo_horas = (((delta1.total_seconds()/60/60/24) - tempo_dias) * 24)
tempo_minutos = ((((delta1.total_seconds()/60/60/24) - tempo_dias) * 24)-tempo_horas)
print(tempo_horas)

# tdelta = datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)
#
#
# print(delta1.days)
# print(tdelta.seconds)


# dias = df - di
#
# horas = hf - hi
# if (horas < 0):
#     horas += 24
#     dias -= 1
#
# minutos = mf - mi
# if (minutos < 0):
#     minutos += 60
#     horas -= 1
#
# segundos = sf - si
# if (segundos < 0):
#     segundos += 60
#     minutos -= 1
#
#
# print(f'{dias} dia(s)')
# print(f'{horas} hora(s)')
# print(f'{minutos} minuto(s)')
# print(f'{segundos} segundo(s)')
