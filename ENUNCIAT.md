# Activitat 4: Models LLM locals, temperatura i paràmetres amb Ollama

## Introducció

Amb Ollama podeu executar models LLM en local i veure, en pocs minuts, com canvia la resposta del model quan en modifiqueu els paràmetres. Un LLM genera el text **token a token**: a cada pas calcula una probabilitat per a cada possible token següent i en tria un. Els paràmetres que treballarem controlen aquesta tria.

| Paràmetre | Què controla | Valor per defecte (orientatiu) |
| :- | :- | :- |
| `temperature` | Com d'arriscada és la tria: 0 és sempre la més probable; valors alts donen més varietat. | 1 |
| `seed` | Llavor de l'aleatorietat; la mateixa llavor repeteix la mateixa resposta. | -1 (aleatòria) |
| `top_k` | Nombre màxim de candidats que es consideren a cada pas. | 64 |
| `top_p` | Només es consideren els candidats que sumen aquesta probabilitat. | 0.95 |
| `num_predict` | Nombre màxim de tokens de la resposta (-1 és sense límit). | -1 |
| `num_ctx` | Mida del context: quants tokens «recorda» el model. | 4096 |

### Com cal treballar

Cada prova és un petit experiment. Perquè els resultats us serveixin, seguiu aquestes regles:

1. **Canvieu una sola cosa cada vegada.** Si canvieu dos paràmetres alhora, no sabreu quin dels dos ha provocat la diferència.
2. **Repetiu cada prova 3 vegades com a mínim.** El model no sempre respon igual, i amb una sola resposta no podeu veure cap patró.
3. **Escriviu `/clear` entre repeticions.** El model recorda la conversa i, si no l'esborreu, la prova queda alterada (ho comprovareu a la prova de memòria). 
4. **Comenceu cada exercici amb una sessió nova del model.** Escriviu `/bye` i torneu a executar `ollama run gemma3:4b`. `/clear` esborra la conversa, però **no** torna els paràmetres als valors per defecte; sortir i tornar a entrar, sí.

Per veure els paràmetres que té el model en aquest moment, escriviu `/show parameters`. Els valors per defecte poden ser diferents segons el model i la versió d'Ollama.

## Preparació

Per a totes les pràctiques farem servir el model **gemma3** (4B paràmetres, uns 3,3 GB) de Google. És un model multilingüe que entén bé el català i no té mode de raonament (*thinking*), així que la sortida que veieu depèn directament dels paràmetres.

### Instal·lació d'Ollama a Windows

Obriu **PowerShell** (cerqueu «PowerShell» al menú d'inici) i instal·leu Ollama amb una d'aquestes dues opcions:

- Amb `winget` (opció recomanada):

  ```powershell
  winget install Ollama.Ollama
  ```

- Amb l'script oficial d'Ollama:

  ```powershell
  irm https://ollama.com/install.ps1 | iex
  ```

En acabar, **tanqueu i torneu a obrir PowerShell** perquè reconegui l'ordre `ollama`. Ollama s'executa en segon pla (hi ha la icona de la llama a la safata del sistema). Si no s'hi està executant, inicieu-lo des del menú d'inici o amb `ollama serve`.

### Descàrrega i primers passos

1. Comproveu que Ollama està instal·lat:

   ```powershell
   ollama --version
   ```

2. Descarregueu el model:

   ```
   ollama pull gemma3:4b
   ```

3. Comproveu que apareix a la llista de models locals:

   ```
   ollama list
   ```

4. Executeu el model en mode interactiu. L'opció `--verbose` mostra estadístiques (tokens per segon, durada) en acabar cada resposta:

   ```
   ollama run gemma3:4b --verbose
   ```

5. Dins la sessió interactiva (el símbol `>>>`) teniu aquestes ordres. Practiqueu-les abans de continuar:

   ```
   /?                                  mostra l'ajuda
   /show parameters                    mostra els paràmetres actuals
   /set parameter temperature 0.8      canvia un paràmetre
   /clear                              esborra el context de la conversa
   /bye                                surt de la sessió
   ```

**Prova de memòria:** dins la sessió, escriviu aquestes quatre línies una darrere l'altra, esperant la resposta abans de passar a la següent:

```
Recorda aquest número: 4721.
Quin número t'he dit?
/clear
Quin número t'he dit?
```

La primera vegada el model respon `4721`; després de `/clear`, ja no ho sap. Per això cal fer `/clear` entre proves: sense ell, el model veu les respostes anteriors i la prova no és neta.

## Exercici 1: la temperatura

**Objectiu:** veure que amb temperatura 0 el model és previsible (però no per això encerta), que a mesura que puja les respostes es fan més variades i que la temperatura no canvia res quan la pregunta només té una resposta correcta.

**Predicció (abans de començar):** què creieu que passarà amb les respostes quan pugeu la temperatura?

### Primera prova: una paraula

1. Inicieu el model i fixeu la temperatura a 0:

   ```
   ollama run gemma3:4b
   >>> /set parameter temperature 0
   ```

2. Escriviu aquest prompt, llegiu la resposta, anoteu-la a la **taula 1** i feu `/clear`. Repetiu-ho fins a tenir **3 respostes** (una a cada columna):

   ```
   Digues una paraula en català de més de 10 lletres. Respon només amb la paraula.
   ```

3. Repetiu el pas 2 amb `/set parameter temperature 0.8` i, després, amb `/set parameter temperature 1.5`. Cada temperatura és una fila de la taula.

**Taula 1: la paraula**

| Temperatura | Resposta 1 | Resposta 2 | Resposta 3 |
| :- | :- | :- | :- |
| 0 | | | |
| 0.8 | | | |
| 1.5 | | | |

### Segona prova: una pregunta amb una sola resposta

4. Feu el mateix que a la primera prova (3 respostes per temperatura, amb `/clear` entre cadascuna), però només amb les temperatures 0 i 1.5 i amb aquest altre prompt. Comenceu per la temperatura 0: torneu-la a fixar amb `/set parameter temperature 0`, perquè ara la teniu a 1.5. Anoteu les respostes a la **taula 2**, encara que sembli que sempre sortirà el mateix: és justament el que voleu comprovar:

   ```
   Quina és la capital de França? Respon només amb el nom.
   ```

**Taula 2: la capital de França**

| Temperatura | Resposta 1 | Resposta 2 | Resposta 3 |
| :- | :- | :- | :- |
| 0 | | | |
| 1.5 | | | |

### Preguntes

1. Mireu la taula 1. Les tres respostes amb temperatura 0 són iguals? Per què? Compteu les lletres de la paraula: en té més de 10? Que sempre surti la mateixa paraula vol dir que sigui correcta?
2. Què passa quan pugeu la temperatura? Surten paraules diferents? N'hi ha alguna que no tingui més de 10 lletres o que no sembli una paraula real?
3. Mireu la taula 2. Les respostes sobre la capital canvien tant com les de la paraula quan puja la temperatura? Per què creieu que la temperatura hi té tan poc efecte? (Pista: quantes respostes correctes té cada pregunta? La temperatura només dona varietat quan el model dubta entre diverses opcions.)
4. Amb les vostres paraules: què fa el paràmetre `temperature`?

## Exercici 2: automatitzar les proves generant un script amb el model

**Objectiu:** crear un script que automatitzi les proves de l'exercici 1: repeteix un prompt les vegades que vulgueu, amb la temperatura que li indiqueu, sense haver d'escriure `/clear`. L'script **no l'heu d'escriure vosaltres**: us el generarà el model `gemma3:4b`. Així veureu fins on arriba un model petit escrivint codi i per què cal llegir-lo i provar-lo abans de fiar-se'n. Aquest script serà el vostre laboratori: als exercicis següents l'ampliareu amb nous paràmetres a mesura que els necessiteu.

**Predicció (abans de començar):** el primer codi que us doni el model funcionarà? Quants intents us caldran?

1. **Configureu l'entorn de Python.** Aquest exercici i els següents fan servir Python. No cal crear cap carpeta nova: feu-ho dins del mateix repositori. Només cal fer-ho un cop, amb Visual Studio Code:

   1. Obriu el repositori a VS Code (*File > Open Folder*). Cal tenir instal·lada l'extensió *Python* de Microsoft.
   2. Premeu `Ctrl+Shift+P`, escriviu `Python: Create Environment` i trieu-lo.
   3. Seleccioneu **Venv** i, després, l'intèrpret de Python que voleu fer servir. VS Code crea la carpeta `.venv`.
   4. Obriu un terminal nou (*Terminal > New Terminal*): l'entorn s'activa sol i veureu `(.venv)` al principi de la línia. Instal·leu la llibreria:

      ```powershell
      pip install ollama
      ```

2. Obriu un segon terminal a VS Code i inicieu el model (el mateix `gemma3:4b` de la Preparació, que també sap escriure codi):

   ```
   ollama run gemma3:4b
   ```

3. Demaneu-li l'script. No li doneu codi: expliqueu-li què ha de fer.

   **Què ha de fer l'script:**

   - El fitxer es diu `lab.py` i es crida així:

     ```powershell
     python lab.py "prompt" --vegades 5 --temperature 0.8
     ```

   - El prompt és obligatori (text). Si no s'indiquen, `--vegades` (enter) val 5 i `--temperature` (decimal) val 1.
   - Les opcions s'escriuen amb nom (`--vegades`, `--temperature`) i en qualsevol ordre. Així, més endavant, hi podrem afegir més opcions sense trencar res.
   - Si s'executa sense cap argument, no ha de fallar amb un error: ha de mostrar l'ajuda (l'ús i les opcions) i sortir.
   - Fa servir el model `gemma3:4b`.
   - Repeteix el prompt les vegades indicades amb crides independents (sense historial, així no cal `/clear`).
   - Primer imprimeix les opcions que fa servir i, després, cada resposta numerada.

   **Com demanar-ho al model:**

   - Digueu-li que faci servir `argparse`.
   - Doneu-li un exemple de sortida, perquè així el format surt igual cada cop:

     ```
     Prompt: Digues una paraula
     vegades: 3
     temperature: 0.8

     1. Algorisme
     2. Microprocessador
     3. Recursivitat
     ```

   - Demaneu-li que respongui **només amb el codi complet, en un sol bloc i sense explicacions**, perquè sigui fàcil de copiar.

   *Pista:* el model no coneix bé la llibreria d'Ollama. Digueu-li que ha de fer servir `ollama.generate(model=..., prompt=..., options={...})`, que **tots els paràmetres del model** (ara `temperature`; més endavant `seed`, `top_k`, `top_p`, `num_predict`...) han d'anar dins del diccionari `options` i no com a arguments directes de `generate`, i que el text de la resposta és a `r["response"]`. Remarqueu-li que `generate` **no retorna el text directament**, sinó un objecte amb diversos camps, i que cal agafar-ne només el camp `response` abans de netejar-lo i imprimir-lo.

4. Creeu el fitxer `lab.py` a VS Code, copieu-hi el codi que us doni el model i **llegiu-lo** abans d'executar-lo. No el corregiu a mà: si falla, copieu l'error al model i demaneu-li que el solucioni. Apunteu els intents i els errors (els necessitareu per a la pregunta 1) i enganxeu el prompt final a l'apartat «El vostre prompt final» del `README.md` de l'exercici.
5. Proveu-lo amb els prompts de l'exercici 1. Aquests exemples són per a PowerShell:

   ```powershell
   $promptParaula = "Digues una paraula en català de més de 10 lletres. Respon només amb la paraula."
   $promptCapital = "Quina és la capital de França? Respon només amb el nom."

   # Primera prova de l'exercici 1: 3 repeticions amb temperatura 0
   python lab.py $promptParaula --vegades 3 --temperature 0
   # El mateix amb temperatura 0.8
   python lab.py $promptParaula --vegades 3 --temperature 0.8
   # Segona prova de l'exercici 1: 3 repeticions amb temperatura 1.5
   python lab.py $promptCapital --vegades 3 --temperature 1.5
   ```

6. Compareu els resultats amb les taules de l'exercici 1. Amb temperatura 0, les repeticions haurien de donar la mateixa resposta. Atenció: la **primera** resposta pot ser diferent de les altres, perquè Ollama processa el prompt de manera lleugerament diferent la primera vegada. No és un error vostre: repetiu la sèrie i compareu les respostes següents.

### Preguntes

1. Quants intents us han calgut? Quins errors ha comès el model (nom del model, paràmetres, lectura dels arguments...) i com els heu resolt?
2. Heu llegit el codi abans d'executar-lo? Per què és important entendre el que s'executa a l'ordinador, encara que l'hagi escrit un model?

## Exercici 3: la temperatura depèn de la tasca

**Objectiu:** comprovar que no hi ha una temperatura «millor»: una tasca de precisió i una de creativitat necessiten valors diferents. També veureu que una temperatura baixa fa el model més consistent, però no el fa encertar més: si no sap fer una tasca, s'equivoca igualment.

**Predicció (abans de començar):** amb quina temperatura creieu que el model encertarà més una multiplicació? I amb quina proposarà noms més variats?

**Script:** aquest exercici no necessita cap paràmetre nou: feu servir `lab.py` tal com el teniu.

1. Deseu els dos prompts en variables de PowerShell. El prompt A mesura la precisió (la resposta correcta és 337491) i el B, la creativitat:

   ```powershell
   $promptA = "Quant fa 487 × 693? Respon només amb el número."
   $promptB = "Dona'm 5 noms originals per a una cafeteria d'informàtics. Respon només amb els noms."
   ```

2. Executeu cada prompt **3 vegades** amb temperatura 0 i **3 vegades** amb temperatura 1.5, i completeu la taula:

   ```powershell
   python lab.py $promptA --vegades 3 --temperature 0
   python lab.py $promptA --vegades 3 --temperature 1.5
   python lab.py $promptB --vegades 3 --temperature 0
   python lab.py $promptB --vegades 3 --temperature 1.5
   ```

| Prompt | Temperatura 0 | Temperatura 1.5 |
| :- | :- | :- |
| A: 487 × 693 (quantes vegades ha encertat?) | | |
| B: noms de cafeteria (hi ha varietat? són repetits?) | | |

### Preguntes

1. Amb quina temperatura funciona millor cada tasca? Per què?
2. Quina temperatura triaríeu per a un assistent de codi? I per un generador de noms de projectes o de startups tecnològiques?
per a un generador d'idees per a un eslògan?
3. Amb temperatura 0, el model ha donat sempre la mateixa resposta al prompt A? Era correcta? Que una resposta sigui consistent vol dir que sigui correcta? Com resoldríeu aquest problema en una aplicació real?

## Exercici 4: seed, repetir l'aleatorietat

**Objectiu:** descobrir que l'«aleatorietat» del model es pot controlar i reproduir.

**Predicció (abans de començar):** si repetiu el mateix prompt amb la mateixa llavor, creieu que sortirà exactament la mateixa resposta?

1. **Actualitzeu `lab.py`:** afegiu l'opció `--seed` (per exemple, `--seed 42`), que va dins d'`options` i només s'ha d'enviar si s'indica.
   - Per demanar-ho al model, feu `/bye`, torneu a executar `ollama run gemma3:4b` i enganxeu-hi el vostre `lab.py` escrivint abans «Tinc aquest script de Python, `lab.py`:». Demaneu-li només el canvi nou i que us torni el codi complet. Feu el mateix als exercicis següents.
   - **Comproveu** que l'script imprimeix la llavor entre les opcions i que tot el que ja funcionava continua funcionant: el model pot esborrar codi anterior.
2. Deseu aquest prompt en una variable de PowerShell i executeu-lo **3 vegades** amb temperatura alta i **sense** llavor (aleatòria). Anoteu els noms a la taula:

   ```powershell
   $prompt = "Inventa el nom d'un mòdul optatiu absurd d'un cicle formatiu de grau superior d'informàtica. Respon només amb el nom."
   python lab.py $prompt --vegades 3 --temperature 1.5
   ```

3. Repetiu-ho **amb** la llavor 42 i anoteu els noms a la taula. El número concret de la llavor no importa; el que compta és que sigui el mateix per repetir la resposta i diferent per canviar-la.

   ```powershell
   python lab.py $prompt --vegades 3 --temperature 1.5 --seed 42
   ```

   Si la primera resposta és diferent de les altres dues, repetiu la prova: a vegades la primera resposta d'una sèrie varia lleugerament (és un efecte numèric normal).

| Llavor (seed) | Nom 1 | Nom 2 | Nom 3 | Són iguals? |
| :- | :- | :- | :- | :- |
| Cap (aleatòria) | | | | |
| 42 | | | | |

### Preguntes

1. Quan la llavor és la mateixa, els tres noms són iguals o diferents? Proveu ara una altra llavor (per exemple, `--seed 43`): surt el mateix nom?
2. Penseu en una situació en què voldríeu obtenir exactament la mateixa resposta dues vegades (per exemple, per trobar un error en un programa). Quina?
3. Compareu els vostres noms amb els d'una altra persona de la classe que hagi fet servir la mateixa llavor. Són iguals? Per què creieu que pot passar?

## Exercici 5: top_k i top_p

**Objectiu:** veure com limitem els candidats entre els quals el model tria el token següent.

**Predicció (abans de començar):** què creieu que passarà si el model només pot triar entre 2 candidats? I si pot triar entre tots?

- `top_k`: només es consideren els *k* tokens més probables (`top_k` 0 desactiva aquest límit).
- `top_p`: només es consideren els tokens més probables fins a sumar aquesta probabilitat (`top_p` 1 vol dir tots).

1. **Actualitzeu `lab.py`:** afegiu les opcions `--top_k` i `--top_p`. Van dins d'`options` i només s'han d'enviar si s'indiquen. **Comproveu** que l'script imprimeix les opcions que li passeu: `python lab.py "Hola" --vegades 1 --temperature 0 --seed 1 --top_k 5 --top_p 0.9` ha de mostrar entre les opcions `seed`, `top_k` i `top_p`.
2. Deseu aquest prompt en una variable de PowerShell:

   ```powershell
   $prompt = "Digues un emoji. Respon només amb l'emoji."
   ```

3. Executeu cada configuració (15 repeticions i sense llavor, així cada repetició pot donar un resultat diferent). Fixeu-vos que cada configuració canvia **una sola cosa** respecte de la referència (A), tret de D i E, que comparteixen la temperatura alta:

   ```powershell
   # Configuració A (referència: sense filtres)
   python lab.py $prompt --vegades 15 --temperature 1 --top_k 0 --top_p 1
   # Configuració B (només top_k)
   python lab.py $prompt --vegades 15 --temperature 1 --top_k 2 --top_p 1
   # Configuració C (només top_p)
   python lab.py $prompt --vegades 15 --temperature 1 --top_k 0 --top_p 0.3
   # Configuració D (temperatura 2.5 sense filtres)
   python lab.py $prompt --vegades 15 --temperature 2.5 --top_k 0 --top_p 1
   # Configuració E (temperatura 2.5 amb els filtres per defecte)
   python lab.py $prompt --vegades 15 --temperature 2.5 --top_k 64 --top_p 0.95
   ```

4. A cada fila de la taula, compteu **quants emojis diferents** han sortit de les 15 respostes.

| Configuració | temperature | top_k | top_p | Emojis diferents (de 15) |
| :- | :- | :- | :- | :- |
| A (referència) | 1 | 0 | 1 | |
| B | 1 | 2 | 1 | |
| C | 1 | 0 | 0.3 | |
| D | 2.5 | 0 | 1 | |
| E | 2.5 | 64 | 0.95 | |

### Preguntes

1. Ordeneu A, B i C de més a menys varietat. Per què `top_k` 2 i `top_p` 0.3 redueixen el nombre d'emojis diferents?
2. Quin valor de `top_k` hauria de tenir la configuració B perquè el model es comportés com si la temperatura fos 0? Per què?
3. Compareu les configuracions D i E. Quants emojis diferents surten a cada una? Quin és l'emoji més inesperat o amb menys sentit com a resposta, i a quina configuració ha aparegut? Per què `top_k` i `top_p` ajuden a evitar respostes sense sentit quan la temperatura és alta?

## Exercici 6: num_predict i tokens

**Objectiu:** entendre que el model compta en **tokens**, no en paraules, i que podem limitar la longitud de la resposta.

**Predicció (abans de començar):** si limiteu la resposta a 20 tokens, el model farà una resposta més curta o quedarà tallada?

1. **Actualitzeu `lab.py`:** afegiu l'opció `--num_predict` (va dins d'`options` i només s'ha d'enviar si s'indica) i feu que, després de cada resposta, l'script imprimeixi el nombre de tokens generats (el camp `eval_count` de la resposta d'Ollama). **Comproveu** que el valor surt després de cada resposta: `python lab.py "Hola" --vegades 1 --temperature 0 --seed 1 --num_predict 10` ha de mostrar `seed` i `num_predict` entre les opcions i, després de la resposta, els tokens generats.
2. Feu aquest prompt amb temperatura 0 i tres límits de tokens diferents: 20, 200 i sense límit (`-1`):

   ```powershell
   $prompt = "Explica què és una xarxa neuronal."
   python lab.py $prompt --vegades 1 --temperature 0 --num_predict 20
   python lab.py $prompt --vegades 1 --temperature 0 --num_predict 200
   python lab.py $prompt --vegades 1 --temperature 0 --num_predict -1
   ```

3. A cada resposta, compareu el nombre de tokens generats (`eval_count`) amb el nombre de paraules de la resposta.

### Preguntes

1. Què passa amb la resposta quan `num_predict` és 20?
2. Compareu el començament de la resposta amb `num_predict` 200 i sense límit. El model «sap» que té un límit o simplement es talla? Com aconseguiríeu una resposta curta però completa?
3. El valor d'`eval_count` coincideix amb el nombre de paraules? Per què creieu que no?
4. En quin cas us interessaria limitar els tokens d'una resposta (cost, temps, interfície)?

## Exercici 7: num_ctx, la memòria del model

**Objectiu:** comprovar que el model només «recorda» el que cap dins la finestra de context.

El **context** (`num_ctx`) és la «memòria de treball» del model: el nombre màxim de tokens que pot tenir en compte alhora. Si el text és més llarg que el context, el model no el pot tenir tot a la vista.

**Predicció (abans de començar):** si el text és més llarg que el context, quina part creieu que oblidarà el model: el principi o el final?

### Preparar els textos

1. A la carpeta `exercici-07/` hi ha l'ajudant `genera_text.py`, que genera un text llarg de la mida (en tokens) que li demaneu: comença amb la frase de `--inici` (el secret), continua amb frases de farciment i acaba amb la de `--final` (la pregunta). Només fa servir Ollama per comptar tokens: **no li fa cap pregunta**. No cal que el llegiu a fons.
2. Genereu dos textos de mides diferents, des de l'arrel del repositori i amb l'entorn virtual activat. Es creen `text_1000.txt` i `text_6000.txt`, amb el secret al principi i la pregunta al final, i l'ajudant us diu quants tokens té exactament cadascun:

   ```powershell
   $inici = "El codi secret és PASSWORD-1234. Recorda'l."
   $final = "Pregunta: quin era el codi secret? Respon en una sola frase."
   python exercici-07/genera_text.py 1000 --inici $inici --final $final
   python exercici-07/genera_text.py 6000 --inici $inici --final $final
   ```

### Actualitzar l'script

3. **Actualitzeu `lab.py`:** demaneu al model aquests tres canvis (podeu fer-los d'un en un):
   - `--num_ctx`: la mida del context. Va dins d'`options`.
   - `--fitxer`: llegeix el prompt d'un fitxer de text. Si s'indica, el prompt de la línia d'ordres ja no és obligatori (*pista:* a `argparse` ha de ser un argument amb `nargs="?"`).
   - Després de cada resposta, imprimeix el valor `prompt_eval_count` de la resposta d'Ollama.

4. **Comproveu-ho** amb aquestes dues ordres (no cal que tingueu cap resposta correcta, només que surtin les dades):

   ```powershell
   # Ha de mostrar els tokens generats i prompt_eval_count
   python lab.py "Hola" --vegades 1 --temperature 0 --num_predict 10 --num_ctx 2048
   # Ha de mostrar un prompt_eval_count igual als tokens que us ha dit genera_text.py (1003)
   python lab.py --fitxer text_1000.txt --vegades 1 --temperature 0 --num_ctx 8192
   ```

   Si a la segona ordre el `prompt_eval_count` no és 1003 (per exemple, 1112), el fitxer es llegeix amb una codificació incorrecta. Digueu al model: «Obre el fitxer amb `encoding="utf-8"`».

### Fer les proves

5. Feu la pregunta al model amb cada text i cada context (una ordre per a cada casella de la taula):

   ```powershell
   # Text de 1000 tokens, context de 2048
   python lab.py --fitxer text_1000.txt --vegades 1 --temperature 0 --num_predict 40 --num_ctx 2048
   # Text de 1000 tokens, context de 8192
   python lab.py --fitxer text_1000.txt --vegades 1 --temperature 0 --num_predict 40 --num_ctx 8192
   # Text de 6000 tokens, context de 2048
   python lab.py --fitxer text_6000.txt --vegades 1 --temperature 0 --num_predict 40 --num_ctx 2048
   # Text de 6000 tokens, context de 8192
   python lab.py --fitxer text_6000.txt --vegades 1 --temperature 0 --num_predict 40 --num_ctx 8192
   ```

   A cada casella de la taula anoteu el valor de `prompt_eval_count` (els tokens del prompt que el model ha processat realment) i si el model recorda el codi (sí o no):

| Mida del text | `num_ctx` 2048 | `num_ctx` 8192 |
| :- | :- | :- |
| 1000 tokens | | |
| 6000 tokens | | |

Un context més gran gasta més memòria RAM. Si l'ordinador va just, genereu un text de 3000 tokens i proveu `num_ctx` 2048 i 4096 en lloc de 8192. Atenció: Ollama no accepta contextos inferiors a 2048 tokens (si demaneu 512, el puja a 2048). Podeu comprovar el context real amb `ollama ps` en un altre terminal (columna `CONTEXT`).

Fixeu-vos que amb `num_ctx` 2048 el `prompt_eval_count` del text de 6000 tokens no és 2048, sinó uns 1027: Ollama retalla el prompt a la meitat del context i **només en conserva el final**. Per això el model no recorda el codi del principi. Si ho voleu comprovar, busqueu l'avís `truncating input prompt` al registre del servidor (`%LOCALAPPDATA%\Ollama\server.log`).

### Preguntes

1. Mireu la taula. Amb quines combinacions de mida del text i `num_ctx` recorda el codi el model i amb quines no? Quina relació hi ha entre la mida del text i `num_ctx`?
2. Per què el model «omet» el principi del text quan aquest és més llarg que el context?
3. Quin problema pràctic us podeu trobar si feu servir un model local per resumir documents llargs?
4. Si amb 2048 el model ha respost una cosa inventada o ha negat que hi hagi cap codi: per què és perillós que ho digui amb seguretat, en lloc de dir que no ho sap?

## Exercici 8: missatge de sistema i Modelfile

**Objectiu:** canviar la «personalitat» i els paràmetres del model de manera permanent creant-ne una variant.

**Predicció (abans de començar):** el missatge de sistema canviarà només el to de la resposta o també el contingut?

1. Creeu un fitxer anomenat `Modelfile` (sense extensió; si feu servir el Bloc de notes, comproveu que no l'ha desat com a `Modelfile.txt`) amb aquest contingut:

   ```Dockerfile
   FROM gemma3:4b
   PARAMETER temperature 0.3
   SYSTEM """
   Ets una persona esgotada i sarcàstica que porta 20 anys fent guàrdies d'informàtica i apagant focs. Respons breument, amb ironia, però sempre dius la solució correcta.
   """
   ```

2. Creeu i executeu el model nou. Escolliu un nom amb unes inicials o un àlies, **mai el vostre nom real**, perquè el repositori no pot contenir dades personals (per exemple `apagafocs_xyz`):

   ```
   ollama create apagafocs_xyz -f Modelfile
   ollama run apagafocs_xyz
   ```

3. Feu-li aquesta pregunta i compareu la resposta amb la del model original `gemma3:4b`:

   ```
   Com es fa un bucle for en Python?
   ```

4. Inventeu un text de `SYSTEM` diferent i substituïu-lo al Modelfile. Podeu provar algun dels exemples clàssics (per exemple «Parles com el mestre Yoda: ordre de les paraules invertit. Ets un mestre de programació i respons breument.» o «Ets una persona revisora de codi molt exigent que sempre troba alguna cosa a criticar, però al final dones la solució correcta. Respons en menys de 80 paraules.») o inventar-ne un de propi. Torneu a executar `ollama create` amb el mateix nom i repetiu la pregunta.
5. Mostreu el missatge de sistema i els paràmetres del model creat i, quan acabeu, elimineu-lo:

   ```
   ollama show apagafocs_xyz --system
   ollama show apagafocs_xyz --parameters
   ollama rm apagafocs_xyz
   ```

### Preguntes

1. Quina diferència veieu entre `gemma3:4b` i la vostra variant amb el mateix prompt?
2. Dins la sessió del model nou, escriviu `/show parameters`: quina temperatura hi apareix? Quina relació té amb la línia `PARAMETER` del Modelfile?
3. Per què el missatge de sistema és tan important a l'hora de construir un assistent?
4. Amb la personalitat que heu donat al model al pas 4, la resposta continuava sent útil i correcta? Quin risc té donar massa «personalitat» a un assistent?

## Exercici 9: la mida del model

**Objectiu:** comparar un model petit i un de més gran amb els mateixos prompts i la mateixa configuració.

**Predicció (abans de començar):** en què creieu que es notarà més la diferència entre el model petit i el gran?

1. Descarregueu la versió d'1B paràmetres (la de 4B ja la teniu de la Preparació):

   ```
   ollama pull gemma3:1b
   ```

2. **Actualitzeu `lab.py`:** demaneu al model aquests dos canvis:
   - `--model`: el model que es fa servir (per defecte, `gemma3:4b`).
   - Després de cada resposta, imprimeix els **tokens per segon**: `eval_count / eval_duration * 1e9` (`eval_duration` és en nanosegons).

   *Pista:* després de cada resposta ha de sortir una línia nova amb els tokens per segon, calculada amb els camps `eval_count` i `eval_duration` de la resposta d'Ollama (que no mesuri el temps ell mateix).

3. **Comproveu-ho** amb aquesta ordre:

   ```powershell
   python lab.py "Hola" --vegades 1 --temperature 0 --num_predict 10 --model gemma3:1b
   ```

   Ha de mostrar els tokens generats, `prompt_eval_count` **i** els tokens per segon. Si en falta alguna cosa de les anteriors, demaneu-li al model que la recuperi.

4. Feu els quatre prompts a cada model, amb temperatura 0. Aquest bucle de PowerShell ho fa tot d'una vegada (8 execucions):

   ```powershell
   $prompts = @(
       "Quantes lletres «r» hi ha a la paraula «strawberry»?",
       "Quantes lletres «r» hi ha a la paraula «ferrocarril»?",
       "Escriu una frase en català sobre Barcelona.",
       "Quant fa 17 × 23? Explica-ho pas a pas."
   )
   foreach ($model in "gemma3:1b", "gemma3:4b") {
       foreach ($p in $prompts) {
           python lab.py $p --vegades 1 --temperature 0 --model $model
       }
   }
   ```

5. Anoteu a la taula la resposta i la velocitat (tokens per segon) de cada model. La velocitat depèn molt de l'ordinador: sense targeta gràfica serà bastant més baixa.

| Prompt | gemma3:1b | gemma3:4b |
| :- | :- | :- |
| Lletres «r» a «strawberry» (la resposta correcta és 3) | | |
| Lletres «r» a «ferrocarril» (la resposta correcta és 4) | | |
| Frase en català (s'entén? té errors?) | | |
| 17 × 23 (la resposta correcta és 391) | | |
| Ha respost en català? | | |
| Velocitat (tokens per segon) | | |

### Preguntes

1. Quines diferències de qualitat observeu entre els dos models?
2. I de velocitat? Quin és l'equilibri entre mida, qualitat i recursos?
3. Per què creieu que comptar lletres és difícil per a un LLM? (Pista: el model veu tokens, no lletres.)

## Exercici 10: sortida estructurada en JSON

**Objectiu:** obtenir respostes que un programa pugui llegir. Quan un LLM forma part d'una aplicació, la resposta sovint ha de ser JSON vàlid, no text lliure.

**Predicció (abans de començar):** si demaneu al model que respongui en JSON, la resposta es podrà llegir directament amb `json.loads`?

Aquest exercici no necessita `lab.py`: feu servir directament l'ordre `ollama run`.

1. Deseu aquest prompt en una variable de PowerShell:

   ```powershell
   $prompt = "Extreu les dades d'aquesta línia de registre: «ERROR 2026-11-20 14:32 al servidor db-02: connexió rebutjada al port 5432.» Respon en JSON amb les claus nivell, data, hora, servidor i port."
   ```

2. Executeu-lo primer sense `--format` i després amb `--format json` (que demana a Ollama que la resposta sigui JSON), i compareu les dues respostes. Fixeu-vos en la primera i l'última línia de cada una:

   ```powershell
   ollama run gemma3:4b $prompt
   ollama run gemma3:4b --format json $prompt
   ```

3. Repetiu les dues ordres 3 vegades. La temperatura per defecte és 1, així que cada resposta pot ser diferent. La resposta amb `--format json` continua sent JSON pur cada vegada?
4. Mireu el valor del camp `port` a les respostes: és un número o un text?

### Preguntes

1. Per què fallaria `json.loads` amb la primera resposta (la de sense `--format`), si el contingut sembla correcte?
2. Què fa `--format json`? Garanteix que les dades siguin correctes o només que el format sigui vàlid? (Penseu en el camp `port`.)
3. En quin tipus d'aplicació necessitaríeu que el model respongués sempre en JSON?

## Lliurament

El lliurament és un **repositori privat de GitHub** amb les respostes en Markdown i els fitxers que heu generat durant l'activitat. Al Moodle només cal lliurar l'adreça (URL) del repositori, dins del termini indicat.

- El repositori és **privat** i hi heu afegit el professorat com a col·laborador.
- Els scripts de Python i els Modelfile són fitxers del repositori, no text enganxat.
- Feu commits a mesura que avanceu (com a mínim un per exercici), amb missatges que diguin què heu fet. L'historial mostra com heu treballat.

### Criteris d'avaluació

L'activitat s'avalua com a lliurada o no lliurada. Es considera lliurada quan es compleixen **tots** aquests criteris.

- **Lliurament:** l'URL del repositori s'ha lliurat al Moodle dins del termini i el professorat hi pot accedir.
- **Exercicis:** hi són tots els exercicis, de l'1 al 10.
- **Prediccions:** cada exercici té la predicció escrita abans dels resultats.
- **Dades pròpies:** les taules estan completades amb els resultats obtinguts a l'ordinador de l'alumne, amb les repeticions que demana cada exercici.
- **Preguntes:** totes les preguntes dels exercicis estan contestades amb paraules pròpies i fan referència als resultats obtinguts.
- **Script:** hi ha `lab.py` a l'arrel del repositori, amb les opcions dels exercicis fets, i a l'exercici 2 el prompt final.
- **Modelfile:** hi ha el `Modelfile` de l'exercici 8 al repositori i les respostes comparen el model nou amb `gemma3:4b`.
- **Treball original:** les respostes i els resultats són propis, no copiats d'un company; l'historial de commits ho reflecteix.

Si algun criteri no es compleix, l'activitat es considera no lliurada.
