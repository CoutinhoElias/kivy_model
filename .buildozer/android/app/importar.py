import xmltodict

handle = open("13190402419765001915650020000589401000589409.xml","r")

content = handle.read()

#print(content)
d = xmltodict.parse(content)

print('-----------------------------ID NFE-----------------------------')
print(d['nfeProc']['NFe']['infNFe']['ide']['natOp'])
print(d['nfeProc']['NFe']['infNFe']['ide']['cNF'])
print(d['nfeProc']['NFe']['infNFe']['ide']['nNF'])
print(d['nfeProc']['NFe']['infNFe']['ide']['dhEmi'])

print('-----------------------------EMITENTE DA NFE-----------------------------')
print(d['nfeProc']['NFe']['infNFe']['emit']['CNPJ'])
print(d['nfeProc']['NFe']['infNFe']['emit']['xNome'])
print(d['nfeProc']['NFe']['infNFe']['emit']['xFant'])
