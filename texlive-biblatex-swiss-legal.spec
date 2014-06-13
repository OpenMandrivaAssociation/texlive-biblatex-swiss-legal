# revision 32750
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-swiss-legal
# catalog-date 2014-01-21 12:42:17 +0100
# catalog-license lppl1.3
# catalog-version 1.1.2a
Name:		texlive-biblatex-swiss-legal
Version:	1.1.2a
Release:	2
Summary:	Bibliography and citation styles following Swiss legal practice
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-swiss-legal
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-swiss-legal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-swiss-legal.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides biblatex bibliography and citation styles
for documents written in accordance with Swiss legal citation
standards. Currently, the package is usable for French and
German documents.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-base.bbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-base.cbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-bibliography.bbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-bibliography.cbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-de.lbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-fr.lbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-general.bbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-general.cbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-longarticle.bbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-longarticle.cbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-shortarticle.bbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-shortarticle.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-swiss-legal/README
%doc %{_texmfdistdir}/doc/latex/biblatex-swiss-legal/biblatex-swiss-legal.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-swiss-legal/doc_source/biblatex-swiss-legal.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-swiss-legal/doc_source/biblatex-swiss-legal.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
