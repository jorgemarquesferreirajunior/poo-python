class CarrinhoDeCompras:
    def __init__(self) -> None:
        self._produtos = []
        
    def total(self):
        return round(sum([p.preco for p in self._produtos]), 2)
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print('')
    
    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)
            
            
class Produtos:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco
        
carrinho = CarrinhoDeCompras()
p1, p2 = Produtos('Caneta', 1.54), Produtos('Estojo', 9.99)

carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())
