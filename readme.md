Solicitar ao usuário que selecione um diretório.

Quando se desenvolve um sisteminha para automação nem sempre o diretório do cliente é o mesmo caminho que está na sua máquina, ao invés de deixar o caminho fixo, podemos deixar o caminho sendo uma variável para o cliente escolher.

isso ajuda em ambiente corporativo, pois cada funcionário organiza suas pastas e nomes da forma que melhor lhe agrada.

Usei a biblioteca tkinter para GUI e o módulo (tkinter.simpledialog) para capturar os caminhos. 

função askdirectory() Abre diretorio e captura pastas
função askopenfilename() Abre diretorio e captura arquivos

Com isso, é só mandar abrir o diretório ou arquivo e deixar o script terminar de rodar.


