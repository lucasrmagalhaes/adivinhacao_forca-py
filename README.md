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

Soma de duas strings
```python
nome = "Nico"
sobrenome = "Steppat"

print(nome + sobrenome)
```
<pre>Retorno: NicoSteppat</pre>

##### Diferenças Python 2 e 3
sep e end entraram no Python 3. <br>
raw_input converte para string no Python 2. <br>
As funções input(...), print(...) e int(...) existem no Python 3. <br>
A função raw_input(..) existe apenas no Python 2. <br>
No Python 3, a instrução print("ola", "mundo") imprime como saída ola mundo, diferente do Python 2, que possui como saída ('ola', 'mundo'). <br>
No Python 2, quando digitamos um valor numérico através de input, ele automaticamente converte de str para int. Já o Python 3 não assume essa conversão automática, sendo o desenvolvedor responsável por fazê-la. <br>
A função raw_input só existe em Python 2 e quando usada, lê a entrada como str, sem realizar conversões de tipos, como na função input. <br>
Uma função em Python 3 sempre deve possuir parênteses.

##### syntax sugar
```python
10 * "20"
```
<pre>Retorno: '20202020202020202020'</pre>