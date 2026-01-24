{pkgs ? import <nixpkgs> {}}:
pkgs.callPackage ./package.nix {
  bindings = ["test"]; # Outdated
}
