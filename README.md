### Python 3

Python é uma linguagem de programação interpretada de alto nível e que suporta múltiplos paradigmas de programação: imperativo, orientado a objetos e funcional. É uma linguagem com tipagem dinâmica e gerenciamento automático de memória.

Isso significa que a implementação da linguagem python em cada computador é feita através de um processo no qual um dos principais componentes é o interpretador.

Python foi idealizado pelo programador holandês Guido Van Hossum e sua primeira versão foi lançada em 1991 no Centrum Wiskunde & Informatica - CWI (Instituto Nacional de Pesquisa para Matemática e Ciência da Computação), na Holanda.

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
- sep e end entraram no Python 3. <br>
- raw_input converte para string no Python 2. <br>
- As funções input(...), print(...) e int(...) existem no Python 3. <br>
- A função raw_input(..) existe apenas no Python 2. <br>
- No Python 3, a instrução print("ola", "mundo") imprime como saída ola mundo, diferente do Python 2, que possui como saída ('ola', 'mundo'). <br>
- No Python 2, quando digitamos um valor numérico através de input, ele automaticamente converte de str para int. Já o Python 3 não assume essa conversão automática, sendo o desenvolvedor responsável por fazê-la. <br>
- A função raw_input só existe em Python 2 e quando usada, lê a entrada como str, sem realizar conversões de tipos, como na função input. <br>
- Uma função em Python 3 sempre deve possuir parênteses.

##### syntax sugar
```python
10 * "20"
```
<pre>Retorno: '20202020202020202020'</pre>

```python
for rodada in range(1,10):
    print(rodada)
```
<pre>
1
2
3
4
5
6
7
8
9
</pre>

range(start, stop, [step]) -> step é opcional.
```python
for rodada in range(1,10,2):
    print(rodada)
```
<pre>
1
3
5
7
9
</pre>

```python
for rodada in [1,2,3,4]:
    print(rodada)
```
<pre>
1
2
3
4
</pre>

##### break e continue
break sai do bloco do laço abruptamente, continue apenas pula para próxima iteração.

f -> float, d -> int/digito
```python
print("R$ {:07.2f}".format(4.5))
print("R$ {:7d}".format(45))
print("Data {:2d}/{:2d}".format(9,12))
```

```python
print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))
```
<pre>Retorno: "Ola Sr. Leonardo Cordeiro"</pre>

##### f-strings ou formatted string literals
```python
>>> nome = 'Lucas'
>>> print(f'Meu nome é {nome}')
Meu nome é Lucas
```

Quando colocamos a letra f antes das aspas, informamos ao Python que estamos utilizando uma f-string. Dessa forma o Python consegue, em tempo de execução, captar a expressão que está entre chaves ({ }) e avaliá-la. <br>
Além de variáveis, podemos passar também de funções e métodos:
```python
>>> nome = 'Lucas'
>>> print(f'Meu nome é {nome.lower()}')
Meu nome é Lucas
```

[Built-in Functions](https://docs.python.org/3/library/functions.html) <br>
Estão automaticamente disponíveis e podem ser chamadas em todo lugar do nosso código.

##### Integer Division
<pre>
3 / 2
Retorno: 1.5

3 // 2
Retorno: 1
</pre>

Mesmo um módulo solitário pode executar alguma funcionalidade quando executado isoladamente, basta adicionar um if no final do código para verificar a variável __name__
```python
def executa():
    print("Executando")

if(__name__ == "__main__"):
    executa()
```

* [Estruturas de Dados](https://docs.python.org/pt-br/3.10/tutorial/datastructures.html) <br>
strip() - Tira espaços em branco e caracteres especiais. <br>
Listas [] - Mutável <br>
Tuplas () - Imutável <br>
readline() - Se desejamos ler linha a linha de nosso arquivo, podemos utilizar a função readline(). Ela nos retorna uma linha por vez, e faz com que a nossa leitura seja feita de modo mais controlado. <br>
read() - Lê o arquivo inteiro de uma vez, colocando o ponteiro de leitura no final do mesmo. Se chamarmos a função read() novamente, como o ponteiro de leitura está no final, nada será lido. <br>
len() - Para saber o tamanho.

**Tipos considerados sequências:** tuple, string e list.