def notas(*notas,sit=False):
    dic = {}
    dic["total"] = len(notas)
    dic["maior"] = max(notas)
    dic["menor"] = min(notas)
    dic["média"] = sum(notas) / len(notas)
    if sit:
        if dic["média"] < 6:
            dic["situação"] = "RUIM"
        else:
            dic["situação"] = "BOA"
    return dic

resp = notas(9,10,6.5,sit=True)
print(resp)

    