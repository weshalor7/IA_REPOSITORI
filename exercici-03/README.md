# Exercici 3: la temperatura depèn de la tasca

**Objectiu:** comprovar que no hi ha una temperatura «millor»: una tasca de precisió i una de creativitat necessiten valors diferents. També veureu que una temperatura baixa fa el model més consistent, però no el fa encertar més: si no sap fer una tasca, s'equivoca igualment.

**Predicció (abans de començar):** amb quina temperatura creieu que el model encertarà més una multiplicació? I amb quina proposarà noms més variats?

**La vostra predicció:**

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

## Preguntes

1. Amb quina temperatura funciona millor cada tasca? Per què?

   **Resposta:**

2. Quina temperatura triaríeu per a un assistent de codi? I per un generador de noms de projectes o de startups tecnològiques?

   **Resposta:**

per a un generador d'idees per a un eslògan?
3. Amb temperatura 0, el model ha donat sempre la mateixa resposta al prompt A? Era correcta? Que una resposta sigui consistent vol dir que sigui correcta? Com resoldríeu aquest problema en una aplicació real?

   **Resposta:**

