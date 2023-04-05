times = ("Flamengo","Santos","Palmeiras","Gremio",
             "Atletico Paranaense", "São Paulo","Internacional",
             "Conrithians","Fortaleza","Goias","Bahia","Vasco",
             "Atletico Mineiro","Fluminense","Botafogo","Ceará",
             "Cruzeiro","CSA","Chapecoense","Avaí")
print (30*'=-')
print (f'Lista de times: {times}')
print (30*'=-')
print (f'Os cinco primeiros times são: {times[0:5]}')
print (30*'=-')
print (f'Os quatro últimos times são: {times[-4:]}')
print (30*'=-')
print(f'Times em ordem alfabética: {sorted(times)}')
print (30*'=-')
print (f'A chapecoense está na posição {times.index("Chapecoense")}')