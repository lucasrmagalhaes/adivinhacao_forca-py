### Python 3 parte 1: Introdução à nova versão da linguagem.

[Python](https://www.python.org/) <br>
[Replit](https://replit.com/languages/python3)

```python
print("olá mundo")
```

Inicializa a ajuda, para sair utilizar "q" ou Ctrl + c <br>
Por exemplo, digitar "print" para obter o retorno da função help
```python
help()
```

sep -> para definir um - entre cada valor.
```python
print("Brasil", "ganhou", 5, "títulos mundiais", sep="-")
```
<pre>Retorno: Brasil-ganhou-5-títulos mundiais</pre>

end -> adiciona uma intrução no final do código. <br>
\n -> é um caractere especial, que faz com que o novo prompt comece em uma nova linha.
```python
print("Brasil", "ganhou", 5, "títulos mundiais", end="\n")
```
<pre>
Brasil ganhou 5 títulos mundiais

</pre>

```python
pais = "Itália"
```

```python
type(pais)
```

```python
type(pais)
```

```python
quantidade = 4
```

```python
type(quantidade)
```

```python
print(pais, "ganhou", quantidade, "titulos mundiais")
```
<pre>Retorno: Itália ganhou 4 títulos mundiais</pre>

Imprimindo uma data
```python
dia = 15
```
```python
mes = 10
```
```python
ano = 2015
```
```python
print(dia, mes, ano, sep="/")
```
<pre>Retorno: 15/10/2015</pre>

Tipagem dinâmica - Uma variável só passa a existir quando atribuímos um valor, definindo assim o seu tipo.
```python
pais = "Brasil"
```
```python
pais = 644
```
```python
pais = 7.9
```

O Python utiliza por convenção o padrão Snake_Case para nomes de variáveis (ou identificadores).
```python
idade_esposa = 20
perfil_vip = 'Flávio Almeida'
recibos_em_atraso = 30
```

[PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows)

O código não funciona! <br>
unsupported operand type(s) for +: 'int' and 'str'
```python
idade1 = 10
idade2 = "20"

print(idade1 + idade2)
```

Funciona
```python
idade1 = 10
idade2 = int("20")

print(idade1 + idade2)
```