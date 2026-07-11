%global tl_name jadetex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.13
Release:	%{tl_revision}.1
Summary:	Macros supporting Jade DSSSL output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/formats/jadetex
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jadetex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jadetex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jadetex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(amsfonts)
Requires:	texlive(babel)
Requires:	texlive(bigintcalc)
Requires:	texlive(bitset)
Requires:	texlive(cm)
Requires:	texlive(colortbl)
Requires:	texlive(cyrillic)
Requires:	texlive(dehyph)
Requires:	texlive(ec)
Requires:	texlive(etoolbox)
Requires:	texlive(fancyhdr)
Requires:	texlive(firstaid)
Requires:	texlive(gettitlestring)
Requires:	texlive(graphics)
Requires:	texlive(graphics-cfg)
Requires:	texlive(graphics-def)
Requires:	texlive(hycolor)
Requires:	texlive(hyperref)
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive(iftex)
Requires:	texlive(infwarerr)
Requires:	texlive(intcalc)
Requires:	texlive(jadetex.bin)
Requires:	texlive(knuth-lib)
Requires:	texlive(kvdefinekeys)
Requires:	texlive(kvoptions)
Requires:	texlive(kvsetkeys)
Requires:	texlive(l3backend)
Requires:	texlive(l3kernel)
Requires:	texlive(latex)
Requires:	texlive(latex-fonts)
Requires:	texlive(ltxcmds)
Requires:	texlive(marvosym)
Requires:	texlive(passivetex)
Requires:	texlive(pdfescape)
Requires:	texlive(pdftex)
Requires:	texlive(pdftexcmds)
Requires:	texlive(psnfss)
Requires:	texlive(refcount)
Requires:	texlive(rerunfilecheck)
Requires:	texlive(stmaryrd)
Requires:	texlive(stringenc)
Requires:	texlive(symbol)
Requires:	texlive(tex)
Requires:	texlive(tex-ini-files)
Requires:	texlive(tipa)
Requires:	texlive(tools)
Requires:	texlive(ulem)
Requires:	texlive(unicode-data)
Requires:	texlive(uniquecounter)
Requires:	texlive(url)
Requires:	texlive(wasysym)
Requires:	texlive(zapfding)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Macro package on top of LaTeX to typeset TeX output of the Jade DSSSL
implementation.

