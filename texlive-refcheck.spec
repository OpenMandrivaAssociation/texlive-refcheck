Name:		texlive-refcheck
Version:	29128
Release:	2
Summary:	Check references (in figures, table, equations, etc)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/refcheck
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refcheck.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refcheck.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
