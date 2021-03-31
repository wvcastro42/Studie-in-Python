

def ip_ok(ip):
    ip = ip.split(".")
    for byte in ip:
        if int(byte) > 255:
            return False
    return True

ips = open('ips.txt', 'r')
invalidos = open('ips_nao_validos.txt', 'w')
validos = open('ips_validos.txt', 'w')

for linha in ips.readlines():
    if ip_ok(linha):
        validos.write(linha)
    if not ip_ok(linha):
        invalidos.write(linha)


ips.close()
invalidos.close()
validos.close()
print('Arquivos prontos...')
