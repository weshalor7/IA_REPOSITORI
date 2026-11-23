# Exercici 8: missatge de sistema i Modelfile

**Objectiu:** canviar la «personalitat» i els paràmetres del model de manera permanent creant-ne una variant.

**Predicció (abans de començar):** el missatge de sistema canviarà només el to de la resposta o també el contingut?

**La vostra predicció:**

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

Deseu el fitxer `Modelfile` que heu creat en aquesta carpeta (`exercici-08/`).

## Preguntes

1. Quina diferència veieu entre `gemma3:4b` i la vostra variant amb el mateix prompt?

   **Resposta:**

2. Dins la sessió del model nou, escriviu `/show parameters`: quina temperatura hi apareix? Quina relació té amb la línia `PARAMETER` del Modelfile?

   **Resposta:**

3. Per què el missatge de sistema és tan important a l'hora de construir un assistent?

   **Resposta:**

4. Amb la personalitat que heu donat al model al pas 4, la resposta continuava sent útil i correcta? Quin risc té donar massa «personalitat» a un assistent?

   **Resposta:**

