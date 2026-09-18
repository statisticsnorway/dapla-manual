{
  description = "Development environment for the dapla manual";

  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "https://channels.nixos.org/nixpkgs-unstable/nixexprs.tar.zst";
    nixpkgs-quarto.url = "github:NixOS/nixpkgs/20075955deac2583bb12f07151c2df830ef346b4";
  };

  outputs = inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" "x86_64-darwin" ];
      perSystem = { config, inputs', pkgs, ... }: {
        devShells.default = pkgs.mkShell {
          name = "Dapla manual devShell";
          packages = with pkgs; [
            # quarto from latest nixpkgs-unstable is broken
            # quarto
            inputs'.nixpkgs-quarto.legacyPackages.quarto
          ];
        };
      };
    };
}
