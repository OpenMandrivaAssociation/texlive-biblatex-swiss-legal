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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides BibLaTeX bibliography and citation styles for
documents written in accordance with Swiss legal citation standards in
either French or German. However, according to
https://tex.stackexchange.com/questions/426142/bibliography-usi ng-
biblatex-swiss-legal-not-displayed-correctly the package is at present
outdated and does not work properly with newer versions of BibLaTeX.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-swiss-legal
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-swiss-legal/doc_source
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-swiss-legal/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-swiss-legal/biblatex-swiss-legal.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-swiss-legal/doc_source/biblatex-swiss-legal.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-swiss-legal/doc_source/biblatex-swiss-legal.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-base.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-base.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-bibliography.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-bibliography.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-de.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-fr.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-general.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-general.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-longarticle.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-longarticle.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-shortarticle.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-shortarticle.cbx
