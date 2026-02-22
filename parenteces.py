def verificar_parenteses(text):
    text_parenteses = [l for l in text if l in '()']
    indexes = []
    for i, parentece1 in enumerate(text_parenteses):
        if parentece1 == '(':
            achou = False
            pula = 0
            for j, parentece2 in enumerate(text_parenteses[i+1:], i+1):
                if parentece2 == ')':
                    if pula > 0:
                        pula -= 1
                    else:
                        achou = True
                        indexes.append((i, j))
                        break
                elif parentece2 == '(':
                    pula += 1
            if not achou: 
                return False
    if len(indexes) * 2 != len(text_parenteses):
        return False
    return True

print(verificar_parenteses('((()))')) # True
print(verificar_parenteses('(()())')) # True
print(verificar_parenteses('(()')) # False
print(verificar_parenteses('())')) # False