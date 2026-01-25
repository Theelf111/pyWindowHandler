{
  stdenv,
  scons,
  pkg-config,
  python313,
  glfw3,
  glew,
  moduleName ? "pyWindowHandler",
}: let
  python = python313;
  pythonPkgs = python.pkgs;
  inherit (pythonPkgs) buildPythonPackage;

  mainFileStart = ''
    import ctypes

    bindings = ctypes.CDLL(path)
  '';

  mainFileEnd = ''
    del path
    del ctypes
    del bindings
  '';

  pyproject = version: ''
    [project]
    name = \"${moduleName}\"
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
        export LINKFLAGS="`pkg-config --libs-only-l ${toString ["glfw3" "glew"]}`"
        export NAME=$name
      '';

      installPhase = let
        dir = "$out/${moduleName}";
      in ''
        mkdir ${dir}
        touch ${dir}/__init__.py
        echo "path = \"`echo ${dir}/bindings.so`\"
        " > ${dir}/__init__.py
        echo "${mainFileStart}" >> ${dir}/__init__.py
        cat "${./main.py}" >> ${dir}/__init__.py
        echo "${mainFileEnd}" >> ${dir}/__init__.py
        touch $out/pyproject.toml
        echo "${pyproject version}" > $out/pyproject.toml

        cp lib$name.so ${dir}/bindings.so
      '';

      nativeBuildInputs = [
        scons
        pkg-config
      ];
      buildInputs = [
        glfw3
        glew
      ];
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
