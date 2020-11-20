### Exercício 06: Controle do Elevador
Elevadores são comuns em prédios. Para sua automação é importante conhecer o andar em que o elevador está, a quantidade de andares do prédio, a capacidade de pessoas suportada e a contagem de pessoas no elevador.
#### Regras
As ações típicas de um elevador são subir e descer.

Contudo, deve-se controlar a quantidade de pessoas que entram e saem do elevador, não permitindo exceder seu limite.

Também é importante controlar se o elevador já chegou ao térreo (andar 0) ou ao último andar do prédio.

Esses controles são realizados por meio da implementação de exceções.

Implemente as exceções esperadas e dispare as exceções nos momentos devidos.

**Não é necessário implementar o tratamento das exceções**, pois o código de testes do Moodle já implementa esses tratamentos.
#### Observações
Quando o controlador inicializar o elevador, é importante garantir que os parâmetros de inicialização sejam válidos. Existem 5 casos que podem invalidar o comando de inicialização:

1. Quando existe algum parâmetro que não é um valor inteiro.
2. Quando existe algum parâmetro com valor negativo.
4. Se o andar atual do elevador não respeita a restrição do número total de andares no prédio.
5. Se o número total de pessoas no elevador não respeita a restrição da capacidade máxima do elevador.

Quando qualquer um desses casos ocorrer, o comando de inicialização é considerado inválido e o elevador deve manter seu estado anterior.
#### Importante
Implemente o exercício seguindo exatamente as Classes disponibilizadas pelo professor. As Interfaces podem ser baixadas aqui: ```Classes Abstratas Exercício 06.```
