# Kom i gang på DAPLA

Dette repoet er ment å være en enkel beskrivelse av hvordan man tar i bruk SSB sin nye skyplattform DAPLA. Besøk hjemmesiden på denne adressen: https://manual.dapla.ssb.no/

## Avhengigheter

For å kunne åpne dapla-manualen lokalt trenger man `quarto`.

### Installer med pipx

1. [Installer pipx](https://pipx.pypa.io/stable/how-to/install-pipx/)
1. `pipx install quarto-cli`

### Installer med uv

1. [Installer uv](https://docs.astral.sh/uv/getting-started/installation/)
1. `uv tool install quarto-cli`

### Installer med Nix

Hvis du bruker Nix kan du få dette gjennom `nix develop .#` kommandoen i rotmappen.

## Bidra

Kjør følgende kommando for å se preview av manualen mens du jobber: `quarto preview dapla-manual`.

For å legge til nye elementer i menyen må filen `dapla-manual/_quarto.yml` oppdateres.

> [!WARNING]
> Notebooks i dette repoet bør ikke strippes, i det output er vist i selve manualen. Kjøre kommandoen under for å slå av stripping kun for dette repoet.

```shell
git config --local include.path ../.gitconfig
```
