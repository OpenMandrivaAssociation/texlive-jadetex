# revision 23409
# category Package
# catalog-ctan /macros/jadetex/jadetex-3.13.tar.gz
# catalog-date 2008-04-20 19:53:04 +0200
# catalog-license other-free
# catalog-version 3.13
Name:		texlive-jadetex
Version:	3.13
Release:	1
Summary:	Macros supporting Jade DSSSL output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/jadetex/jadetex-3.13.tar.gz
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jadetex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jadetex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jadetex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-latex
Requires:	texlive-pdftex
Requires:	texlive-tex
Requires:	texlive-jadetex.bin
Provides:	jadetex = %{version}
Provides:	texlive-jadetex = %{version}
Provides:	texlive-texmf-jadetex = %{version}
Obsoletes:	jadetex <= 3.12
Conflicts:	jadetex <= 3.12
Obsoletes:	texlive-texmf-jadetex <= 2007
Conflicts:	texlive-texmf-jadetex <= 2007
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3
Requires(post):	texlive-tetex

%description
Macro package on top of LaTeX to typeset TeX output of the Jade
DSSSL implementation.

%pre
    %_texmf_fmtutil_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post
    %_texmf_fmtutil_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_fmtutil_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
	%_texmf_fmtutil_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/jadetex/base/dsssl.def
%{_texmfdistdir}/tex/jadetex/base/jadetex.ini
%{_texmfdistdir}/tex/jadetex/base/jadetex.ltx
%{_texmfdistdir}/tex/jadetex/base/pdfjadetex.ini
%{_texmfdistdir}/tex/jadetex/base/uentities.sty
%{_texmfdistdir}/tex/jadetex/base/ut1omlgc.fd
%_texmf_fmtutil_d/jadetex
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/ChangeLog
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/ChangeLog-old
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/Makefile
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/demo.sgm
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/docbook.dsl
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/index.html
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/index.xml
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/index.xsl
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/jadetex.1
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/jadetex.cfg
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/logo.png
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/pdfjadetex.1
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/releasenotes.dsl
%doc %{_texmfdistdir}/doc/otherformats/jadetex/base/releasenotes.xml
#- source
%doc %{_texmfdistdir}/source/jadetex/base/Makefile
%doc %{_texmfdistdir}/source/jadetex/base/jadetex.dtx
%doc %{_texmfdistdir}/source/jadetex/base/jadetex.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/jadetex <<EOF
jadetex pdftex language.dat *jadetex.ini
pdfjadetex pdftex language.dat *pdfjadetex.ini
EOF
