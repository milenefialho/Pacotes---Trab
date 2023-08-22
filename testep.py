from graphicsmilens import Graficos

#barra

#aux = Graficos('testbar.csv')

#aux.barra('coluna1','coluna2',legenda = 'x', tit = 'x' , xlabel = 'x', ylabel = 'y') 


#pizza

aux2 = Graficos('testpiz.csv')

#cores = ['red','green','black','pink','blue'] 
labels = [r'vendas', r'gastos',r'despesas', r'imoveis',r'aluguel']


aux2.pizza('coluna1','Gráfico de Vendas Lanchonete UFPI',labels,cores='-')

#ponto

#aux3 = Graficos('test.csv')
#aux3.ponto('coluna1','coluna2',legenda='vendas',tit='Grafico de Ponto',xlabel='x',ylabel='y')

#linhas

#ponto

#aux4 = Graficos('test.csv')

#aux4.linha('coluna1','coluna2',legenda='vendas',tit='Grafico de Ponto',xlabel='x',ylabel='y')