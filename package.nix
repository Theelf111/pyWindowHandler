{
  stdenv,
  scons,
  pkg-config,
  python313,
}: let
  python = python313;
  pythonPkgs = python.pkgs;
  inherit (pythonPkgs) buildPythonPackage;

  soFile = stdenv.mkDerivation (final: {
    name = "py-window-handler-bindings.so";

    src = builtins.path {
      path = ./cpp-src;
      name = final.name + "-src";
    };

    preBuild = ''
      export LINKFLAGS="`pkg-config --libs-only-l ${toString [python]}`"
      export NAME=$name
    '';

    installPhase = ''
      cp lib$name.so $out
    '';

    nativeBuildInputs = [
      scons
      pkg-config
    ];
    buildInputs = [python];
  });
in
  buildPythonPackage (final: {
    pname = "py-window-handler";
    version = "0.1";

    src = builtins.path {
      path = ./python-src;
      name = final.pname + "-src";
    };

    propagatedBuildInputs = [
      python.pkgs.setuptools
    ];

    pyproject = true;

    installPhase = ''
      cp ${soFile} ${final.src.name}/pyWindowHandler.so
    '';
  })
