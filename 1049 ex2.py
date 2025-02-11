def identificar_animal(palavra1, palavra2, palavra3):
    classificacao = {
        "vertebrado": {
            "ave": {
                "carnivoro": "aguia",
                "onivoro": "pomba"
            },
            "mamifero": {
                "onivoro": "homem",
                "herbivoro": "vaca"
            }
        },
        "invertebrado": {
            "inseto": {
                "hematofago": "pulga",
                "herbivoro": "lagarta"
            },
            "anelideo": {
                "hematofago": "sanguessuga",
                "onivoro": "minhoca"
            }
        }
    }

    return classificacao.get(palavra1, {}).get(palavra2, {}).get(palavra3, "Animal não encontrado")

palavra1 = input().strip().lower()
palavra2 = input().strip().lower()
palavra3 = input().strip().lower()

print(identificar_animal(palavra1, palavra2, palavra3))
