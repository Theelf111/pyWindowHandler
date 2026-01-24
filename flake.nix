{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = {nixpkgs, ...}: let
    inherit (nixpkgs) lib;
    forEachSystem = lib.genAttrs lib.systems.flakeExposed;
    localPkgs = system: nixpkgs.legacyPackages.${system};
  in {
    packages = forEachSystem (system: let
      pkgs = localPkgs system;
    in rec {
      py-window-handler = pkgs.callPackage ./package.nix {
        bindings = [
          "test"
        ];
      };

      default = py-window-handler;

      environment = pkgs.python313.withPackages (_: [py-window-handler]);
    });
  };
}
