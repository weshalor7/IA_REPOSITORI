# Exercici 10: sortida estructurada en JSON

**Objectiu:** obtenir respostes que un programa pugui llegir. Quan un LLM forma part d'una aplicació, la resposta sovint ha de ser JSON vàlid, no text lliure.

**Predicció (abans de començar):** si demaneu al model que respongui en JSON, la resposta es podrà llegir directament amb `json.loads`?

**La vostra predicció:**

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

## Preguntes

1. Per què fallaria `json.loads` amb la primera resposta (la de sense `--format`), si el contingut sembla correcte?

   **Resposta:**

2. Què fa `--format json`? Garanteix que les dades siguin correctes o només que el format sigui vàlid? (Penseu en el camp `port`.)

   **Resposta:**

3. En quin tipus d'aplicació necessitaríeu que el model respongués sempre en JSON?

   **Resposta:**

