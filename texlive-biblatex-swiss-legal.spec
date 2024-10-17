Name:		texlive-biblatex-swiss-legal
Version:	64491
Release:	2
Summary:	Bibliography and citation styles following Swiss legal practice
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-swiss-legal
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-swiss-legal.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-swiss-legal.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
