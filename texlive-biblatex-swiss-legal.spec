# revision 26210
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-swiss-legal
# catalog-date 2012-04-28 17:44:11 +0200
# catalog-license nosource
# catalog-version 1.0 alpha
Name:		texlive-biblatex-swiss-legal
Version:	1.0alpha
Release:	1
Summary:	Bibliography and citation styles following Swiss legal practice
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-swiss-legal
License:	NOSOURCE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-swiss-legal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-swiss-legal.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides biblatex bibliography and citation styles
for documents written in accordance with Swiss legal citation
standards. Currently, the package is only usable for French
documents; translations to German and Italian are under
development for future versions.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-fr.lbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-general.bbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-general.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-swiss-legal/README
%doc %{_texmfdistdir}/doc/latex/biblatex-swiss-legal/biblatex-swiss-legal.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-swiss-legal/doc_source/biblatex-swiss-legal.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-swiss-legal/doc_source/biblioinstructions.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-swiss-legal/doc_source/listerevuesCH.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
