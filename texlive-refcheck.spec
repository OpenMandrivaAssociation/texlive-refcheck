%global tl_name refcheck
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9.2
Release:	%{tl_revision}.1
Summary:	Check references (in figures, table, equations, etc)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/refcheck
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refcheck.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refcheck.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package checks references in a document, looking for numbered but
unlabelled equations, for labels which are not used in the text, for
unused bibliography references. It can also display label names in text
near corresponding numbers of equations and/or bibliography references.

