## PC - Por favor, me aprova Marlos, eu tô desesperado kkkkkkkk

Nesse arquivo, as palavras trabalho e projeto serão intercaladas e tendo o mesmo significado

### Como gerar código para distribuição e testes

Execute o arquivo ```bundle.py```, ele irá gerar o código de distribuição numa pasta ```dist```, o que também é necessário
para testar o código, uma vez que ele se copia para pasta do trabalho recém-criado e é necessário que seja o código todo.

Caso ocorra um erro neste processo, crie uma pasta "dist" antes.

### Como usar?

| ATENÇÃO: Para utilizar o projeto, baixe as releases que estão disponíveis (sempre a mais atual), nunca utilize o código fonte aqui disponibilizado. |
| --- |

Antes de tudo, é necessário adicionar suas informações no ```config.json```, adicionando as informações necessárias como nome, numero de matricula,
email institucional para login, senha do seu email e email para quem enviar (se for marlos já tem lá específico qual email), seguindo modelo a seguir:

```json
{
    "enrollment": "<matricula>",
    "to": "<recipient, email de marlos=marlos.uesb@gmail.com",
    "author": "<breno>",
    "email": "<seu_email_academico>",
    "password": "<senha do email academico>"
}
```

Obviamente sem os sinais de menor e maior que (```<``` e ```>```), existem os seguintes comandos:

Os seguintes argumentos SÓ podem ser usados no processo de criação de projetos, ou seja, onde ficam todos os trabalhos de programação concorrente:

* **-create**: Esse é utilizado para criar um projeto, ele só cria um arquivo Principal.java dentro da pasta do projeto.
* **-jfx** ou **--use-javafx**: Ordena que o projeto seja do JavaFX. Se o projeto for do JavaFX, ele cria todos os arquivos
necessários apresentando uma sugestão de estrutura para seu projeto, com imagem, css, fxml e controlador.
* **-pn** ou **--project-name**: Quando criar um novo trabalho, já cria com o nome especificado nesse argumento (Para o cabeçalho dos arquivos java).
* **-desc** ou **--project-description**: Ao criar um novo trabalho, especifica no cabeçalho da classe Principal.java a "função" do trabalho, o que ele faz.

Os comandos abaixo SÓ funcionam dentro da pasta de cada trabalho, nunca fora dela.

* **-compile**: Usado para compilar o projeto (O que na verdade faz é só executar ```javac Principal.java```)
* **-ex** ou **-execute**: Usado para executar o projeto (O que na verdade faz é só executar ```java Principal```)
* **-clean**: Apaga todos os .class dentro da pasta do trabalho (não é necessário fazer antes de comprimir ou zipar)
* **-zip**: Zipa o projeto, sem adicionar os arquivos ```.class```, ```config.json``` e ```pc.py```. E salva o arquivo na pasta pai
onde fica o arquivo Principal.java. Lembrando que ele não inclui também pastas vazias.
* **-send** ou **-submit**: Envia o projeto para o email especificado no ```config.json```, usando as credenciais email
e password para login (lembre-se de permitir o login de apps menos seguros nas configurações da Google, se não se lembrar o script te lembra)
* **-p** ou **--prettify**: Reservado para uso posterior, ainda nao se aplica. Mas pretende-se adicionar a função de corrigir erros de indentação,
codificação, quebra de linhas e os cabeçalhos dos arquivos .java. Ele irá pedir sua confirmação antes de enviar o email. Responda com "s" para enviar.

Vale lembrar que é possível usar todos esses comandos simultamente, basta executar:

```powershell
python pc.py -compile -execute -clean -zip -send [--prettify]
```
