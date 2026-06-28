{
  python3Packages,
  lib,
}:
python3Packages.buildPythonApplication {
  pname = "theLabyrinth";
  version = "0.1.0";
  src = ./.;

  pyproject = true;

  propagatedBuildInputs = with python3Packages; [
    textual
    rich
    rich-pixels
    requests
    pillow
  ];

  meta = with lib; {
    description = "Terminal \"Guess the Word\" game in Python + Textual";
    license = licenses.mit;
  };
}
