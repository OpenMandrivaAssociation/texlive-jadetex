# revision 23409
# category Package
# catalog-ctan /macros/jadetex/jadetex-3.13.tar.gz
# catalog-date 2008-04-20 19:53:04 +0200
# catalog-license other-free
# catalog-version 3.13
Name:		texlive-jadetex
Version:	3.13
Release:	5
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
Requires(post):	texlive-tetex
Requires:	texlive-latex
Requires:	texlive-pdftex
Requires:	texlive-tex
Requires:	texlive-jadetex.bin
%rename jadetex

%description
Macro package on top of LaTeX to typeset TeX output of the Jade
DSSSL implementation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/jadetex <<EOF
#
# from jadetex:
jadetex pdftex language.dat *jadetex.ini
pdfjadetex pdftex language.dat *pdfjadetex.ini
EOF


%changelog
* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.13-4
+ Revision: 778434
- Rebuild after tlpobj2spec.pl bug correction.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.13-3
+ Revision: 752892
- Rebuild to reduce used resources

* Sun Nov 13 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.13-2
+ Revision: 730326
- Use rename macro instead of mix of provides/conflicts/obsoletes

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.13-1
+ Revision: 718966
- texlive-jadetex
- texlive-jadetex
- texlive-jadetex
- texlive-jadetex
- texlive-jadetex
- texlive-jadetex

