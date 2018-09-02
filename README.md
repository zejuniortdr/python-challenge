# Proposta de solução de José Luis da Cruz Junior

## Instalação / Setup:
Após baixarem os arquivos, é necessário conceder permissão de execução ao arquivo **setup.sh** e para o **run.sh**:
```bash
chmod +x setup.sh run.sh
```

### Execute o **setup.py**
```bash
./setup.sh
```

### Para execução via terminal
Após rodar o **setup.py**,  digite no terminal:
```bash
python tree.py
```

## Para API Rest:
Basta rodar o arquivo **run.sh** no terminal:
```bash
./run.sh
```
A API Rest estará disponível em http://localhost:8000/autocomplete/.

### Parâmetros
- **q**: Carateres iniciais do nome do paciente, conforme valores possíveis abaixo:
    - **<str>**: Ex:  http://localhost:8000/autocomplete/?q=Mar.
    - **Omitido (None)**: Em caso de omissão, nenhum filtro por nome será feito e a lista completa será exibida conforme quantidade definida no parâmetro **limit**. Ex:  http://localhost:8000/autocomplete/.
- **limit**: Define a quantidade de registros exibidas na busca, conforme valores possíveis abaixo:
    - **0 (zero)**: Serão exibidos todos os registros que satisfizerem a busca. Ex: http://localhost:8000/autocomplete/?q=Mar&limit=0 ;
    - **X (int)**: Serão exibidos os **X** primeiros registros que satisfizerem a busca. Ex: http://localhost:8000/autocomplete/?q=Mar&limit=10 ;
    - **Omitido (None)**: Em caso de omissão, por padrão serão  exibidos apenas os **5 primeiros** registros que satisfizerem a busca. Ex:  http://localhost:8000/autocomplete/?q=Mar

### Exemplos para consumir API via terminal:
```bash
curl -X GET -H "Content-Type: application/json" http://localhost:8000/autocomplete/
curl -X GET -H "Content-Type: application/json" http://localhost:8000/autocomplete/?limit=10
curl -X GET -H "Content-Type: application/json" http://localhost:8000/autocomplete/?q=Mar
curl -X GET -H "Content-Type: application/json" http://localhost:8000/autocomplete/?q=Mar\&limit=0
curl -X GET -H "Content-Type: application/json" http://localhost:8000/autocomplete/?q=Mar\&limit=3
```
