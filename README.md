## CaesarCipher

<h3>Caesar Cipher in Cryptography</h3>
<img src="https://play-lh.googleusercontent.com/4HWP0WU1N91Uav9dB-iljHvuEu2FHUA6uWRCm6T2fh7peSEiWONlwEHL9YlET3nfxYDP" alt="cipher">

<p>
Esta cifra foi (provavelmente) inventada e usada por Caio Júlio César e suas tropas durante as Guerras da Gália. A ideia é bastante simples – cada letra da mensagem é substituída por seu consequente mais próximo ( A torna-se B , B torna-se C e assim por diante). A única exceção é Z , que se torna A .
</p>
<h4>
Nós o escrevemos usando as seguintes suposições:
</h4>

**1-** Aceita apenas letras latinas (nota: os romanos não usavam espaços em branco ou dígitos).<br>
**2-** Todas as letras da mensagem são maiúsculas (nota: os romanos conheciam apenas maiúsculas).<br>
<h4>Vamos rastrear o código:</h4>

**linha 02:** solicita ao usuário que digite a mensagem aberta (não criptografada) de uma linha;<br>
**linha 03:** prepare uma string para uma mensagem criptografada (vazia por enquanto).<br>
**linha 04:** inicia a iteração através da mensagem;<br>
**linha 05:** se o caractere atual não for alfabético...<br>
**linha 06:** ...ignore;<br>
**linha 07:** converter a letra para maiúscula (é preferível fazer às cegas, ao invés de verificar se é necessário ou não).<br>
**linha 08:** pega o código da letra e incrementa em um;<br>
**linha 09:** se o código resultante tiver "saído" do alfabeto latino (se for maior que o código Z )...<br>
**linha 10:** ...mude para o código A ;<br>
**linha 11:** anexa o caractere recebido ao final da mensagem criptografada;<br>
**linha 13:** imprima a cifra.<br>