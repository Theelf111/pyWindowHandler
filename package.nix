{
  stdenv,
  scons,
  pkg-config,
  python313,
}: let
  python = python313;
  pythonPkgs = python.pkgs;
  inherit (pythonPkgs) buildPythonPackage;

  bindings = ["test"];

  mainFileText =
    ''
      from ctypes import CDLL

      bindings = CDLL(path)

    ''
    + builtins.concatStringsSep "\n" (map (x: "${x} = bindings.${x}") bindings)
    + "\n"
    + ''
      del bindings
      del path
    '';

  pyproject = version: ''
    [project]
    name = \"pyWindowHandler\"
    version = \"${version}\"

    [tool.setuptools.packages]
    find = {}
  '';

  pythonSource = version:
    stdenv.mkDerivation (final: {
      name = "py-window-handler-python-src";

      src = builtins.path {
        path = ./src;
        name = final.name + "-src";
      };

      preBuild = ''
        export LINKFLAGS="`pkg-config --libs-only-l ${toString []}`"
        export NAME=$name
      '';

      installPhase = let
        dir = "$out/pyWindowHandler";
      in ''
        mkdir ${dir}
        touch ${dir}/__init__.py
        echo "path = \"`echo $out/pyWindowHandler/bindings.so`\"
        " > ${dir}/__init__.py
        echo "${mainFileText}" >> ${dir}/__init__.py
        touch $out/pyproject.toml
        echo "${pyproject version}" > $out/pyproject.toml

        cp lib$name.so ${dir}/bindings.so
      '';

      nativeBuildInputs = [
        scons
        pkg-config
      ];
      buildInputs = [];
    });
in
  buildPythonPackage (final: {
    pname = "py-window-handler";
    version = "0.1";

    src = builtins.path {
      path = (pythonSource final.version).outPath;
      name = final.pname + "-src";
    };

    propagatedBuildInputs = [
      python.pkgs.setuptools
    ];

    pyproject = true;
  })
