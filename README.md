# Dapla-manualen for internt innhold

Dette repoet inneholder nå en ny versjon av Dapla-manualen, som er tilpasset den nye Dapla-team strukturen. Den har også gjennomgått større endringer i organiseringen av innholdet.

På sikt er det ment at dette repoet skal inneholde kapitler i boken som ikke skal eksponeres mot resten av verden, og derfor har repoet postfixen `-internal`.

[website](https://probable-waddle-o4w1og1.pages.github.io/)

## Bidra

Kjør følgende kommando for å se preview av manualen mens du jobber: `quarto preview dapla-manual`.

For å legge til nye elementer i menyen må filen `dapla-manual/_quarto.yml` oppdateres.

> [!WARNING]
> Notebooks i dette repoet bør ikke strippes, i det output er vist i selve manualen. Kjøre kommandoen under for å slå av stripping kun for dette repoet.

```shell
git config --local include.path ../.gitconfig
```
