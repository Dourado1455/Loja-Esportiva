from django.db import models

# Modelo de Produtos
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.CharField(max_length=255)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# Modelo de Nota Fiscal
class NotaFiscal(models.Model):
    numero = models.CharField(max_length=50, unique=True)
    data_emissao = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='ItemNotaFiscal')

    def __str__(self):
        return f"NF {self.numero}"


# Modelo de Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# Modelo de Fornecedor
class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    endereco = models.TextField()

    def __str__(self):
        return self.nome


# Modelo de Funcionário
class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_admissao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# Modelo Intermediário para a relação entre Produto e Nota Fiscal (Produto na NF)
class ItemNotaFiscal(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nota_fiscal = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"
