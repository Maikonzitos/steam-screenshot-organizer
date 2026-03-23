**Steam-Screenshot-Organizer**

Este script automatiza a organização das capturas de tela da Steam, que normalmente ficam escondidas em diversas subpastas dentro do diretório de instalação. Fiz esse script com a finalidade de facilitar o encontro de todas as minhas capturas e tambem a importação para o Google Drive, pois a minha pasta de destino é sincronizada com o meu Google Fotos e assim que as imagens são copiadas, já é feito a sincronização, facilitando assim a minha visualização pelo celular.


**O que ele faz:**
- Varre as pastas de IDs de jogos da Steam.
- Localiza imagens nos formatos `.png`, `.jpg`, `.jpeg` e `.bmp`.
- Ignor a pasta "thumbnails".
- Copia as imagens para uma pasta centralizada de sua escolha.
- **Evita duplicatas:** Se a imagem já existir no destino, o script pula para a próxima (evite mudar o nome da imagem).
- **Preserva metadados:** Mantém a data original da captura.

**Tecnologias:**
- **Python 3**
- Bibliotecas nativas: `os` e `shutil`.

**Como usar:**
1. Altere as variáveis `origem` e `destino` no arquivo `screenshot-import.py` para os seus caminhos locais.
2. Execute o script: `python screenshot-import.py`.

**O que eu recomendo:**
Para que você não precise rodar o script manualmente toda vez, recomendo configurar o **Agendador de Tarefas do Windows** para executar o script automaticamente.

**Passo a passo para configurar:**
1. Abra o **Agendador de Tarefas do Windows**.
2. Clique em **Criar Tarefa Básica...** no painel direito.
3. Dê um nome (ex: `Screenshots_Sync`) e escolha o disparador: **Ao fazer logon** ou **Ao iniciar o computador**.
4. Em "Ação", escolha **Iniciar um programa**.
5. No campo **Programa/script**, digite `pythonw.exe` (o `pythonw` evita que uma janela preta do console pisque).
6. No campo **Adicionar argumentos**, coloque o caminho completo do seu script, por exemplo: `C:\Scripts\screenshot-import.py`.
7. No campo **Iniciar em**, coloque o caminho da pasta onde o script está salvo.
