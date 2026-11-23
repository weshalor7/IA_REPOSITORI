"""Ajudant de l'exercici 7: genera un text llarg de la mida que li demaneu.

El text comença amb la frase de --inici (el secret), continua amb farciment
i acaba amb la frase de --final (la pregunta). Fa servir Ollama NOMÉS per
comptar els tokens exactes del text (no li fa cap pregunta) i ajusta la
mida fins que s'hi acosta.

Ús (des de l'arrel del repositori):
    python exercici-07/genera_text.py 3000 --inici "..." --final "..."

Crea el fitxer text_<tokens>.txt a la carpeta on l'executeu.
"""
import argparse

import ollama

MODEL = "gemma3:4b"
FRASES = [
    "A la meva màquina funciona, així que el problema deu ser el teu ordinador.",
    "Algú va esborrar la base de dades de producció un divendres a les cinc de la tarda.",
    "Ningú sap qui va escriure aquest programa, però tothom té por de tocar-lo.",
    "El programa va fallar per un punt i coma i vam trigar tres hores a trobar-lo.",
    "El servidor es va reiniciar sol a mitjanit i ningú no en vol parlar.",
    "Hem apagat l'ordinador i l'hem tornat a encendre, i curiosament ha funcionat.",
    "El commit es deia «arreglat definitiu», però el definitiu número set tampoc no va funcionar.",
    "El cafè s'ha acabat i el projecte s'ha de lliurar demà a les vuit del matí.",
    "El wifi de l'aula va caure just quan tothom feia l'examen de xarxes.",
    "El gat del veí ha passejat pel teclat i ha fet un commit a la branca principal.",
]


def construeix(inici, final, repeticions):
    farciment = " ".join(FRASES[i % len(FRASES)] for i in range(repeticions))
    return inici + "\n\n" + farciment + "\n\n" + final


def compta_tokens(text, objectiu):
    # Demanem 1 sol token: la resposta diu quants tokens té el prompt.
    r = ollama.generate(
        model=MODEL,
        prompt=text,
        options={"num_ctx": objectiu * 3, "num_predict": 1},
    )
    return r["prompt_eval_count"]


parser = argparse.ArgumentParser(description="Genera un text llarg d'una mida donada en tokens.")
parser.add_argument("tokens", type=int, nargs="?", default=3000, help="mida aproximada (per defecte, 3000)")
parser.add_argument("--inici", required=True, help="frase del principi (el secret)")
parser.add_argument("--final", required=True, help="frase del final (la pregunta)")
args = parser.parse_args()

objectiu = args.tokens
repeticions = max(1, objectiu // 30)  # primera estimació (curta)
for _ in range(4):
    text = construeix(args.inici, args.final, repeticions)
    tokens = compta_tokens(text, objectiu)
    if abs(tokens - objectiu) <= objectiu * 0.02:
        break
    repeticions = max(1, round(repeticions * objectiu / tokens))

nom = f"text_{objectiu}.txt"
with open(nom, "w", encoding="utf-8") as f:
    f.write(text)
print(f"{nom} creat: {tokens} tokens exactes ({len(text.split())} paraules).")
