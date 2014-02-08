# revision 21094
# category Package
# catalog-ctan /macros/latex/contrib/refcheck
# catalog-date 2007-01-06 10:07:33 +0100
# catalog-license gpl
# catalog-version 1.7
Name:		texlive-refcheck
Version:	1.7
Release:	3
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
Intended to check references in a document, looking for
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.7-2
+ Revision: 755652
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.7-1
+ Revision: 719442
- texlive-refcheck
- texlive-refcheck
- texlive-refcheck
- texlive-refcheck

