# Exercici 5: top_k i top_p

**Objectiu:** veure com limitem els candidats entre els quals el model tria el token següent.

**Predicció (abans de començar):** què creieu que passarà si el model només pot triar entre 2 candidats? I si pot triar entre tots?

**La vostra predicció:**

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

## Preguntes

1. Ordeneu A, B i C de més a menys varietat. Per què `top_k` 2 i `top_p` 0.3 redueixen el nombre d'emojis diferents?

   **Resposta:**

2. Quin valor de `top_k` hauria de tenir la configuració B perquè el model es comportés com si la temperatura fos 0? Per què?

   **Resposta:**

3. Compareu les configuracions D i E. Quants emojis diferents surten a cada una? Quin és l'emoji més inesperat o amb menys sentit com a resposta, i a quina configuració ha aparegut? Per què `top_k` i `top_p` ajuden a evitar respostes sense sentit quan la temperatura és alta?

   **Resposta:**

