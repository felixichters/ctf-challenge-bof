{
  description = "dev-shell it-sec";

  inputs.nixpkgs.url = "nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }: 
		let 
			system = "x86_64-linux";
			pkgs = import nixpkgs { inherit system; };
		in 
		{
    devShells.${system}.default = pkgs.mkShell {
      nativeBuildInputs = with pkgs; [
				python3Packages.pwntools      
				python3Packages.python-utils
				];

      shellHook = ''
      '';
    };
  };
}

