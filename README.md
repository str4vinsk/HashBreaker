# HashBreaker
Linux password hashes breaker, used for linux post hacking process.

## 💾 Installing

Você pode rodar o programa mesmo sem instalar, basta usar o script normalmente dentro da pasta que contém os arquivos necessários.

Torne o script executável
```
chmod +x INSTALL.sh
```
exeute o arquivo como root para iniciar a instalação
```
sudo ./INSTALL.sh
```
---

## 🔨 Usage

<b>Modos</b>

Você pode usar o script em dois modos diferentes, o raw ou o shadow.
O modo <code>raw</code> é usado quando você quer quebrar hashes comuns, como a seguinte

    ec0e2603172c73a8b644bb9456c1ff6e

Para a utilização desse modo é necessário que você especifique o tipo de hash a ser testada usando a opção <code>--type</code>,
se a hash contém um salt especifique o salt usando a opção <code>--salt</code>

<code>python hashbreaker.py wordlist hashlist raw --type 2 --salt Gh5e77H</code>

---

O modo <code>shadow</code> como o próprio nome diz é usado para quebrar hashes armazenadas no arquivo shadow das distribuições unix. Ou qualquer outra 
hash que siga esse padrão:

    $1$5RPVAd$vgsoSANybLDepv2ETcUH7.

Neste modo não é preciso especificar o tipo de hash, o script irá detectar o tipo a partir do número
entre os primeiros cifrões da hash. <b>ESTE MODO É USADO ESPECIFICAMENTE PARA O PROPÓSITO DE QUEBRAR SENHAS LINUX</b>

Exemplo de uso:
<code>python hashbreaker.py wordlist hashlist shadow</code>


Por favor use o comando <code>--help</code> para ver o funcionamento do programa, se tiver qualquer pergunta ou sugestão entre em contato comigo

---

## Hash Table

Use a seguinte tabela para descobrir o número correspondente a determinada hash, utilize esse número como valor do argumento <code>--type</code>

| Tipo de Hash  | Valor Númerico |
| ------------- | -------------  |
  MD5           |          1     
  MD5(salt + pass) |       2
  MD5(pass + salt)|        3
  SHA256       |           4
  SHA256(salt + pass) |    5
  SHA256(pass + salt) |    6
  SHA512       |           7
  SHA512(salt + pass) |    8
  SHA512(pass + salt)|     9


---
 
## 📖 Author
<table>
  <tr>
    <td  align=center>
        <img src="https://avatars0.githubusercontent.com/u/64869691?s=460&u=55a251a576b8f0a784a65c555a6da34eefeb9f1a&v=4" width="100px" alt="Vitor Conroy">
        <a href="https://github.com/str4vinsk">
          <br>
            Vitor Conroy
          </br>
        </a>
        <sub>
          <a href="https://www.instagram.com/vitorconroy/" alt="instagram">
            ☕️ @vitorconroy
          </a>
        </sub>
    </td>
  </tr>
</table>


#Good Hacking!!
