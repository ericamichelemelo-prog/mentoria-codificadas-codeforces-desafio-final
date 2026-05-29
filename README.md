# Desafio Codeforces - Mentoria Codificadas | Além do Código

## Sobre este repositório

Este repositório contém a minha jornada de aprendizado em Python e Inteligência Artificial. Aqui estão as resoluções de 4 desafios da plataforma Codeforces, onde cada linha de código representa uma superação na minha lógica de proigramação.

---

## Problemas Escolhidos

| # | Nome do Problema | Link | Dificuldade |
|---|------------------|------|-------------|
| 1 | Watermelon (4A) | [Ver no Codeforces](https://codeforces.com/problemset/problem/4/A) | 800 |
| 2 | Even Odds (318A) | [Ver no Codeforces](https://codeforces.com/problemset/problem/318/A) | 900 |
| 3 | Way Too Long Words (71A) | [Ver no Codeforces](https://codeforces.com/problemset/problem/71/A) | 800 |
| 4 | Taxi (158B) | [Ver no Codeforces](https://codeforces.com/problemset/problem/158/B) | 1100 |

---

## Minha Experiência com os Problemas

### Problema 2: Even Odds (318A) - O Grande Desafio
Por mais estranho que pareça, este foi o problema mais difícil de todos na minha opinião. Diferente dos outros, não consegui entender a lógica de primeira, nem de segunda, nem de terceira. Precisei de um tempo muito maior para processar as fórmulas.

**A Lógica:** O desafio era encontrar um número em uma posição 'K' sem criar uma lista real (que travaria o comútador por excesso de memória). Tive que entender que:
- Se for **ímpar**, a fórmula é '2 * K - 1'.
- Se for **par**, precisamos calcular a quantidade de ímpares '(n + 1) // 2' e subtrair para achar a posição na sequência dos pares, multiplicando por 2.

Escrever isso em Python foi muito dificultoso. Usei o 'map' (que funciona como um **encaminhador**), o 'input().split()' para receber os textos e o 'int' para transformar esses números inteiros de verdade para o programa processar.

### Problema 1: Watermelon (4A)
No começo, eu estava com a mente fechada para a lógica desse problema. Eu pensava: *''Que problema de doido, o povo cria problema onde não tem para tentar resolver''*. Esse bloqueio me atrapalhou, mas depois entendi que é matemática (verificar se o peso é par e maior que 2) era a chave.

### Problema 4: Taxi (158B)
Este foi primordial para fixar a linguagem! Ele me ajudou a relembrar e aprender comandos como 'list()', 'map()', 'int()', input()' e 'split()'. O uso do 'max(0, ...)' para evitar restos negativos foi uma das lógicas mais interessantes que aprendi aqui.

### Problema 3: Way Too Long words (71A)
Neste eu entendi a lógica logo de cara. O desafio foi aprender a escrever as linhas de código corretamenete, já que é a minha primeira vez.Ele reforçou o uso do 'input()' e do 'plit()' que agora já estão fixos ba minha memória.

---

## Uso da Inteligência Artificial (Gemini)

Neste desafio, usei o Gemini como um mentor técnico. A IA me ajudou em:
1. **Interpretação:** Me explicando como visualizar o problema sem precisar criar uma lista real no computador, economizando processamento e memória.
2. **Identificação de Fórmulas:** Me ajudando a chegar na conta certa para os números ímpares no 'Even Odds'.
3. **Depuração (debug):** Analizamos juntos meus erros de digitação e garantimos que as converções de tipos (textos para números) estivessem corretas.

---

##Reflexão final

**Dificuldades:** Minha maior dificuldade foi o raciocínio lógico em fórmulas matemáticas e compreender as nuances da tradução automática de termos técnicos. Isso gerou muita confusão na hora de passar o pensamento para a ''gramática'' (sintaxe) do Python.

**O que aprendi:** Aprendi que nem sempre a solução mais óbia (como criar um lista do zero) é a melhor. É possivel usar a lógica matemática para ''pular direto para a resposta'', economizando tempo e esforço do computador.

**Experiência Geral:**
Saí do ''zero'' no GitHub, no Python, no codeforces e no VS Code (onde digitei as sintaxes de python) para um repositório organizado. Ver o ''verdinho'' das contribuições no perfil e ver o código funcionando depois de tantas tentativas foi a melhor parte. Sinto que hoje estendo o ''porquê'' de cada comando, e não apenas copio o que vejo.
