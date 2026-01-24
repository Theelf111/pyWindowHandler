{
  stdenv,
  scons,
  pkg-config,
  python313Packages,
}: let
  inherit (python313Packages) python;
  libs = [python];
in
  stdenv.mkDerivation (final: {
    pname = "pyWindowHandler";
    version = "0.1";

    src = builtins.path {
      path = ./.;
      name = final.pname + "-src";
    };

    preBuild = ''
      export LINKFLAGS="`pkg-config --libs-only-l ${toString libs}`"
      export NAME=$pname
    '';

    installPhase = ''
      mkdir $out/bin
      ls
      cp lib$pname.so $out/bin/$pname.so
    '';

    nativeBuildInputs = [
      scons
      pkg-config
    ];
    buildInputs = libs;
  })
