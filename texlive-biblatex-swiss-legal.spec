%global tl_name biblatex-swiss-legal
%global tl_revision 78431

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.2a
Release:	%{tl_revision}.1
Summary:	Bibliography and citation styles following Swiss legal practice
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-swiss-legal
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-swiss-legal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-swiss-legal.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides BibLaTeX bibliography and citation styles for
documents written in accordance with Swiss legal citation standards in
either French or German. However, according to
https://tex.stackexchange.com/questions/426142/bibliography-usi ng-
biblatex-swiss-legal-not-displayed-correctly the package is at present
outdated and does not work properly with newer versions of BibLaTeX.

