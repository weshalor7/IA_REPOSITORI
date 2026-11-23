# Exercici 9: la mida del model

**Objectiu:** comparar un model petit i un de més gran amb els mateixos prompts i la mateixa configuració.

**Predicció (abans de començar):** en què creieu que es notarà més la diferència entre el model petit i el gran?

**La vostra predicció:**

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

## Preguntes

1. Quines diferències de qualitat observeu entre els dos models?

   **Resposta:**

2. I de velocitat? Quin és l'equilibri entre mida, qualitat i recursos?

   **Resposta:**

3. Per què creieu que comptar lletres és difícil per a un LLM? (Pista: el model veu tokens, no lletres.)

   **Resposta:**

