# Exercici 6: num_predict i tokens

**Objectiu:** entendre que el model compta en **tokens**, no en paraules, i que podem limitar la longitud de la resposta.

**Predicció (abans de començar):** si limiteu la resposta a 20 tokens, el model farà una resposta més curta o quedarà tallada?

**La vostra predicció:**

1. **Actualitzeu `lab.py`:** afegiu l'opció `--num_predict` (va dins d'`options` i només s'ha d'enviar si s'indica) i feu que, després de cada resposta, l'script imprimeixi el nombre de tokens generats (el camp `eval_count` de la resposta d'Ollama). **Comproveu** que el valor surt després de cada resposta: `python lab.py "Hola" --vegades 1 --temperature 0 --seed 1 --num_predict 10` ha de mostrar `seed` i `num_predict` entre les opcions i, després de la resposta, els tokens generats.
2. Feu aquest prompt amb temperatura 0 i tres límits de tokens diferents: 20, 200 i sense límit (`-1`):

   ```powershell
   $prompt = "Explica què és una xarxa neuronal."
   python lab.py $prompt --vegades 1 --temperature 0 --num_predict 20
   python lab.py $prompt --vegades 1 --temperature 0 --num_predict 200
   python lab.py $prompt --vegades 1 --temperature 0 --num_predict -1
   ```

3. A cada resposta, compareu el nombre de tokens generats (`eval_count`) amb el nombre de paraules de la resposta.

## Preguntes

1. Què passa amb la resposta quan `num_predict` és 20?

   **Resposta:**

2. Compareu el començament de la resposta amb `num_predict` 200 i sense límit. El model «sap» que té un límit o simplement es talla? Com aconseguiríeu una resposta curta però completa?

   **Resposta:**

3. El valor d'`eval_count` coincideix amb el nombre de paraules? Per què creieu que no?

   **Resposta:**

4. En quin cas us interessaria limitar els tokens d'una resposta (cost, temps, interfície)?

   **Resposta:**

