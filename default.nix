let
  nixpkgs = import <nixpkgs> {};
in
with nixpkgs;
with import ./project.nix;
stdenv.mkDerivation {
  name = name;
  
  src = builtins.path {
    path = ./.;
    name = name + "-src";
  };

  preBuild = ''
    export LINKFLAGS="`pkg-config --libs-only-l ${lib.strings.concatStringsSep " " libs}`"
    export NAME=$name
  '';

  installPhase = ''
    mkdir $out/bin
    ls
    cp lib$name.so $out/bin/$name.so
  '';

  nativeBuildInputs = [
    scons
    pkg-config
  ];
  buildInputs = builtins.map (x: nixpkgs."${x}") libs;
}
