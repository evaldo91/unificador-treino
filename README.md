# Unificador de Treino

Página web que junta o treino exportado do **Hevy** (`.json`) com o arquivo do **relógio** (`.fit`), analisa cada exercício e gera um `.fit` de musculação para importar no **Strava**. Tudo roda no navegador: nenhum arquivo é enviado para servidor algum.

Feito por Evaldo · Butzke Tech · evaldo.butzke@butzke.tech

## O que faz

- Lê vários arquivos de uma vez e pareia cada treino do Hevy com o `.fit` do relógio pelo horário de início (tolerância de 30 minutos).
- Mostra duração, séries, volume, FC média e máxima, calorias e tempo por zona de FC.
- Avalia cada exercício contra a faixa de repetições (padrão 8 a 12) e sugere manter, reduzir ou subir a carga. Avisa sobre descanso longo e séries duplicadas.
- Gera um texto série por série, pronto para colar na descrição da atividade.
- Gera o `.fit` com a FC do relógio e as séries do Hevy, marcado como musculação (`training` / `strength_training`).

## Como usar

1. No Hevy, exporte o treino como `.json`.
2. Pegue o `.fit` do mesmo dia no app do relógio.
3. Abra a página, solte os dois arquivos, ajuste idade e faixa de reps se quiser.
4. Copie o texto e baixe o `.fit`.
5. Envie o `.fit` em <https://www.strava.com/upload/select> e cole o texto na descrição.

A FC máxima é estimada em 220 menos a idade. É uma estimativa, não uma medida.

## Rodar localmente

```bash
python3 -m http.server 8000
# abra http://localhost:8000
```

Precisa de servidor local (e não de abrir o arquivo direto) porque a página carrega `exmap.json` por `fetch`.

## Publicar no GitHub Pages

1. Crie o repositório e envie o código (veja abaixo).
2. Em **Settings → Pages**, escolha **Source: GitHub Actions**.
3. A cada push na `main`, o workflow `.github/workflows/pages.yml` publica a página.

```bash
git init -b main
git add .
git commit -m "Unificador de Treino"
git remote add origin git@github.com:evaldo91/unificador-treino.git
git push -u origin main
```

## Estrutura

```
index.html                  página completa (HTML, CSS e JS em um arquivo)
exmap.json                  nome do exercício no Hevy -> código do exercício no FIT
scripts/gen_exmap.py        regenera o exmap.json
.github/workflows/pages.yml deploy no GitHub Pages
```

## Limitações

- Exercícios que o Hevy exporta com nomes fora do padrão FIT ficam de fora do `.fit` (a página avisa quais).
- Os nomes em português do texto cobrem os exercícios mais comuns; os demais saem em inglês e podem ser editados na caixa de texto.
- O `.fit` é gerado sem assinatura do fabricante. O Strava aceita, mas não o trata como atividade de um dispositivo.
- Se o treino já tiver sincronizado do relógio para o Strava, o envio pode ser recusado como duplicado.

## Licença

MIT. Veja `LICENSE`.
