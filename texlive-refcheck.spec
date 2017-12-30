# revision 29128
# category Package
# catalog-ctan /macros/latex/contrib/refcheck
# catalog-date 2012-06-26 13:14:08 +0200
# catalog-license gpl
# catalog-version 1.7
Name:		texlive-refcheck
Version:	1.9.1
Release:	1
Summary:	Check references (in figures, table, equations, etc)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/refcheck
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refcheck.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refcheck.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package checks references in a document, looking for
numbered but unlabelled equations, for labels which are not
used in the text, for unused bibliography references. It can
also display label names in text near corresponding numbers of
equations and/or bibliography references.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/refcheck/refcheck.sty
%doc %{_texmfdistdir}/doc/latex/refcheck/README
%doc %{_texmfdistdir}/doc/latex/refcheck/refdemo.pdf
%doc %{_texmfdistdir}/doc/latex/refcheck/refdemo.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
