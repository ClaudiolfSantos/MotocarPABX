# MotocarPABX

Sistema de PABX da **Motocar**, baseado em **FreePBX 17** e **Asterisk** para **Debian 12 (bookworm)**.

Repositório oficial no GitHub: https://github.com/ClaudiolfSantos/MotocarPABX

## Estrutura do Projeto

```text
MotocarPABX/
├── assets/
│   └── branding/
│       ├── motocar-vermelha.png        # Logotipo oficial Motocar (original)
│       ├── motocar-logo-nav.png        # Logotipo para a barra superior
│       ├── motocar-logo-footer.png     # Logotipo compacto para o rodapé
│       ├── motocar-logo-login.png      # Logotipo para a tela de login
│       ├── motocar-badge.png           # Ícone quadrado (Apple Touch Icon)
│       └── favicon.ico                 # Favicon multi-resolução Motocar
├── docs/
│   └── repositorio-github.md           # Referência do repositório oficial
├── freepbx/
│   ├── framework/                      # Núcleo do painel MotocarPABX (FreePBX 17)
│   └── modules/                        # 78 módulos FreePBX 17
├── installer/
│   └── debian/
│       ├── README.md
│       ├── apply_motocar_branding.sh   # Aplica tema branco/vermelho, logos e remove anúncios
│       └── sng_freepbx_debian_install.sh  # Instalador oficial para Debian 12
├── .gitignore
└── README.md
```

## Teste Local no Mac (OrbStack)

Para testar no macOS de forma isolada, sem alterar o sistema do Mac nem o servidor Debian de produção:

```bash
# Iniciar a VM Debian no OrbStack
orb start debian

# Acessar o painel web no navegador
# http://debian.orb.local/admin/config.php

# Pausar/parar a VM após os testes
orb stop debian

# (Opcional) Clonar a VM para testes descartáveis sem alterar a VM atual
orb clone debian motocar-teste
```

## Instalação em Servidor Debian 12 (bookworm)

Em um servidor **Debian 12 (bookworm)** limpo, execute como `root`:

```bash
bash installer/debian/sng_freepbx_debian_install.sh
bash installer/debian/apply_motocar_branding.sh
```

Consulte detalhes adicionais em [installer/debian/README.md](installer/debian/README.md).
