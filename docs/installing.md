# Installing

## Using the Flake

### Flake Input

```nix
outputs = { self, theLabyrinth, nixpkgs, flake-utils, ... }:
  flake-utils.lib.eachDefaultSystem (system:
    {
      devShells.default = nixpkgs.legacyPackages.${system}.mkShell {
        buildInputs = [ theLabyrinth.packages.${system}.default ];
      };
    }
  );
```

### Overlay

```nix
outputs = { self, theLabyrinth, nixpkgs, flake-utils, ... }:
  flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs {
        inherit system;
        overlays = [ theLabyrinth.overlays.default ];
      };
    in
    {
      packages.default = pkgs.theLabyrinth;
    }
  );
```

## Nix (Any system with the Nix package manager)

### Install

```bash
nix profile install github:the-penwing/the-labyrinth
theLabyrinth
```

### Uninstall

```bash
nix profile remove theLabyrinth
```

### Run Without Installation

```bash
nix run github:the-penwing/the-labyrinth
```
