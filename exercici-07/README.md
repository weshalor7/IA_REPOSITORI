# Exercici 7: num_ctx, la memòria del model

**Objectiu:** comprovar que el model només «recorda» el que cap dins la finestra de context.

El **context** (`num_ctx`) és la «memòria de treball» del model: el nombre màxim de tokens que pot tenir en compte alhora. Si el text és més llarg que el context, el model no el pot tenir tot a la vista.

**Predicció (abans de començar):** si el text és més llarg que el context, quina part creieu que oblidarà el model: el principi o el final?

**La vostra predicció:**

## Preparar els textos

1. A la carpeta `exercici-07/` hi ha l'ajudant `genera_text.py`, que genera un text llarg de la mida (en tokens) que li demaneu: comença amb la frase de `--inici` (el secret), continua amb frases de farciment i acaba amb la de `--final` (la pregunta). Només fa servir Ollama per comptar tokens: **no li fa cap pregunta**. No cal que el llegiu a fons.
2. Genereu dos textos de mides diferents, des de l'arrel del repositori i amb l'entorn virtual activat. Es creen `text_1000.txt` i `text_6000.txt`, amb el secret al principi i la pregunta al final, i l'ajudant us diu quants tokens té exactament cadascun:

   ```powershell
   $inici = "El codi secret és PASSWORD-1234. Recorda'l."
   $final = "Pregunta: quin era el codi secret? Respon en una sola frase."
   python exercici-07/genera_text.py 1000 --inici $inici --final $final
   python exercici-07/genera_text.py 6000 --inici $inici --final $final
   ```

## Actualitzar l'script

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

## Fer les proves

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

## Preguntes

1. Mireu la taula. Amb quines combinacions de mida del text i `num_ctx` recorda el codi el model i amb quines no? Quina relació hi ha entre la mida del text i `num_ctx`?

   **Resposta:**

2. Per què el model «omet» el principi del text quan aquest és més llarg que el context?

   **Resposta:**

3. Quin problema pràctic us podeu trobar si feu servir un model local per resumir documents llargs?

   **Resposta:**

4. Si amb 2048 el model ha respost una cosa inventada o ha negat que hi hagi cap codi: per què és perillós que ho digui amb seguretat, en lloc de dir que no ho sap?

   **Resposta:**

