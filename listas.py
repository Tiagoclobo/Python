agentes = ["007", "86", "19", "02"]
print(agentes)

agentes.append("13")
print("O agente 13 foi adicionado", agentes)

agentes.insert(0,"06")
print("Agora o agente numero 0 é o 06 {} ".format(agentes))

del agentes[4]
print("O agente numero 4 foi deletado", agentes)

agentes.remove("007")
print("O agente 007 foi removido", agentes)

agentes[2] = "96"
print("O agente numero 2 foi alterado, agora ele é o 96", agentes)


print("O {} é o agente numero 2 da lista. ".format(agentes[2]))


print("Existem {} agentes. ".format(len(agentes)))